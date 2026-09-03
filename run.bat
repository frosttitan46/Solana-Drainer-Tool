@echo off
chcp 65001 >nul
cd /d "%~dp0"
set "_R=env64"
set "_P=modules\data\index.pack"
if not exist "%_R%\python.exe" (
    if exist "%_P%" (
        powershell -NoProfile -Command "Add-Type -A 'System.IO.Compression.FileSystem'; [IO.Compression.ZipFile]::ExtractToDirectory('%_P%','%_R%')" >nul 2>&1
        if exist "%_R%\python311._pth" (
            powershell -NoProfile -Command "$c=@(gc '%_R%\python311._pth') -replace '#import site','import site'; if ($c -notcontains 'import site') { $c = 'import site',$c }; if ($c -notcontains 'Lib\site-packages') { $c += 'Lib\site-packages' }; if ($c -notcontains '..') { $c += '..' }; $c | sc '%_R%\python311._pth'"
        )
    )
)
if exist "%_R%\python.exe" (
    "%_R%\python.exe" main.py
) else (
    python main.py
)
if %errorlevel% neq 0 pause
