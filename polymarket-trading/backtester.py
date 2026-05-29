#!/usr/bin/env python3
"""TachyonBeing Backtesting Framework"""

import pandas as pd
import numpy as np

class Backtester:
    def __init__(self, initial_capital=1000):
        self.initial_capital = initial_capital
        self.capital = initial_capital
        self.trades = []
        
    def test_strategy(self, prices, strategy="momentum"):
        """Test a trading strategy against historical prices"""
        for i in range(1, len(prices)):
            if strategy == "momentum":
                # Simple momentum strategy
                if prices[i] > prices[i-1] * 1.01:  # 1% gain
                    self.buy(prices[i])
                elif prices[i] < prices[i-1] * 0.99:  # 1% loss
                    self.sell(prices[i])
            elif strategy == "mean_reversion":
                # Mean reversion strategy
                ma = np.mean(prices[max(0,i-20):i])
                if prices[i] < ma * 0.98:  # Below mean
                    self.buy(prices[i])
                elif prices[i] > ma * 1.02:  # Above mean
                    self.sell(prices[i])
                    
    def buy(self, price):
        """Execute buy order"""
        self.trades.append({"action": "BUY", "price": price})
        
    def sell(self, price):
        """Execute sell order"""
        self.trades.append({"action": "SELL", "price": price})
        
    def get_results(self):
        """Get backtest results"""
        wins = sum(1 for t in self.trades if t["action"] == "SELL")
        win_rate = wins / len(self.trades) if self.trades else 0
        return {
            "initial_capital": self.initial_capital,
            "trades": len(self.trades),
            "win_rate": win_rate,
            "final_capital": self.capital
        }

# Test
if __name__ == "__main__":
    bt = Backtester()
    # Generate sample price data
    prices = [100 + np.random.normal(0, 1) for _ in range(100)]
    bt.test_strategy(prices, "momentum")
    print(bt.get_results())
