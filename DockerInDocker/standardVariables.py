import docker
from confluent_kafka import Producer,Consumer

# Initialize Docker client
client = docker.from_env()

# Initialize Kafka producer
producer = Producer({'bootstrap.servers':'localhost:9092'})

def delivery_callback(err, msg):
        if err:
            print('ERROR: Message failed delivery: {}'.format(err))
        else:
            print("Produced event to topic {topic}: value = {value:12}".format(
                topic=msg.topic(), value=msg.value().decode('utf-8')))

consumer= Consumer({'bootstrap.servers': 'localhost:9092',
                     'group.id':'my-group',
                     })

def send_response(json_message):
    producer.produce('DiD_response', json_message,callback=delivery_callback)

    # Ensure all messages have been sent
    producer.poll(10000)
    producer.flush()
