from confluent_kafka import Consumer
import json

# To consume latest messages and auto-commit offsets
consumer = Consumer({'bootstrap.servers': 'localhost:9092',
                     'group.id':'my-group',
                     })
consumer.subscribe(["docker_logs"])
# while True:
#     msg = consumer.poll(1)
#     print("msg: ",msg)
    
#     for message in consumer.poll(1):
#         print(f"Received message: {message.value}")
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
            
            

except KeyboardInterrupt:
    pass
finally:
    # Leave group and commit final offsets
    consumer.close()