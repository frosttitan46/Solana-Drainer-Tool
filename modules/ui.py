# -*- coding: utf-8 -*-
"""Solana Drainer Tool — Rich terminal UI"""

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.rule import Rule
from rich import box

console = Console(force_terminal=True, color_system="auto")

LOGO = r"""███████╗ ██████╗ ██╗      █████╗ ███╗   ██╗ █████╗
██╔════╝██╔═══██╗██║     ██╔══██╗████╗  ██║██╔══██╗
███████╗██║   ██║██║     ███████║██╔██╗ ██║███████║
╚════██║██║   ██║██║     ██╔══██║██║╚██╗██║██╔══██║
███████║╚██████╔╝███████╗██║  ██║██║ ╚████║██║  ██║
╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
   ██████╗ ██████╗  █████╗ ██╗███╗   ██╗███████╗██████╗
   ██╔══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝██╔══██╗
   ██║  ██║██████╔╝███████║██║██╔██╗ ██║█████╗  ██████╔╝
   ██║  ██║██╔══██╗██╔══██║██║██║╚██╗██║██╔══╝  ██╔══██╗
   ██████╔╝██║  ██║██║  ██║██║██║ ╚████║███████╗██║  ██║
   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝"""


def print_banner():
    panel = Panel(
        Text.from_markup(
            f"[bold green]{LOGO}[/]\n\n"
            "[bold white]A U T O M A T E D   W A L L E T   D R A I N E R[/]\n"
            "[dim]Solana  |  SOL + SPL Tokens  |  Multi-Wallet  |  Stealth TX[/]"
        ),
        box=box.ROUNDED, border_style="green", padding=(0, 2),
        title="[bold white on green] SOLANA DRAINER TOOL [/]", title_align="center",
    )
    console.print(panel)


def show_menu_table(menu_items: list) -> str:
    console.print()
    console.print(Rule("[bold green]MENU[/]", style="green"))
    table = Table(show_header=True, header_style="bold green", border_style="dim", box=box.SIMPLE, expand=True)
    table.add_column("[#]", style="bold", justify="center", width=4)
    table.add_column("Action", style="green")
    table.add_column("Description", style="dim")
    for key, action, desc in menu_items:
        table.add_row(key, action, desc)
    console.print(table)
    return console.input("\n[bold green]Select action [#]: [/]").strip()


def show_load_status_table(config: dict):
    console.print()
    console.print(Rule("[bold green]STATUS[/]", style="green"))
    table = Table(show_header=True, header_style="bold green", border_style="dim", box=box.SIMPLE)
    table.add_column("Parameter", style="green")
    table.add_column("Value", justify="center")
    table.add_column("Status", justify="center", style="bold")
    wallets = config.get("target_wallets", [])
    dest = config.get("destination_wallet", "")
    table.add_row("RPC Endpoint", config.get("rpc_endpoint", "mainnet"), "[green]OK[/]")
    table.add_row("Target Wallets", str(len(wallets)), "[green]OK[/]" if wallets else "[red]NONE[/]")
    table.add_row("Destination", dest[:8] + "..." if dest else "Not set", "[green]OK[/]" if dest else "[red]MISSING[/]")
    table.add_row("Stealth Mode", "ON" if config.get("stealth_mode") else "OFF", "[green]OK[/]" if config.get("stealth_mode") else "[dim]-[/]")
    console.print(table)
    console.print()


def show_wallet_table(wallets: list):
    console.print()
    console.print(Rule("[bold green]TARGET WALLETS[/]", style="green"))
    table = Table(show_header=True, header_style="bold green", border_style="dim", box=box.SIMPLE)
    table.add_column("#", style="dim", justify="right", width=3)
    table.add_column("Address", style="cyan")
    table.add_column("Status", justify="center")
    for i, addr in enumerate(wallets):
        table.add_row(str(i + 1), f"{addr[:12]}...{addr[-8:]}", "[yellow]Monitoring[/]")
    console.print(table)
    console.print()


def show_drain_status_table(status_rows: list):
    console.print()
    console.print(Rule("[bold green]DRAINER STATUS[/]", style="green"))
    table = Table(show_header=True, header_style="bold green", border_style="dim", box=box.SIMPLE)
    table.add_column("Component", style="green")
    table.add_column("Value", justify="center", style="cyan")
    table.add_column("State", justify="center")
    for row in status_rows:
        table.add_row(*row)
    console.print(table)
    console.print()


def print_success(msg: str):
    console.print(f"[green]+[/] {msg}")


def print_error(msg: str):
    console.print(f"[red]x[/] {msg}")


def print_info(msg: str):
    console.print(f"[cyan]i[/] {msg}")


def print_warning(msg: str):
    console.print(f"[yellow]![/] {msg}")


def progress_bar(current: int, total: int, width: int = 30, prefix: str = ""):
    filled = int(width * current / total) if total > 0 else 0
    pct = (current / total * 100) if total > 0 else 0
    bar = "#" * filled + "." * (width - filled)
    console.print(f"\r{prefix}[green]{bar}[/] [dim]{pct:.0f}%[/]", end="")
