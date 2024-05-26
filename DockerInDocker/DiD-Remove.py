import json
from standardVariables import client, producer,  consumer, send_response

def format_message(message):
    command = ""
    container =client.containers.get(message["Container"])
    return container, command


def remove_container(container_id):
    container = client.containers.get(container_id)
    response = container.remove()
    return response


# Kafka consume mechanism
consumer.subscribe(["docker_remove"])

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            # Initial message consumption may take up to
            # `session.timeout.ms` for the consumer group to
            # rebalance and start consuming
            print("Waiting...")
        elif msg.error():
            print("ERROR: %s".format(msg.error()))
        else:
            # Extract the (optional) key and value, and print.

            print("Consumed event from topic {topic}: value = {value:12}".format(
                topic=msg.topic(), value=msg.value().decode('utf-8')))
            
            container_id,command= format_message(msg.value)
            json_message = json.dumps(remove_container(container_id))
            send_response(json_message)
            
            

except KeyboardInterrupt:
    pass
finally:
    # Leave group and commit final offsets
    consumer.close()
