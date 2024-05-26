import os
import docker
from confluent_kafka import Producer,Consumer
from dotenv import load_dotenv

load_dotenv()

# Initialize Docker client
client = docker.from_env()

config = {
    'bootstrap.servers': os.environ.get("KAFKA_BOOTSTRAP_SERVER"),
    'security.protocol': os.environ.get("KAFKA_SECURITY_PROTOCOL"),
    'sasl.mechanisms': os.environ.get("KAFKA_SASL_MECHANISMS"),
    'sasl.username': os.environ.get("KAFKA_SASL_USERNAME"),
    'sasl.password': os.environ.get("KAFKA_SASL_PASSWORD"),
}

# Initialize Kafka producer
producer = Producer(config)

def delivery_callback(err, msg):
        if err:
            print('ERROR: Message failed delivery: {}'.format(err))
        else:
            print("Produced event to topic {topic}: value = {value:12}".format(
                topic=msg.topic(), value=msg.value().decode('utf-8')))


config['group.id'] = "group_id"
consumer= Consumer(config)

def send_response(json_message):
    producer.produce('DiD_response', json_message,callback=delivery_callback)

    # Ensure all messages have been sent
    producer.poll(10000)
    producer.flush()
