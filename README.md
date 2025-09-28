# Weather Data ELT Pipeline Project
Automated data pipeline that extracts, transforms, and loads weather data into a PostgreSQL database using Airflow and dbt, and Superset displays the final output

## Video Link
- **Youtube**: [Watch on YT](https://youtu.be/tbXHcp_y7rY)
  
## Project Overview
The project automates the collection and processing of weather data from my home. It fetches raw weather data from Weatherstack API, processes it using Python scripts, and runs transformations with dbt before loading it into PostgreSQL for analytics. 
The pipeline is scheduled and managed with Apache Airflow and containerized using Docker, and displayed the final output through Superset.

### Dashboard Preview
Here is an example Superset dashboard showing the processed weather metrics:

![Dashboard Example](images/superset1.PNG)

---

## Key Features
- Scheduled elt pipeline using Airflow (PythonOperator & DockerOperator)
- Data transformation and modeling with dbt
- Automated hourly, daily, monthly and yearly aggregation of weather metrics
- Containerized using Docker and Docker Compose
- Displayed the final output using Superset

### My Dashboard Charts
![Dashboard](images/superset1.PNG)
![Dashboard](images/superset2.PNG)
![Dashboard](images/superset3.PNG)
![Dashboard](images/superset4.PNG)

---

## Technologies & Skills
- Python, SQL (PostgreSQL)
- Apache Airflow (DAGs, Operators, scheduling)
- Docker & Docker Compose
- dbt (data modeling & transformations)
- Apache Superset (visualization)

---
