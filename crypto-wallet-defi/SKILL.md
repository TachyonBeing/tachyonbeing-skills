---
name: crypto-wallet-defi
description: Multi-wallet management and DeFi protocol integration
category: crypto
---

# Crypto Wallet & DeFi

Multi-wallet management with DeFi protocol integration.

## Wallets

- **MetaMask** (EVM chains)
- **Phantom** (Solana)
- **Lightning** (Bitcoin)
- **TRON** (TRC-20)

## DeFi Protocols

- **Aave** - Lending/borrowing
- **Compound** - Yield generation
- **Uniswap** - DEX swaps
- **Jupiter** - Solana DEX
- **Aerodrome** - Base DEX

## Security

- Private keys in .env only
- Transaction limits enforced
- Human-in-the-loop for large tx
- Multi-sig for critical operations

## Integration

```python
from web3 import Web3
from ethers import Wallet

# Connect wallet
provider = Web3(Web3.HTTPProvider(RPC_URL))
wallet = Wallet(private_key, provider)
```
