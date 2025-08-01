import requests
import json
from datetime import datetime
import boto3

# 1. Coletar dados da API
url = "https://api.coingecko.com/api/v3/simple/price"
params = {
    "ids": "bitcoin,ethereum",
    "vs_currencies": "usd",
    "include_market_cap": "true",
    "include_24hr_vol": "true",
    "include_24hr_change": "true"
}
response = requests.get(url, params=params)
data = response.json()

# 2. Adicionar timestamp e preparar os registros
now = datetime.utcnow().isoformat()
records = []
for coin, info in data.items():
    record = {
        "timestamp": now,
        "coin": coin,
        "price_usd": info["usd"],
        "market_cap": info.get("usd_market_cap"),
        "volume_24h": info.get("usd_24h_vol"),
        "change_24h_pct": info.get("usd_24h_change")
    }
    records.append(record)

# 3. Enviar os registros para o Firehose
firehose = boto3.client('firehose')
delivery_stream_name = "crypto-firehose"

for record in records:
    response = firehose.put_record(
        DeliveryStreamName=delivery_stream_name,
        Record={
            "Data": json.dumps(record) + "\n"
        }
    )
    print(f"Enviado: {record['coin']} - status: {response['ResponseMetadata']['HTTPStatusCode']}")
