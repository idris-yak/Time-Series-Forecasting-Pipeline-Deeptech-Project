# Time-Series-Forecasting-Data Pipeline
## 1. Project Overview

### Title: Time Series Forecasting Pipeline
**Objective:**
Design and implement an automated pipeline that:

- Ingests time-series data
- Cleans and transforms it
- Applies forecasting using Prophet
- Stores predictions in a data warehouse (BigQuery or S3 + Athena)
- Makes outputs available for BI tools (e.g., Power BI, Tableau)

## 2. Architecture
        ┌──────────────┐
        │ Data Source  │ (CSV / API / DB)
        └──────┬───────┘
               │
        ┌──────▼───────┐
        │ Data Ingest  │ (Python + Pandas)
        └──────┬───────┘
               │
        ┌──────▼───────┐
        │ Data Storage │ (S3 Bucket)
        └──────┬───────┘
               │
        ┌──────▼───────┐
        │ Data Cleaning│
        └──────┬───────┘
               │
        ┌──────▼───────┐
        │ Forecasting  │ (Prophet)
        └──────┬───────┘
               │
        ┌──────▼────────────┐
        │ Store Predictions │ (S3)
        └──────┬────────────┘
               │
        ┌──────▼───────┐
        │ BI Dashboard │
        └──────────────┘


## 3. Tech Stack
| Layer           | Tool                   |
| --------------- | ---------------------- |
| Data Processing | Python (Pandas, NumPy) |
| Forecasting     | Prophet                |
| Storage         | BigQuery / AWS S3      |
| Query Layer     | SQL                    |
| Orchestration   | Airflow (optional)     |
| Visualization   | Power BI / Tableau     |

## 4. Dataset
Dataset used: Time Series Forecasting in Yahoo Stock Price
 
Link 🔗: 


Also you can use any time-series dataset such as:
- Sales data
- Website traffic
- Stock prices
- Weather data
