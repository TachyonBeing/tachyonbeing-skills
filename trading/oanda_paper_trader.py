#!/usr/bin/env python3
"""
TachyonBeing OANDA Paper Trader
Paper trading with real market data
"""
import json
import time
from datetime import datetime
import urllib.request

class OANDA_PaperTrader:
    def __init__(self, api_key, account_id):
        self.api_key = api_key
        self.account_id = account_id
        self.base_url = "https://api-fxtrade.oanda.com/v3"
        self.virtual_balance = 1000.0  # $1000 virtual capital
        self.trades = []
        self.trade_log = []
    
    def _request(self, method, path, data=None):
        url = f"{self.base_url}{path}"
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        if data:
            data = json.dumps(data).encode()
        req = urllib.request.Request(url, data=data, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req) as resp:
                return json.loads(resp.read())
        except Exception as e:
            return {"error": str(e)}
    
    def get_candles(self, instrument, count=100, granularity="H1"):
        return self._request("GET", f"/instruments/{instrument}/candles?count={count}&granularity={granularity}")
    
    def calculate_rsi(self, closes, period=14):
        if len(closes) < period + 1:
            return 50
        deltas = [closes[i] - closes[i-1] for i in range(1, len(closes))]
        gains = [d if d > 0 else 0 for d in deltas]
        losses = [-d if d < 0 else 0 for d in deltas]
        avg_gain = sum(gains[-period:]) / period
        avg_loss = sum(losses[-period:]) / period
        if avg_loss == 0:
            return 100
        rs = avg_gain / avg_loss
        return 100 - (100 / (1 + rs))
    
    def calculate_sma(self, closes, period=20):
        if len(closes) < period:
            return None
        return sum(closes[-period:]) / period
    
    def scan_opportunities(self, instruments=["EUR_USD", "GBP_USD", "USD_JPY", "AUD_USD", "USD_CAD", "USD_CHF", "NZD_USD"]):
        opportunities = []
        for inst in instruments:
            data = self.get_candles(inst, count=100, granularity="H1")
            if "candles" not in data:
                continue
            
            candles = data["candles"]
            closes = [float(c["mid"]["c"]) for c in candles]
            
            rsi = self.calculate_rsi(closes)
            sma20 = self.calculate_sma(closes, 20)
            current = closes[-1]
            
            signal = None
            confidence = 0
            
            # RSI oversold bounce (Bjorn's preferred strategy)
            if rsi < 30:
                signal = "BUY"
                confidence = min(90, (30 - rsi) * 3)
            elif rsi > 70:
                signal = "SELL"
                confidence = min(90, (rsi - 70) * 3)
            
            # Price vs SMA crossover
            if sma20:
                if current > sma20 and rsi < 40:
                    signal = "BUY"
                    confidence = max(confidence, 60)
                elif current < sma20 and rsi > 60:
                    signal = "SELL"
                    confidence = max(confidence, 60)
            
            if signal:
                opportunities.append({
                    "instrument": inst,
                    "signal": signal,
                    "confidence": round(confidence, 1),
                    "rsi": round(rsi, 1),
                    "current_price": round(current, 5),
                    "sma20": round(sma20, 5) if sma20 else None,
                    "timestamp": datetime.utcnow().isoformat()
                })
        
        return opportunities
    
    def simulate_trade(self, instrument, direction, units=1000):
        data = self.get_candles(instrument, count=10, granularity="H1")
        if "candles" not in data:
            return None
        
        candles = data["candles"]
        current_price = float(candles[-1]["mid"]["c"])
        
        trade = {
            "instrument": instrument,
            "direction": direction,
            "units": units,
            "entry_price": current_price,
            "timestamp": datetime.utcnow().isoformat(),
            "status": "OPEN"
        }
        
        self.trades.append(trade)
        self.trade_log.append({
            "action": f"PAPER {direction}",
            "instrument": instrument,
            "price": current_price,
            "time": trade["timestamp"]
        })
        
        return trade
    
    def get_status(self):
        return {
            "virtual_balance": round(self.virtual_balance, 2),
            "open_trades": len(self.trades),
            "total_trades": len(self.trade_log),
            "timestamp": datetime.utcnow().isoformat()
        }

# Run paper trader scan
api_key = "36a991ea82cd3312d22848e1690e3435-41ab59875eb940035da25f4dd86398b0"
account_id = "001-001-21553572-001"

trader = OANDA_PaperTrader(api_key, account_id)

print("=== OANDA PAPER TRADER ===")
print(f"Virtual Balance: ${trader.virtual_balance}")
print(f"Account: {account_id}")
print()

print("=== SCANNING FOR OPPORTUNITIES ===")
opportunities = trader.scan_opportunities()

if opportunities:
    print(f"Found {len(opportunities)} opportunities:")
    for opp in opportunities:
        print(f"  {opp['instrument']}: {opp['signal']} (confidence: {opp['confidence']}%, RSI: {opp['rsi']}, Price: {opp['current_price']})")
else:
    print("No high-conviction opportunities found")

print()
print("=== PAPER TRADER STATUS ===")
status = trader.get_status()
print(json.dumps(status, indent=2))
print()
print("=== OANDA PAPER TRADING READY ===")
