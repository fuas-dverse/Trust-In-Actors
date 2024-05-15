import json
from standardVariables import client,consumer, send_response

def format_message(message):
    json_msg = json.loads(message)
    command = json_msg["Action"]
    container =client.containers.get(json_msg["Container"])
    return container, command


def proccess_run_container(container,action):
    message = ""

    if(action.lower()=="start"):
        if(container.status=="paused"):
            container.unpause()
        container.start()
        message = "Container started"
    elif(action.lower()=="pause"):
        container.pause()
        message = "Container paused"
    elif(action.lower()=="stop"):
        container.stop()
        message = "Container stopped"
    else:
        print("This action is not supported")

    return message


# Kafka consume mechanism
consumer.subscribe(["DiD_running"])

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
            
            container_id,command= format_message(msg.value().decode('utf-8'))
            json_message = json.dumps(proccess_run_container(container_id,command))
            send_response(json_message)
            
            

except KeyboardInterrupt:
    pass
finally:
    # Leave group and commit final offsets
    consumer.close()
