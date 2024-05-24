import json
from MockVar import mock_client

# As Python is weird with imports I need to do it via this. I just copy the identical functions to this script

## DiD-Command
def format_message_command(message):
    json_msg = json.loads(message)
    command = json_msg["Command"]
    container =mock_client.containers.get(json_msg["Container"])
    return container, command


def proccess_command_container(container,action):
    _,stream = container.exec_run(action,privileged=True)    
    print("Stream: ",stream)
    return stream.decode('utf-8')

## DiD-GetFolder.py
output_path= "./save/tarball.tar"

def format_message_folder(message):    
    json_msg = json.loads(message)
    print("Msg: ",json_msg)
    command = json_msg["DownloadWhat"]
    container =mock_client.containers.get(json_msg["Container"])
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
        #         print(tarball)
        #         for chunk in tarball:
        #             f.write(chunk)
    return tarball

## DiD-GetLogs.py
def format_message_logs(message):
    json_msg = json.loads(message)
    command = ""
    container =mock_client.containers.get(json_msg["Container"])
    return container, command


def get_container_logs(container):
    logs = container.logs()

    message = {
            'container_id': container.id,
            'logs': logs.decode('utf-8')  # decode from bytes to string
        }
    return message

## DiD-Remove.py
def format_message_remove(message):
    command = ""
    container =mock_client.containers.get(message["Container"])
    return container, command


def remove_container(container_id):
    container = mock_client.containers.get(container_id)
    response = container.remove()
    return response



## DiD-Running.py
def format_message_running(message):
    json_msg = json.loads(message)
    command = json_msg["Action"]
    container =mock_client.containers.get(json_msg["Container"])
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
        message ="This action is not supported"

    return message
