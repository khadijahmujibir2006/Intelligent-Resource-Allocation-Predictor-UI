import pandas as pd
import joblib
import os
from sklearn.linear_model import LinearRegression

# Get project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load processed data
data_path = os.path.join(BASE_DIR, "data", "processed_metrics.csv")
df = pd.read_csv(data_path)

# Input features (X) and output (y)
X = df[["memory", "disk", "cpu_memory_ratio"]]
y = df["cpu"]

# Train regression model
model = LinearRegression()
model.fit(X, y)

# Save model
model_path = os.path.join(BASE_DIR, "models", "cpu_regressor.pkl")
joblib.dump(model, model_path)

print("CPU regression model trained and saved.")
