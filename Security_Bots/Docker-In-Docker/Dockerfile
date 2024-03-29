FROM docker:latest
RUN apk add --no-cache python3 py3-pip
# --break-system-packages is dangerous and can cause OS to break
RUN pip3 install docker --break-system-packages 
COPY myscript.py .
CMD ["python3", "/myscript.py"]

# To start it also include
# docker run -v /var/run/docker.sock:/var/run/docker.sock my-docker-app
# For output
# docker run -it -v /var/run/docker.sock:/var/run/docker.sock my-docker-app
