
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Railway Analytics Dashboard", layout="wide")
st.title("🚦 Indian Railways Real-Time Risk Alerting Dashboard")

# ---- Upload or use preloaded datasets ----
uploaded_file = st.file_uploader("📤 Upload latest Railway Sensor CSV data (Environmental + Weather + Error + Maintenance)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📄 Uploaded Sensor Data")
    st.dataframe(df.head())

    try:
        model = joblib.load("accident_risk_model.pkl")  # Make sure this is present in the same repo
        prediction = model.predict(df)
        df["Prediction"] = prediction
        st.subheader("⚠️ Alert Results")
        for i, row in df.iterrows():
            if row["Prediction"] == 1:
                st.error(f"🚨 High Risk at Row {i+1}")
            else:
                st.success(f"✅ Safe at Row {i+1}")
    except Exception as e:
        st.warning("🚫 Model not found or failed to load.")
        st.code(str(e))

# ---- Static Dataset Explorations ----
with st.expander("📊 View Static Datasets"):
    st.write("Environmental Factors:")
    st.dataframe(pd.read_csv("Environmental_Factors.csv").head())

    st.write("Historical Weather:")
    st.dataframe(pd.read_csv("Historical_Weather.csv").head())

    st.write("Human Error Factors:")
    st.dataframe(pd.read_csv("Human_Error_Factors.csv").head())

    st.write("Maintenance Logs:")
    st.dataframe(pd.read_csv("Maintenance_Schedules_Log.csv").head())

    st.write("Railway Points Map Data:")
    st.dataframe(pd.read_csv("hotosm_ind_railways_points.csv").head())

    st.write("Railway Line Map Data:")
    st.dataframe(pd.read_csv("hotosm_ind_railways_lines_shp.csv").head())
