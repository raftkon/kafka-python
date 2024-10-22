from kafka import KafkaProducer
import json
import ssl

context = ssl.create_default_context()

context.load_cert_chain(certfile="certs/symbiotik/kafka-truststore.pem",keyfile="certs/symbiotik/kafka-keystore.pem")

TOPIC = "my-topic"
BROKER = "symbiotik.aegisresearch.eu:9093"
KEY = b"python-producer"

producer = KafkaProducer(
    bootstrap_servers=[BROKER],  # Adjust to your broker's SSL port
    security_protocol='SSL',
    ssl_context=context,
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    acks='all'
)

# Send messages securely
for i in range(10):
    message = {'number': i}
    future = producer.send(TOPIC, value=message,key=KEY)
    result = future.get(timeout=10)  # Wait for confirmation of message delivery

producer.flush()  # Ensure all messages are sent
producer.close()  # Close the producer when done

print("SSL Messages sent successfully.")