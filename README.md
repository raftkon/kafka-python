# Kafka - Python

Scripts for Consumer and Producer connecting to a Kafka Broker.
The project implements both configurations for connecting to a Kafka Broker
with PLAINTEXT and SSL communication.

For windows:

- create venv (if exists skip this step):

```bash
python -m venv venv
```

- activate venv:

```bash
source env/Scripts/activate
```

- deactivate venv:

```bash
deactivate
```

- install dependencies:

```bash
pip install -r requirements.txt
```

## PLAINTEXT

### Producer

To run the producer:

```bash
python producer.py
```

Specify:

- `TOPIC`: topic you want to produce
- `BROKER`: kafka broker you want to connect
- `KEY`: key for the messages
- `message`: message in JSON format

If you want to send just bytestream comment out `value_serializer` and change the message to be `b'message-you-want-to-send'`

### Consumer

To run the consumer:

```bash
python consumer.py
```

Specify:

- `TOPIC`: topic you want to produce
- `BROKER`: kafka broker you want to connect

If you want to receive just bytestream as messages comment out `value_deserializer`.

## SSL

Both Producer & Consumer have the same specifications, the only difference is the SSL certificates you have to provide to establish TLS communication.

Create an ssl context and provide the truststore.pem and keystore.pem for the certificate and the key for the client authentication on the Kafka Broker.

The path files are relative to where you run the python command.

### Producer

To run the producer:

```bash
python ssl/producer.py
```

### Consumer

To run the consumer:

```bash
python ssl/consumer.py
```
