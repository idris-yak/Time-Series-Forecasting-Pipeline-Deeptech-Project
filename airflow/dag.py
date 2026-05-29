from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess


def run_ingest():
    subprocess.run(["python", "scripts/ingest.py"], check=True)


def run_preprocess():
    subprocess.run(["python", "scripts/preprocess.py"], check=True)


def run_forecast():
    subprocess.run(["python", "scripts/forecast.py"], check=True)


def run_upload():
    subprocess.run(["python", "scripts/upload.py"], check=True)


with DAG(
    dag_id="time_series_forecasting_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    ingest_task = PythonOperator(
        task_id="ingest",
        python_callable=run_ingest
    )

    preprocess_task = PythonOperator(
        task_id="preprocess",
        python_callable=run_preprocess
    )

    forecast_task = PythonOperator(
        task_id="forecast",
        python_callable=run_forecast
    )

    upload_task = PythonOperator(
        task_id="upload",
        python_callable=run_upload
    )

    ingest_task >> preprocess_task >> forecast_task >> upload_task
