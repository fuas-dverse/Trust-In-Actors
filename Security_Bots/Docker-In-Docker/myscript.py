import docker
import time
import os
from cryptography.fernet import Fernet
import base64

# Static Variable for easier access
line_encoding = 'utf-8'
separator = b'<<STOP>>' # I use stop as a word that is commonly used in ending message via Morse code

## For the Docker volume if the directory doesn't exist
os.makedirs('/app/logs', exist_ok=True)

# Getting encryption key
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()
 
# using the generated key
fernet = Fernet(key)


# Create a client connection to the Docker daemon
def create_docker_client():
    client: vars
    try:
        # Try connecting directly to the Docker daemon
        client = docker.DockerClient(base_url='unix://var/run/docker.sock')
    except Exception as exc:
        print("Trying with environment variables: ", exc)
        # If direct connection fails, use environment variables
        client = docker.from_env()
    return client

# Try to connect to docker
try:
    docker_client = create_docker_client()
    print("Connected to Docker successfully!")
except Exception as ex:
    print("Can't connect to Docker: ",ex)

# Create a dictionary to store the last tx_bytes for each container
last_tx_bytes = {}

def check_network_stats(stats):
    # Get the current tx_bytes
    current_tx_bytes = stats['networks']['eth0']['tx_bytes']

    # If we have recorded tx_bytes for this container before
    if container.short_id in last_tx_bytes:
        # Calculate the difference
        diff = current_tx_bytes - last_tx_bytes[container.short_id]

        # If the difference is more than 5000
        if diff > 100000:
            # Write a message to the log file
            normal_line = f'Time: {time.ctime()}, Container ID: {container.short_id}, transmit bytes increased by more than 0.1 mb in the last minute.'
            encoded_line = base64.b64encode(fernet.encrypt(normal_line.encode(line_encoding)))
            f.write(encoded_line)
            f.write(separator)
           
           

    # Update the last tx_bytes for this container
    last_tx_bytes[container.short_id] = current_tx_bytes

# Open the log file in append mode
with open('/app/logs/docker_logs.txt', 'ab') as f:
    while True:
        # Get a list of all containers
        print("Get containers")
        containers = docker_client.containers.list(all=True)

        for container in containers:
            # Get the current stats
            stats = container.stats(stream=False)

            # Write the container's id, name, status to the log file
            normal_line= f'Time: {time.ctime()}, Container ID: {container.short_id},Name: {container.name}, Status: {container.status}'
            encoded_line = base64.b64encode(fernet.encrypt(normal_line.encode(line_encoding)))
            f.write(encoded_line)
            f.write(separator)

            if 'networks' in stats:
                check_network_stats(stats)

            # Flush the file buffer to ensure that the logs are written to disk
            f.flush()

        # Wait for 60 seconds before the next iteration
        print("Container sleeping: ",time.ctime())
        time.sleep(60)
