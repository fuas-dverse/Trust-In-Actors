from cryptography.fernet import Fernet
import base64

# Getting encryption key
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()

# using the key
fernet = Fernet(key)

# Define a separator
separator = b'<<STOP>>'

# Suggested way of getting the docker_logs.txt is to download it from the volume itself
# An example of where you can find it using windows is \\wsl.localhost\docker-desktop-data\data\docker\volumes\security_bots_mylogs\_data
# opening the encrypted file
with open('docker_logs.txt', 'rb') as enc_file:
    content = enc_file.read()
    lines = content.split(separator)
    for line in lines:
        if line:  # Avoid trying to decrypt empty lines
            # Base64 decode the line before decrypting
            decrypted_line = fernet.decrypt(base64.b64decode(line))
            # Write the decrypted data
            with open('decrypted_docker_logs.txt', 'ab') as dec_file:
                dec_file.write(decrypted_line)
                dec_file.write('\n'.encode())