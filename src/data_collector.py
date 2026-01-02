import psutil
import time
import csv
import os

# Find project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create data folder if it doesn't exist
data_folder = os.path.join(BASE_DIR, "data")
os.makedirs(data_folder, exist_ok=True)

# Full path to CSV file
file_path = os.path.join(data_folder, "system_metrics.csv")

with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["cpu", "memory", "disk", "label"])

    for _ in range(30):  # keep small for testing
        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        if cpu < 30:
            label = "Light"
        elif cpu < 70:
            label = "Medium"
        else:
            label = "Heavy"

        writer.writerow([cpu, memory, disk, label])
        time.sleep(1)
