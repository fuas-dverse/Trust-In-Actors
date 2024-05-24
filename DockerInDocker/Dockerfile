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

# Copy the application files into the container
COPY DiD-SendContainers.py .
COPY standardVariables.py .
COPY requirements.txt .

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Specify the default command to run when the container starts
CMD ["python", "DiD-SendContainers.py"]
