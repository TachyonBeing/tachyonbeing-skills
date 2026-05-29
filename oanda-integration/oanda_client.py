#!/usr/bin/env python3
"""OANDA Integration Framework for TachyonBeing"""

import os
import json
import requests
from datetime import datetime

class OANDAIntegration:
    def __init__(self):
        self.api_key = "730ab777f39643eab6637e7eae606c7e-b5b5e040f84f042bd28223531b7308dd"
        self.account_id = "21553572001"
        self.base_url = "https://api-fxtrade.oanda.com/v3"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def test_connection(self):
        """Test API connection"""
        try:
            response = requests.get(
                f"{self.base_url}/accounts/{self.account_id}/summary",
                headers=self.headers
            )
            return response.status_code, response.json()
        except Exception as e:
            return 500, {"error": str(e)}
    
    def get_account_summary(self):
        """Get account summary"""
        response = requests.get(
            f"{self.base_url}/accounts/{self.account_id}/summary",
            headers=self.headers
        )
        return response.json()
    
    def get_positions(self):
        """Get current positions"""
        response = requests.get(
            f"{self.base_url}/accounts/{self.account_id}/positions",
            headers=self.headers
        )
        return response.json()
    
    def get_pricing(self, instruments=["EUR_USD", "GBP_USD", "USD_JPY"]):
        """Get pricing for instruments"""
        params = {"instruments": ",".join(instruments)}
        response = requests.get(
            f"{self.base_url}/pricing",
            headers=self.headers,
            params=params
        )
        return response.json()
    
    def place_order(self, instrument, units, type="MARKET"):
        """Place a trade order"""
        order = {
            "instrument": instrument,
            "units": str(units),
            "type": type
        }
        response = requests.post(
            f"{self.base_url}/accounts/{self.account_id}/orders",
            headers=self.headers,
            json=order
        )
        return response.json()

if __name__ == "__main__":
    oanda = OANDAIntegration()
    print("Testing OANDA connection...")
    status, result = oanda.test_connection()
    print(f"Status: {status}")
    print(f"Result: {json.dumps(result, indent=2)}")
