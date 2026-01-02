import pandas as pd
import joblib
import os
from sklearn.ensemble import RandomForestClassifier


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


data_path = os.path.join(BASE_DIR, "data", "processed_metrics.csv")
df = pd.read_csv(data_path)


X = df[["cpu", "memory", "disk"]]
y = df["label"]


model = RandomForestClassifier(random_state=42)
model.fit(X, y)


model_path = os.path.join(BASE_DIR, "models", "workload_classifier.pkl")
joblib.dump(model, model_path)

print("Workload classification model trained and saved.")

