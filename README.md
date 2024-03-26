```
docker build -t upload_seagate_disk .


```


```
docker run -d -p 80:80 \
  --name upload_seagate_container \
  -v /media/yiyun/seagate/Timeline/:/media/yiyun/seagate/Timeline/ \
  -e FILE_STORAGE_PATH=/media/yiyun/seagate/Timeline/ \
  upload_seagate_disk
```



## Corresponding Http Download Support
To have the Python HTTP server serve on port 8001 instead, you'll need to adjust the command used to start the server within the Docker container. Additionally, you should map the appropriate port when running the Docker container to reflect this change. Here's how you can adjust both the Dockerfile and the Docker run command:

### Adjusted Dockerfile

If you want the Python HTTP server to serve on a port other than the default (80), you must modify the `CMD` in the Dockerfile to specify the desired port. However, Python's built-in HTTP server always serves on port 8000 by default when you don't specify a port. Since you want it to serve on port 8001, you'll need to explicitly set this in the command:

```Dockerfile
# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /data

# Specify the default command to run the Python HTTP server on port 8001
CMD ["python", "-m", "http.server", "8001"]
```

### Step to Build the Docker Image (Remains Unchanged)

Build the Docker image with the updated Dockerfile:

```sh
docker build -t python-http-server .
```

### Adjusted Docker Run Command

When running the Docker container, you should map the external port you wish to use (e.g., 8001) to the internal port that the server is running on (also 8001 in this case):

```sh
docker run -d -p 8001:8001 \
  --name python-http-container \
  -v /media/yiyun/seagate/Timeline/:/data \
  python-http-server
```

This command maps port 8001 on the host to port 8001 in the container, making the HTTP server accessible via `http://localhost:8001` or your host's IP address on port 8001.

Following these steps, you'll have a Python HTTP server running in a Docker container, serving files from `/media/yiyun/seagate/Timeline/` on your host machine, accessible through port 8001.
