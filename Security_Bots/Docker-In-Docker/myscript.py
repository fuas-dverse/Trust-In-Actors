import docker
import time
import os
os.makedirs('/app/logs', exist_ok=True)

# Create a client connection to the Docker daemon
try:
    try:
        client = docker.DockerClient(base_url='unix://var/run/docker.sock')
    except:
        client = docker.from_env()
except Exception:
    print("Can't connect to docker")

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
        if diff > 5000:
            # Write a message to the log file
            f.write(f'Time: {time.ctime()}, Container ID: {container.short_id}, tx_bytes increased by more than 5000 in the last minute.\n')

    # Update the last tx_bytes for this container
    last_tx_bytes[container.short_id] = current_tx_bytes

# Open the log file in append mode
with open('/app/logs/docker_logs.txt', 'a') as f:
    while True:
        # Get a list of all containers
        print("Get containers")
        containers = client.containers.list(all=True)

        for container in containers:
            # Get the current stats
            stats = container.stats(stream=False)

            if 'networks' in stats:
                check_network_stats(stats)              

            # Write the container's id, status to the log file
            f.write(f'Time: {time.ctime()}, Container ID: {container.short_id}, Status: {container.status}\n')

        # Flush the file buffer to ensure that the logs are written to disk
        f.flush()

        # Wait for 60 seconds before the next iteration
        print("Container sleeping: ",time.ctime())
        time.sleep(60)
