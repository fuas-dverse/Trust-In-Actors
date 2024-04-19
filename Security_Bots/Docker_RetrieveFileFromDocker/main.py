import docker

# Define container and file names
container_name = "sonarqube_2223nj_cb01"
file_name = "access.2023-01-11.log"

# Initialize Docker client
client = docker.from_env()

# Get the container by name
container = client.containers.get(container_name)

# Get the file content from the container
file_content = container.exec_run(f"cat /opt/sonarqube/logs/{file_name}").output.decode("utf-8")

# Save the file content locally
output_file_name = f"{container_name}_{file_name}"
with open(output_file_name, "w") as f:
    f.write(file_content)

# Print a success message
print(f"{file_name} from {container_name} was successfully saved as {output_file_name}")
