FROM docker:24

# Install Python and pip
RUN apk add --no-cache python3 py3-pip

# Create a virtual environment
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Install the docker package
RUN pip3 install docker

# Set the working directory
WORKDIR /app

# Add the requirements for the Python script
COPY requirements.txt .

# Install Python dependencies from requirements.txt
RUN pip3 install -r requirements.txt

# Add necessary files
COPY filekey.key .
COPY myscript.py .

# Set the default command to run the Python script
CMD ["python3", "/app/myscript.py"]