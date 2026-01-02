import pandas as pd
import joblib
import os
from sklearn.linear_model import LinearRegression


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


data_path = os.path.join(BASE_DIR, "data", "processed_metrics.csv")
df = pd.read_csv(data_path)


X = df[["memory", "disk", "cpu_memory_ratio"]]
y = df["cpu"]


model = LinearRegression()
model.fit(X, y)


model_path = os.path.join(BASE_DIR, "models", "cpu_regressor.pkl")
joblib.dump(model, model_path)

print("CPU regression model trained and saved.")

