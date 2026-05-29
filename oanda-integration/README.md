# OANDA Integration Framework for TachyonBeing

## Account Setup
- Live OANDA account created
- Email: tachyonbeing@protonmail.com
- Status: Ready for integration

## API Configuration
- Base URL: https://api-fxtrade.oanda.com/v3
- API Key: Stored in .env
- Python SDK: oanda-v20

## Integration Steps
1. Install oanda-v20 SDK
2. Configure API credentials
3. Test account connection
4. Set up paper trading
5. Run backtests
6. Deploy live trading

## Risk Parameters
- Max position size: 1% of account
- Daily loss limit: 2%
- Max drawdown: 5%
- Stop loss: Mandatory on all positions

## Trading Pairs
- EUR/USD (primary)
- GBP/USD
- USD/JPY
- AUD/USD
- USD/CAD
