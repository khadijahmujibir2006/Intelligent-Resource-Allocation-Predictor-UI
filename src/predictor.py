import psutil
import joblib
import pandas as pd
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


regressor_path = os.path.join(BASE_DIR, "models", "cpu_regressor.pkl")
classifier_path = os.path.join(BASE_DIR, "models", "workload_classifier.pkl")

cpu_regressor = joblib.load(regressor_path)
workload_classifier = joblib.load(classifier_path)


cpu = psutil.cpu_percent()
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent


input_data = pd.DataFrame(
    [[memory, disk, cpu / (memory + 1)]],
    columns=["memory", "disk", "cpu_memory_ratio"]
)


predicted_cpu = cpu_regressor.predict(input_data)[0]


workload = workload_classifier.predict([[cpu, memory, disk]])[0]


print("\n===== INTELLIGENT RESOURCE ALLOCATION PREDICTOR =====\n")
print(f"Current CPU Usage      : {cpu:.2f}%")
print(f"Current Memory Usage   : {memory:.2f}%")
print(f"Current Disk Usage     : {disk:.2f}%\n")

print(f"Predicted CPU Usage    : {predicted_cpu:.2f}%")
print(f"Workload Classification: {workload}\n")


if workload == "Heavy":
    print("Recommendation: Allocate MORE CPU cores and memory.")
elif workload == "Medium":
    print("Recommendation: Maintain BALANCED resource allocation.")
else:
    print("Recommendation: Reduce resource usage or save power.")

print("\n=====================================================\n")

