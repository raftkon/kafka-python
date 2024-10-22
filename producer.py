from kafka import KafkaProducer
import json

TOPIC = "my-topic"
BROKER = "symbiotik.aegisresearch.eu:9093"
KEY = b"python-producer"

producer = KafkaProducer(
    bootstrap_servers=[BROKER],  # Adjust to your broker address
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),  # Serialize JSON data
    acks="all"
)

# Send messages
for i in range(10):
    message = {'number': i}
    producer.send(TOPIC, value=message)  # Replace 'my_topic' with your topic name



producer.flush()  # Ensure all messages are sent
producer.close()  # Close the producer when done

print("Messages sent successfully.")

