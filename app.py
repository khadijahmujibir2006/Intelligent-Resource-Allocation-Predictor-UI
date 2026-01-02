import streamlit as st
import joblib
import pandas as pd
import psutil
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="Intelligent Resource Allocation Predictor", layout="wide")

st.markdown("""
<style>
.main { background-color: #0f172a; }
h1, h2, h3 { color: #e5e7eb; }
</style>
""", unsafe_allow_html=True)

st.markdown("## ⚙️ Intelligent Resource Allocation Predictor")
st.caption("Real-time monitoring • ML prediction • Visual analytics")

cpu_model = joblib.load("models/cpu_regressor.pkl")
expected_features = list(cpu_model.feature_names_in_)

st.sidebar.header("🧩 Configuration")

workload = st.sidebar.selectbox("Expected Workload", ["Low", "Medium", "High"])
simulate = st.sidebar.checkbox("Simulate Extra CPU Load")
simulated_cpu = st.sidebar.slider("Simulated CPU Load (%)", 0, 50, 15) if simulate else 0

run = st.sidebar.button("🚀 Predict & Visualize")

if run:
    df = pd.read_csv("data/processed_metrics.csv")
    latest = df.iloc[-1]

    cpu = psutil.cpu_percent(interval=1) + simulated_cpu
    memory = psutil.virtual_memory().percent

    row = {}
    for col in expected_features:
        if col == "cpu_memory_ratio":
            row[col] = cpu / memory
        else:
            row[col] = latest[col]

    features = pd.DataFrame([row])
    predicted_cpu = cpu_model.predict(features)[0]

    st.divider()
    st.subheader("📊 Key Metrics")

    c1, c2, c3 = st.columns(3)
    c1.metric("Live CPU (%)", f"{cpu:.2f}")
    c2.metric("Memory Usage (%)", f"{memory:.2f}")
    c3.metric("Predicted CPU (%)", f"{predicted_cpu:.2f}")

    st.subheader("🧭 CPU Load Gauge")
    progress = st.progress(0)
    for i in range(int(predicted_cpu)):
        progress.progress(i + 1)
        time.sleep(0.01)

    if predicted_cpu > 80:
        st.error("🚨 Scale up resources immediately")
    elif predicted_cpu > 60:
        st.warning("⚠️ Monitor system closely")
    else:
        st.success("✅ Resources are sufficient")

    st.subheader("📈 Live vs Predicted CPU")
    fig1, ax1 = plt.subplots()
    ax1.plot(["Live CPU", "Predicted CPU"], [cpu, predicted_cpu], marker="o")
    ax1.axhline(70, linestyle="--")
    ax1.set_ylabel("CPU Usage (%)")
    st.pyplot(fig1)

    st.subheader("📊 CPU vs Memory Comparison")
    fig2, ax2 = plt.subplots()
    ax2.bar(["CPU Usage", "Memory Usage"], [cpu, memory])
    ax2.set_ylabel("Percentage (%)")
    st.pyplot(fig2)

    st.subheader("📉 Historical CPU Trend (Rolling Avg)")
    if "cpu_usage" in df.columns:
        df["rolling_cpu"] = df["cpu_usage"].rolling(5).mean()
        st.line_chart(df[["cpu_usage", "rolling_cpu"]].tail(40))

    st.caption("🔁 Visuals update every prediction for animation effect")
