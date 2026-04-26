from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'orders',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='order-group'
)

print("Consumer started... Waiting for messages")

for message in consumer:
    data = message.value

    if data["amount"] > 1000:
        print(f"HIGH VALUE ORDER: {data}")
    else:
        print(f"Order processed: {data}")
