---
name: cyber-threat-monitor
description: Real-time cyber threat intelligence monitoring for risk assessment
version: 1.0.0
author: TachyonBeing
---

# Cyber Threat Monitor Skill

## Purpose
Monitor global cyber threats for risk assessment and market impact analysis.

## Threat Intelligence Feeds

### Real-Time Maps
- Kaspersky Cybermap: cybermap.kaspersky.com
- Check Point ThreatMap: threatmap.checkpoint.com
- Radware Live Threat Map: livethreatmap.radware.com
- Netscout Horizon: horizon.netscout.com

### Vulnerability Feeds
- AlienVault OTX: AlienVault Open Threat Exchange
- Abuse.ch: Malware and exploit tracking
- VirusTotal: File and URL analysis
- NVD: National Vulnerability Database

### Crypto Threats
- Chainalysis: Blockchain analytics
- Elliptic: Crypto crime detection
- TRM Labs: Sanctions screening

## Monitoring Pipeline

```
Threat Feed -> Pattern Detection -> Risk Scoring -> Alert Generation
```

## Risk Scoring

### Low Risk (1-3)
- Minor DDoS attacks
- Phishing campaigns
- Impact: No trading adjustment

### Medium Risk (4-6)
- Ransomware attacks
- Exchange breaches
- Impact: Reduce crypto positions 20%

### High Risk (7-10)
- Nation-state attacks
- Major exchange hacks
- Impact: Move to stablecoins, halt trading

## Implementation

### Feed Integration
```bash
# Kaspersky API
curl -s "https://cybermap.kaspersky.com/api/threats"

# AlienVault OTX
curl -s "https://otx.alienvault.com/api/v1/pulses/subscribed"
```

### Alert System
```python
if risk_score >= 7:
    send_alert("HIGH RISK: Reduce positions")
    execute_risk_reduction()
```

## Market Impact Analysis

### Crypto Markets
- Major exchange hack -> -15% BTC in 24h
- Regulatory action -> -10% sector
- Stablecoin depeg -> immediate sell

### Forex Markets
- Central bank cyber attack -> volatility spike
- SWIFT disruption -> currency pair swings

## Cron Integration
- Check feeds every 30 minutes
- Alert on risk score >= 7
- Auto-reduce positions on high risk
