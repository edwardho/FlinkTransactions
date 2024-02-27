# Apache Flink Transaction Analytics with Elasticsearch and Postgres

This repository contains an Apache Flink application for real-time transaction analytics built using Docker Compose to orchestrate the infrastructure components Apache Flink, Postgres, Elastisearch, and Kibana. The application processes financial transaction data from Kafka using Kafka KRaft, performs aggregations, and stores the results in both Postgres and Elasticsearch for further analysis.

## Requirements
- Docker
- Apache Kafka
- Apache Flink
- PostgreSQL
- Elastisearch
- Kibana

## System Design
![System Design.png](System%20Design.png)

## Installation, Setup, and Usage
1. Clone this repository.
2. Navigate to ~/TransactionsGenerator
3. If the following components are not installed execute:
- `pip install faker`
- `pip install confluent_kafka`
- `pip install simplejson`
4. Run `docker compose up -d` to start the required services (Apache Flink, Postgres, Elastisearch, and Kibana).
5. Run the Sales Transaction Generator `main.py` in order to generate the sales transactions into Kafka.
6. Navigate into the Kafka KRaft container `docker exec -it kafka-kraft /bin/bash`
7. Send all the transactions generated from main.py to the Kafka consumer and process the transaction data `kafka-console-consumer --topic financialTransactions --bootstrap-server kafka-kraft:29092 --from-beginning`
8. Navigate to the location of your Flink folder
9. Start your flink cluster `./bin/start-cluster.sh `
10. Navigate back to ~/FlinkTransactions
11. Compile your maven packages using:
- mvn clean
- mvn compile
- mvn package
12. Run the DataStreamJob using `[FLINK FOLDER LOCATION]/bin/flink run -c FlinkTransactions.DataStreamJob target/FlinkTransactions-1.0-SNAPSHOT.jar`

## Application Details
The `DataStreamJob` class within the `FlinkTransactions` package serves as the main entry point for the Flink application. The application consumes financial transaction data from Kafka, performs transformations, and stores aggregated results in both Postgres and Elasticsearch.

### Components
#### Apache Flink
- Sets up the Flink execution environment.
- Connects to Kafka as a source for financial transaction data.
- Processes, transforms, and performs aggregations on transaction data streams.

#### Postgres
- Stores transaction data and aggregated results in tables (`transactions`, `sales_per_category`, `sales_per_day`, `sales_per_month`).

#### Elasticsearch
- Stores transaction data for further analysis.

#### Kibana
- Visualizes transaction data from Elastisearch.

## Code Structure
- `DataStreamJob.java`: Contains the Flink application logic, including Kafka source setup, stream processing, transformations, and sinks for Postgres and Elasticsearch.
- `Deserializer`, `Dto`, and `utils` packages: Include necessary classes and utilities for deserialization, data transfer objects, and JSON conversion.

## Configuration
- Kafka settings are defined within the Kafka docker source setup using KRaft.
- Postgres connection details (username, password, database) are defined within the Postgres docker source setup under `POSTGRES_USER`, `POSTGRES_PASSWORD`, and `POSTGRES_DB`

## Sink Operations
- The application includes sink operations for Postgres using JDBC to create tables (`transactions`, `sales_per_category`, `sales_per_day`, `sales_per_month`) and perform insert/update operations.
- Additionally, it includes an Elasticsearch sink to index transaction data for further analysis.
