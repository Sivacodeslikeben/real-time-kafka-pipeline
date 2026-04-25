# real-time-kafka-pipeline
E-commerce real-time order processing system
# Real-Time Order Streaming Pipeline

## 📌 Overview

This project demonstrates a real-time data pipeline using Kafka.

It simulates order events, streams them through Kafka, and processes them using a consumer application.

## 🧱 Architecture

Producer → Kafka → Consumer

## ⚙️ Tech Stack

* Kafka
* Python
* Docker

## 🚀 How to Run

1. Start Kafka

docker-compose up -d

2. Run producer

python producer/producer.py

3. Run consumer

python consumer/consumer.py


## 📊 Sample Output

Consumer receives real-time order events from Kafka.

## 💡 Key Concepts Demonstrated

* Event-driven architecture
* Kafka producer/consumer
* Real-time streaming

## 🔮 Future Improvements

* Add Spark Streaming
* Add Airflow orchestration
* Store in Data Warehouse
