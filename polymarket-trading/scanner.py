#!/usr/bin/env python3
"""TachyonBeing Polymarket Scanner - Find high-conviction opportunities"""

import json
import requests
from datetime import datetime

def scan_polymarket():
    """Scan Polymarket for active trading opportunities"""
    url = "https://gamma-api.polymarket.com/events?limit=100&active=true"
    
    try:
        response = requests.get(url, timeout=10)
        events = response.json()
        
        opportunities = []
        for event in events[:20]:
            if event.get('volume', 0) > 10000:  # High volume filter
                opportunities.append({
                    'title': event['title'][:70],
                    'volume': event.get('volume', 0),
                    'date': event.get('date', 'N/A'),
                    'clob_url': event.get('clob_url', '')
                })
        
        return opportunities
    except Exception as e:
        print(f"Error scanning Polymarket: {e}")
        return []

def analyze_opportunities():
    """Analyze opportunities for trading edge"""
    opportunities = scan_polymarket()
    
    print(f"Found {len(opportunities)} high-volume opportunities")
    for opp in opportunities[:10]:
        print(f"- {opp['title']}")
        print(f"  Volume: ${opp['volume']:,.2f}")
        print()

if __name__ == "__main__":
    analyze_opportunities()
