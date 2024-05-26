import json
import docker
from confluent_kafka import Producer

# Initialize Docker client
client = docker.from_env()

# Initialize Kafka producer
producer = Producer({'bootstrap.servers':'localhost:9092'})

def delivery_callback(err, msg):
        if err:
            print('ERROR: Message failed delivery: {}'.format(err))
        else:
            print("Produced event to topic {topic}: key = {key:12} value = {value:12}".format(
                topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))


# while True:
    # Iterate over all running containers
for container in client.containers.list():
    print("Start list")
    # Fetch the logs of the container
    logs = container.logs()
    print("fetched log")

    # Prepare the message to be sent to Kafka
    message = {
        'container_id': container.id,
        'logs': logs.decode('utf-8')  # decode from bytes to string
    }

    # print("Message: ",message)
    json_message =json.dumps(message)

    # Send the message to Kafka
    producer.produce('docker_logs', json_message,callback=delivery_callback)
    print("send log")

# Ensure all messages have been sent
producer.poll(10000)
producer.flush()
print("End loop")
