# Use an official lightweight Python image
FROM python:3.7-alpine

# Install the Prometheus client library for Python
RUN pip install prometheus_client

# Set the working directory in the container to /app
WORKDIR /app

# Copy the Python script into the container at /app
COPY process-logs.py .

# Make port 8000 available to the world outside this container
# This is the port on which the metrics are exposed
EXPOSE 8000

# Run the Python application when the container launches
CMD ["python", "-u", "process-logs.py"]

