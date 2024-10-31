# Kafka - Python

## Python version bug

_kafka-python_ has a compatibility issue with python version 3.12. The script certainly runs with **python v3.9**. The known [issue](https://github.com/dpkp/kafka-python/issues/2412).

### Install Python v3.9 and pip

To successfully install python3.9:
- (optionally) uninstall your current version of python, if any:
```bash
sudo apt-get remove python3.12
```
- install a PPA (standard method for installing python on Ubuntu):
```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
```
- install python3.9
```bash
sudo apt-get install python3.9
```
- verify python3.9 is successfully installed:
```bash
python3.9 --version
```
- install necessary tools for building Python and managing packages:
```bash
sudo apt-get update
sudo apt-get install python3.9-distutils python3.9-venv
```

- install pip using ensurepip:
```bash
python3.9 -m ensurepip --upgrade
```

- verify installation:
```bash
python3.9 -m pip --version
```

- create venv
```bash
python3.9 -m venv myenv
```

- install dependencies:
```bash
pip install -r requirements.txt
```

and the scripts should run correctly.

## Usage
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
