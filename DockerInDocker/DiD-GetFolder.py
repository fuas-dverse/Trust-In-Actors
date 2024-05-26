import json
from standardVariables import client, consumer, send_response
# Specify the path where you want to save the tarball
output_path = "./save/tarball.tar"

def format_message(message):    
    json_msg = json.loads(message)
    print("Msg: ",json_msg)
    command = json_msg["DownloadWhat"]
    container =client.containers.get(json_msg["Container"])
    return container, command


def get_tarball(container, input_command):
    tarball = None
    if(input_command.upper() == "ALL"):
        tarball = container.export()
    # Save the tarball to disk
        # with open(output_path, "wb") as f:
        #     for chunk in tarball:
        #         f.write(chunk)

    elif(input_command.upper() != "ALL"):
        tarball = container.get_archive(input_command)
        tarball = tarball[0]
    # Save the tarball to disk
        # with open(output_path, "wb") as f:
        #         print(file_content)
        #         for chunk in file_content:
        #             f.write(chunk)
    return tarball


# Kafka consume mechanism
consumer.subscribe(["DiD_download"])

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
            json_message = (get_tarball(container_id,command))
            json_bytes = b"".join(json_message)
            print("Size: ",json_bytes)
            send_response(json_bytes)
            
            

except KeyboardInterrupt:
    pass
finally:
    # Leave group and commit final offsets
    consumer.close()

