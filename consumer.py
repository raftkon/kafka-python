from kafka import KafkaConsumer
import json
import os

# Generate 4 random bytes
random_bytes = os.urandom(4)
# Convert to hexadecimal string
GROUP_ID = random_bytes.hex()

TOPIC = "my-topic"
BROKER = "symbiotik.aegisresearch.eu:9093"


# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer("just_topic",group_id=GROUP_ID,
        bootstrap_servers=[BROKER],
        auto_offset_reset="earliest",  # Read from the beginning if no offset is found
        value_deserializer=lambda x: json.loads(x.decode('utf-8')))

print("Listening for messages...")
for message in consumer:
    print(f"Received message: {message.value}")



