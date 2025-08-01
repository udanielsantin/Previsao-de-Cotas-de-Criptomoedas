import requests
import json
from datetime import datetime

# Endpoint da CoinGecko
url = "https://api.coingecko.com/api/v3/simple/price"

# Parâmetros da consulta
params = {
    "ids": "bitcoin,ethereum",
    "vs_currencies": "usd",
    "include_market_cap": "true",
    "include_24hr_vol": "true",
    "include_24hr_change": "true"
}

# Requisição
response = requests.get(url, params=params)
data = response.json()

# Adiciona timestamp atual UTC
now = datetime.utcnow().isoformat()

# Transforma em lista de registros com timestamp
registros = []
for coin, info in data.items():
    registros.append({
        "timestamp": now,
        "coin": coin,
        "price_usd": info["usd"],
        "market_cap": info.get("usd_market_cap"),
        "volume_24h": info.get("usd_24h_vol"),
        "change_24h_pct": info.get("usd_24h_change")
    })

# Exibe os dados
print(json.dumps(registros, indent=2))
