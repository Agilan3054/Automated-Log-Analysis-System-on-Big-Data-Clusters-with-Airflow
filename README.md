# Automated Log Analysis System on Big Data Clusters with Airflow

This project involves the development of a large-scale log analysis system that integrates data ingestion, processing, and workflow management on a big data cluster. The system leverages Apache Spark for scalable data processing and Apache Airflow for automated workflow management, ensuring efficient handling of large volumes of log data.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Architecture](#architecture)
- [Setup](#setup)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)

## Introduction
The large-scale log analysis system aims to streamline the ingestion, processing, and management of log data using big data technologies. It provides an automated and scalable pipeline for extracting insights from log data, reducing manual intervention and improving data analysis efficiency.

## Features
- Integration of data ingestion, processing, and workflow management on a big data cluster.
- Scalable data processing using Apache Spark.
- Automated ETL workflows managed by Apache Airflow.
- Docker-based development environment for seamless deployment and scaling.
- Simulation and ingestion of log data, with extraction and storage of error logs in a scalable file system like HDFS.
- Fully automated and scalable log processing pipeline.

## Architecture
The system architecture includes the following components:
1. **Apache Spark**: For scalable data processing, including ETL operations.
2. **Apache Airflow**: For automating and managing complex ETL workflows using DAGs.
3. **Docker**: For creating a development environment and deploying Spark and Airflow services.
4. **HDFS**: For storing processed log data.

## Setup
### Prerequisites
- Docker and Docker Compose
- Apache Spark
- Apache Airflow
- HDFS (or any other scalable file system)

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/log-analysis-system.git
    cd log-analysis-system
    ```

2. Set up the Docker environment:
    ```sh
    docker-compose up -d
    ```

3. Configure Spark and Airflow settings in the `docker-compose.yml` file if necessary.

4. Initialize the Airflow database:
    ```sh
    docker-compose run airflow-webserver airflow db init
    ```

5. Create an Airflow user (optional but recommended):
    ```sh
    docker-compose run airflow-webserver airflow users create \
      --username admin \
      --firstname FIRST_NAME \
      --lastname LAST_NAME \
      --role Admin \
      --email admin@example.com
    ```

## Usage
1. Simulate and ingest log data:
    ```sh
    python simulate_log_data.py
    ```

2. Access the Airflow web UI to manage and monitor workflows:
    - Open your browser and go to `http://localhost:8080`
    - Log in with the credentials created during setup

3. Submit Spark jobs for ETL processing:
    ```sh
    spark-submit --master spark://spark-master:7077 etl_job.py
    ```

4. Monitor the processing pipeline and check results in HDFS:
    ```sh
    hdfs dfs -ls /path/to/output
    ```

## Technologies Used
- **Apache Spark**: For scalable data processing and ETL operations.
- **Apache Airflow**: For workflow automation and management.
- **Docker**: For containerization and seamless deployment.
- **HDFS**: For scalable file storage.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or new features.

