---
name: cyber-threat-monitor
description: Real-time cyber threat intelligence monitoring
category: security
---

# Cyber Threat Monitor

Real-time cyber threat intelligence feeds.

## Data Sources

### Threat Maps
- Kaspersky Cybermap
- Check Point Threatmap
- Radware Live Threat Map
- NetScout Horizon

### Feeds
- AlienVault OTX
- Abuse.ch
- VirusTotal
- Shodan alerts

### Integration

```bash
# Fetch threat data
curl https://cybermap.kaspersky.com/api/threats
curl https://otx.alienvault.com/api/v1/indicators
