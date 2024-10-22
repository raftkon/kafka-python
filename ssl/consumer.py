from kafka import KafkaConsumer
import json
import ssl
import os

# Generate 4 random bytes
random_bytes = os.urandom(4)
# Convert to hexadecimal string
GROUP_ID = random_bytes.hex()

context = ssl.create_default_context()

context.load_cert_chain(certfile="certs/symbiotik/kafka-truststore.pem",keyfile="certs/symbiotik/kafka-keystore.pem")

TOPIC = "my-topic"
BROKER = "symbiotik.aegisresearch.eu:9093"

consumer = KafkaConsumer(
    TOPIC,  # Replace with your topic name
    bootstrap_servers=[BROKER],  
    group_id=GROUP_ID,
    security_protocol='SSL',
    ssl_context=context,
    auto_offset_reset='earliest', # Read from the beginning if no offset is found
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)
# Consume messages securely
print("Listening for SSL messages...")
for message in consumer:
    print(f"Received message: {message.value}")

consumer.close()