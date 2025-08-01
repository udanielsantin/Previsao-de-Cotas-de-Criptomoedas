# Previsao-de-Cotas-de-Criptomoedas

[API de Cripto (CoinGecko/Binance)] 
          ↓
[FastAPI ou Lambda para coleta]
          ↓
[Amazon Kinesis Data Firehose]
          ↓
[Destino: S3 (Data Lake) ou Redshift / Elasticsearch]
          ↓
[Processamento com Athena, Glue ou Spark (ETL)]
          ↓
[ML Training: Sagemaker / Notebook Local / EC2]
          ↓
[Modelo Previsivo LSTM / Regressão]
          ↓
[Endpoint para inferência via API ou Dashboard Streamlit]
