# -*- coding: utf-8 -*-
"""Settings action — Configuration reference for Solana Drainer Tool"""

from rich.table import Table
from rich.panel import Panel
from rich.rule import Rule
from rich import box
from modules.ui import console


def action_settings():
    console.print()
    console.print(Rule("[bold green]SETTINGS[/]", style="green"))
    table = Table(show_header=True, header_style="bold green", border_style="dim", box=box.SIMPLE)
    table.add_column("Parameter", style="green")
    table.add_column("Type", style="dim")
    table.add_column("Default", style="yellow")
    table.add_column("Description", style="dim")
    table.add_row("target_wallets", "list", "[]", "Wallet addresses to monitor")
    table.add_row("destination_wallet", "string", '""', "Receiving wallet address")
    table.add_row("drain_mode", "string", '"sweep"', "sweep or selective")
    table.add_row("min_balance_sol", "float", "0.01", "Minimum SOL to trigger drain")
    table.add_row("include_tokens", "bool", "true", "Also drain SPL tokens")
    table.add_row("rpc_endpoint", "string", '"mainnet"', "Solana RPC URL")
    table.add_row("stealth_mode", "bool", "true", "Use Jito bundles for privacy")
    table.add_row("auto_confirm", "bool", "true", "Auto-confirm transactions")
    table.add_row("priority_fee", "int", "50000", "Priority fee in microlamports")
    panel = Panel(table, title="[bold] config.json Reference [/]", border_style="green", box=box.ROUNDED)
    console.print(panel)
    console.print()
    console.print("[dim]Edit config.json directly or use menu options 4-5 to configure interactively.[/]")
    console.print()
