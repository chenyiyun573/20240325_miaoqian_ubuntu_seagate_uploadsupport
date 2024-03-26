# Use an official Python runtime as the parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container
COPY . .

# Install any necessary packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 80 to the outside world
EXPOSE 80

# Set an environment variable for the file storage path
# This can be overridden at runtime if needed
ENV FILE_STORAGE_PATH=/media/yiyun/seagate/Timeline/

# Command to run the application using uvicorn
CMD ["uvicorn", "upload_server:app", "--host", "0.0.0.0", "--port", "80"]

