import json
import time
from standardVariables import client, producer, delivery_callback

while True:
    for container in client.containers.list(all=True):
        message = {
            'container_id': container.id,
            'container_image': str(container.image),
            'container_name':container.name,
            'container_status':container.status,
            }
        # print(message)
        json_message =json.dumps(message)
        producer.produce('DiD_containers', json_message,callback=delivery_callback)

    # Ensure all messages have been sent
    producer.poll(10000)
    producer.flush()
    
    print("sleep")
    time.sleep(30)
    print("awake")