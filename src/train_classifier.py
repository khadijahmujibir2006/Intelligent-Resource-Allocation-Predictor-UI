import pandas as pd
import joblib
import os
from sklearn.ensemble import RandomForestClassifier

# Get project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load processed data
data_path = os.path.join(BASE_DIR, "data", "processed_metrics.csv")
df = pd.read_csv(data_path)

# Input features and target
X = df[["cpu", "memory", "disk"]]
y = df["label"]

# Train classification model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Save model
model_path = os.path.join(BASE_DIR, "models", "workload_classifier.pkl")
joblib.dump(model, model_path)

print("Workload classification model trained and saved.")
