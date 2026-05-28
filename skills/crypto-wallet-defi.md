---
name: crypto-wallet-defi
description: Cryptocurrency wallet integration and DeFi protocol access for autonomous trading
version: 1.0.0
author: TachyonBeing
---

# Crypto Wallet & DeFi Skill

## Purpose
Enable autonomous wallet operations and DeFi protocol interactions for trading capital management.

## Wallets Supported

### MetaMask (Ethereum/ERC20)
- Connection: WalletConnect or injected provider
- Networks: Ethereum, BASE, Optimism, Arbitrum
- Use: Polymarket settlement, DeFi operations

### Phantom (Solana)
- Connection: Wallet adapter
- Use: Jupiter DEX, Solana DeFi

### Bitcoin Lightning
- Connection: Lightning Network API
- Use: Micro-payments, instant settlement

## DeFi Protocols

### Lending
- Aave: Lending/borrowing
- Compound: Algorithmic money market
- Use case: Yield on idle capital

### DEX
- Uniswap: Ethereum swaps
- Jupiter: Solana aggregator
- Aerodrome: BASE DEX
- Use case: Token swaps, liquidity provision

### Yield
- Harvest Finance: Auto-compounding
- Yearn: Yield optimization
- Use case: Passive income on reserves

## Security Protocol

### 1. Multi-Sig Requirement
- All transactions > $100 require human approval
- Daily limit: $500 without approval

### 2. Slippage Protection
- Max slippage: 0.5%
- Revert on failure

### 3. Gas Management
- Max gas: 500,000 units
- Gas price cap: 100 gwei

## Implementation

### MetaMask Connection
```javascript
const provider = new ethers.providers.Web3Provider(window.ethereum);
const signer = provider.getSigner();
```

### DeFi Operations
```javascript
// Aave deposit
const aavePool = new ethers.Contract(AAVE_POOL_ADDRESS, poolABI, signer);
await aavePool.supply(asset, amount, onBehalfOf, referralCode);
```

## Risk Management
- Never store full private keys
- Use hardware wallet for large amounts
- Regular balance audits
- Emergency stop-loss at -15% daily
