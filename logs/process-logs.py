import json
import time
from prometheus_client import start_http_server, Counter

log_file_path = "/var/log/amqp-client/receiver.log"

# Metrics
processed_logs_counter = Counter('processed_logs', 'Number of processed log entries')

def tail_log_file(file_path):
    with open(file_path, "r") as file:
        file.seek(0, 2)  # Move the cursor to the end of the file
        while True:
            line = file.readline()
            if not line:
                time.sleep(0.5)  # Sleep briefly
                continue
            yield line

def process_log_entry(log_entry):
    try:
        data = json.loads(log_entry)
        # Increment the counter for each processed log entry
        processed_logs_counter.inc()
        # Example of processing the log entry, e.g., printing the delivery time
        print(f"Delivery Time: {data['delivery-time']}")
    except json.JSONDecodeError:
        print("Error decoding JSON.")

if __name__ == "__main__":
    # Start up the server to expose the metrics.
    start_http_server(8000)
    for line in tail_log_file(log_file_path):
        process_log_entry(line.strip())

