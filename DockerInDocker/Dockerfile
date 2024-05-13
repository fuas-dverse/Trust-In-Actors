# Use the official Python base image
FROM python:3.8.3-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the application files into the container
COPY DiD-GetFolder.py /app
COPY standardVariables.py /app
COPY requirements.txt /app

# Install dependencies from requirements.txt
RUN pip install -r /app/requirements.txt

# Specify the default command to run when the container starts
CMD ["python", "DiD-GetFolder.py"]
