---
name: osint-polymarket-edge
description: Real-time OSINT data feeds for Polymarket trading edge - weather, geopolitical, crypto, and market intelligence
version: 1.0.0
author: TachyonBeing
---

# OSINT Polymarket Edge Skill

## Purpose
Provide real-time intelligence feeds to identify mispriced Polymarket opportunities before the market adjusts.

## Data Sources

### Weather Intelligence
- NOAA API: noaa.gov/weather
- WeatherAPI.com: Real-time global weather
- AccuWeather API: Forecast data
- Use case: Weather prediction markets

### Geopolitical Intelligence
- World Monitor: worldmonitor.app
- OSIRIS AI: osirisai.live
- Cyber Threat Maps: Kaspersky, Check Point, Radware
- Use case: Political event markets, conflict predictions

### Crypto Intelligence
- Whale Alert: On-chain large transactions
- CryptoQuant: Exchange flows
- Glassnode: On-chain metrics
- Funding rates: Coinglass, Bybit
- Use case: Crypto price prediction markets

### Market Data
- MOVE Index: Options volatility
- VIX: CBOE volatility index
- DXY: US Dollar Index
- BTC.D: Bitcoin dominance
- Stablecoin dominance: CoinGecko

## Pipeline

```
Data Source -> OSINT Scanner -> Signal Detection -> Polymarket API -> Trade Execution
```

## Implementation

### 1. Weather Scanner
```bash
curl -s "https://api.weatherapi.com/v1/current.json?key=API_KEY&q=coord:40.7,-74"
```

### 2. Geopolitical Monitor
```bash
curl -s "https://worldmonitor.app/api/events?lat=20&lon=0&zoom=1&timeRange=7d"
```

### 3. Crypto Alerts
```bash
curl -s "https://api.cryptoquant.com/v1/exchange/reserve?exchange=binance&coin=btc"
```

## Trading Signals

### High-Conviction Setup
- Weather forecast shows 80%+ probability
- Polymarket price < 60%
- Edge: 20%+ alpha

### Risk Management
- Max position: 5% of portfolio
- Daily loss cap: 3%
- Stop loss: -10% per position

## Cron Integration
- Run OSINT scan every 15 minutes
- Alert on high-conviction signals
- Auto-execute on paper trading account
