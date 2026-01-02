import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

input_file = os.path.join(BASE_DIR, "data", "system_metrics.csv")
output_file = os.path.join(BASE_DIR, "data", "processed_metrics.csv")

df = pd.read_csv(input_file)

df["cpu_memory_ratio"] = df["cpu"] / (df["memory"] + 1)

df.to_csv(output_file, index=False)

print("Feature engineering completed.")
