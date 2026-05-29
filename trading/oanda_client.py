#!/usr/bin/env python3
"""
TachyonBeing OANDA Integration Framework
Paper trading + live trading ready
"""
import urllib.request
import json
import time
from datetime import datetime

class OANDA_Client:
    def __init__(self, api_key, account_id, environment="live"):
        self.api_key = api_key
        self.account_id = account_id
        if environment == "live":
            self.base_url = "https://api-fxtrade.oanda.com/v3"
        else:
            self.base_url = "https://api-fxpractice.oanda.com/v3"
    
    def _request(self, method, path, data=None):
        url = f"{self.base_url}{path}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        if data:
            data = json.dumps(data).encode()
        req = urllib.request.Request(url, data=data, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req) as resp:
                return json.loads(resp.read())
        except Exception as e:
            return {"error": str(e)}
    
    def get_account(self):
        return self._request("GET", f"/accounts/{self.account_id}")
    
    def get_prices(self, instruments="EUR_USD"):
        return self._request("GET", f"/accounts/{self.account_id}/prices?instruments={instruments}")
    
    def get_positions(self):
        return self._request("GET", f"/accounts/{self.account_id}/positions")
    
    def get_open_trades(self):
        return self._request("GET", f"/accounts/{self.account_id}/trades")
    
    def place_order(self, instrument, units, type="MARKET"):
        order = {
            "order": {
                "unit": str(units),
                "instrument": instrument,
                "type": type,
                "timeInForce": "FOK"
            }
        }
        return self._request("POST", f"/accounts/{self.account_id}/orders", order)
    
    def get_candles(self, instrument, count=100, granularity="H1"):
        return self._request("GET", f"/instruments/{instrument}/candles?count={count}&granularity={granularity}")
    
    def get_instruments(self):
        return self._request("GET", f"/accounts/{self.account_id}/instruments")

# Load credentials
import os
api_key = os.getenv("OANDA_API_KEY") or "36a991ea82cd3312d22848e1690e3435-41ab59875eb940035da25f4dd86398b0"
account_id = os.getenv("OANDA_ACCOUNT_ID") or "001-001-21553572-001"

client = OANDA_Client(api_key, account_id, "live")

# Test connection
print("=== OANDA CONNECTION TEST ===")
account = client.get_account()
if "account" in account:
    acct = account["account"]
    print("Account:", acct["id"])
    print("Balance:", acct["balance"], acct["currency"])
    print("NAV:", acct["NAV"])
    print("Margin Available:", acct["marginAvailable"])
    print("Status: CONNECTED")
else:
    print("ERROR:", account)

# Test price feed
print("\n=== PRICE FEED TEST ===")
prices = client.get_prices("EUR_USD")
if "prices" in prices:
    for p in prices["prices"]:
        print(f"EUR/USD - BID: {p['bid']} ASK: {p['ask']}")
else:
    print("Price error:", prices)

# Test candle data
print("\n=== CANDLE DATA TEST ===")
candles = client.get_candles("EUR_USD", count=5, granularity="H1")
if "candles" in candles:
    print(f"Retrieved {len(candles['candles'])} candles")
    for c in candles["candles"][-3:]:
        print(f"  {c['time']} - O:{c['mid']['o']} H:{c['mid']['h']} L:{c['mid']['l']} C:{c['mid']['c']}")
else:
    print("Candle error:", candles)

print("\n=== OANDA INTEGRATION READY ===")
