import pandas as pd
import os
from statsmodels.tsa.arima.model import ARIMA

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load processed metrics
data_path = os.path.join(BASE_DIR, "data", "processed_metrics.csv")
df = pd.read_csv(data_path)

# CPU usage as time series
cpu_series = df["cpu"]

# Train ARIMA model
model = ARIMA(cpu_series, order=(1, 1, 1))
model_fit = model.fit()

# Forecast next 5 values
forecast = model_fit.forecast(steps=5)

print("Predicted future CPU usage:")
print(forecast)
