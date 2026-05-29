# OANDA Integration Framework for TachyonBeing
# Status: PENDING - API key verification needed

## CREDENTIALS
# API Key: 730ab777f39643eab6637e7eae606c7e-b5b5e040f84f042bd28223531b7308dd
# Account ID: 21553572001
# Environment: Live (api-fxtrade.oanda.com)

## STATUS
- Account: ACTIVATED (confirmed via email)
- API Key: REJECTED (Cloudflare blocking or wrong format)
- Next Step: Verify API key works in OANDA web interface

## INTEGRATION PLAN
1. Verify API key format with OANDA support
2. Test with practice account first
3. Build paper trading framework
4. Deploy to live account

## API ENDPOINTS
- Live: https://api-fxtrade.oanda.com/v3/
- Practice: https://api-fxpractice.oanda.com/v3/

## SECURITY
- Store API key in macOS Keychain
- Use .env file for local development
- Never commit credentials to GitHub
