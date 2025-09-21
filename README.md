# Weather Data ETL Pipeline Project
Automated data pipeline that extracts, transforms, and loads weather data into a PostgreSQL database using Airflow and dbt, and Superset displays the final output

## Project Overview
This project automates the collection and processing of weather data. 
It fetches raw weather data from Weatherstack API, processes it using Python scripts, and runs transformations with dbt before loading it into PostgreSQL for analytics. 
The pipeline is scheduled and managed with Apache Airflow and containerized using Docker, and displayed the final output through Superset.

### Dashboard Preview
Here is an example Superset dashboard showing the processed weather metrics:

![Dashboard Example](images/superset1.png)

---

## Key Features
- Scheduled ETL pipeline using Airflow (PythonOperator & DockerOperator)
- Data transformation and modeling with dbt
- Automated daily aggregation of weather metrics
- Containerized using Docker and Docker Compose
- Displayed the final output using Superset

### Example Charts
(images/superset2.png)
(images/superset3.png)
(images/superset4.png)

---

## Technologies & Skills
- Python, SQL (PostgreSQL)
- Apache Airflow (DAGs, Operators, scheduling)
- Docker & Docker Compose
- dbt (data modeling & transformations)
- Apache Superset (visualization)

---

## How to Use the Project

### Prerequisites
... (your existing text)

---

## Step 3: Access the Superset
- **user:** admin  
- **password:** admin  

Open you browser and go to:  

```bash
http://127.0.0.1:8088
