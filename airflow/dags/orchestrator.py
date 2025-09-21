from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount
import sys

sys.path.append('/opt/airflow/api_request')

def safe_callable_main():
    from insert_records import main
    return main()

default_args = {
    'description': 'A Dag for weather data',
    'start_date': datetime(2025, 9, 19),
    'catchup': False
}

dag = DAG(
    dag_id='Weather-Dag',
    default_args=default_args,
    schedule=timedelta(minutes=5)
)

with dag:
    task1 = PythonOperator(
        task_id='weather-data-task1',
        python_callable=safe_callable_main
    )

    task2 = DockerOperator(
        task_id='weather-data-task2-dbt',
        image='ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
        command='run --select stg_weather_data  hourly_average hourly_hottest_strongest daily_average daily_hottest_temperature_strongest_wind_speed monthly_average yearly_average yearly_hottest_temperature yearly_strongest_wind_speed',
        working_dir='/usr/app',
        mounts=[
            Mount(
                source="/home/reijin051824/repos/weather_data_project/dbt/my_project",   
                target="/usr/app",
                type="bind"
            ),
            Mount(
                source="/home/reijin051824/repos/weather_data_project/dbt/profiles.yml", 
                target="/root/.dbt/profiles.yml",
                type="bind"
            )
        ],
        network_mode="weather_data_project_my-network",
        docker_url="unix://var/run/docker.sock",
        auto_remove='success'
    )

    task1 >> task2
