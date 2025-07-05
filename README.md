Binance Crypto Portfolio Simulator with Monte Carlo Simulation

This project simulates potential future portfolio outcomes using Monte Carlo simulations on historical crypto price data from the Binance API. It follows a modular data engineering approach, including ingestion, transformation, and analysis pipelines, with data storage in AWS S3 (bronze/silver layers) and processing in Python.

Binance API → Ingestion Script → Bronze Layer (raw OHLCV Parquet in S3)
                               ↓
                      Processing Script → Silver Layer (clean log returns in S3)
                               ↓
                  Monte Carlo Simulation → Risk metrics & Portfolio outcomes
                               ↓
                     Visualization (Matplotlib / Streamlit)

Tech Stack

| Layer              | Tools Used                                            |
| ------------------ | ----------------------------------------------------- |
| **Ingestion**      | Python, Binance REST API, `requests`, `pandas`        |
| **Storage**        | AWS S3, Parquet (`pyarrow`, `s3fs`)                   |
| **Processing**     | `pandas`, `numpy`                                     |
| **Simulation**     | Monte Carlo using Geometric Brownian Motion (`numpy`) |
| **Visualization**  | Matplotlib / Streamlit                                |
| **Infrastructure** | Local dev, scalable to Airflow/Spark (optional)       |


Project Features

✅ Pull historical OHLCV (candlestick) data for selected crypto symbols.

✅ Store raw data in S3 Bronze Layer as Parquet.

✅ Process and clean data: calculate log returns, remove gaps, and sort timestamps.

✅ Save cleaned data to S3 Silver Layer.

✅ Simulate future price paths using Geometric Brownian Motion.

✅ Visualize portfolio paths, histograms of outcomes, and Value-at-Risk (VaR).


Future Work

Add Airflow DAG for scheduled ingestion & simulation

Deploy visualization as a public Streamlit app

Extend to equities using Alpha Vantage or Yahoo Finance API

Integrate backtesting framework (Backtrader)

