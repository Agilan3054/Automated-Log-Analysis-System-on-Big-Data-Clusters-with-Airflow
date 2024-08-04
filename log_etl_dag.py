from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import os

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'log_etl',
    default_args=default_args,
    description='Log ETL DAG',
    schedule_interval=timedelta(days=1),
)

def run_etl():
    os.system("spark-submit /usr/local/airflow/dags/etl.py")

run_etl_task = PythonOperator(
    task_id='run_etl',
    python_callable=run_etl,
    dag=dag,
)

run_etl_task
