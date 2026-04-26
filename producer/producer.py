import random
import time
from datetime import datetime
from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

products = ["laptop", "phone", "tablet"]
cities = ["Dallas", "Austin", "Houston"]

while True:
    order = {
        "order_id": random.randint(1000, 9999),
        "user_id": random.randint(1, 100),
        "product": random.choice(products),
        "amount": random.randint(100, 2000),
        "city": random.choice(cities),
        "timestamp": datetime.now().isoformat()
    }
    producer.send('orders', value=order)
    print(f"Sent: {order}")
    time.sleep(2)
