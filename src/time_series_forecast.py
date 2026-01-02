import pandas as pd
import os
from statsmodels.tsa.arima.model import ARIMA


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


data_path = os.path.join(BASE_DIR, "data", "processed_metrics.csv")
df = pd.read_csv(data_path)


cpu_series = df["cpu"]


model = ARIMA(cpu_series, order=(1, 1, 1))
model_fit = model.fit()


forecast = model_fit.forecast(steps=5)

print("Predicted future CPU usage:")
print(forecast)

