import streamlit as st
import pandas as pd
import time
from datetime import datetime

st.set_page_config(page_title="🛡️ Honeypot Dashboard", layout="wide")

st.title("🕵️ Honeypot Attacker Logs")
st.markdown("Monitor attacker IPs, payloads, and frequency.")

import sqlite3

DB_FILE = "honeypot_logs.db"

@st.cache_data(ttl=10)
def load_data():
    try:
        conn = sqlite3.connect(DB_FILE)
        df = pd.read_sql_query("SELECT * FROM logs", conn)
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        return df
    except Exception as e:
        st.error(f"Failed to load DB: {e}")
        return pd.DataFrame(columns=["Timestamp", "Attacker_IP", "Payload"])


df = load_data()

# Show data
if df.empty:
    st.warning("No log data available yet.")
else:
    with st.expander("🔍 Filter Logs"):
        ip_filter = st.text_input("Filter by Attacker IP")
        payload_filter = st.text_input("Search Payload")

        filtered_df = df.copy()

        if ip_filter:
            filtered_df = filtered_df[filtered_df['Attacker_IP'].str.contains(ip_filter)]
        if payload_filter:
            filtered_df = filtered_df[filtered_df['Payload'].str.contains(payload_filter)]

    st.subheader("📜 Attacker Log Table")
    st.dataframe(filtered_df, use_container_width=True)

    st.subheader("📊 Attack Frequency by IP")
    ip_counts = df['Attacker_IP'].value_counts()
    st.bar_chart(ip_counts)

    st.subheader("📈 Attacks Over Time")
    df_time = df.groupby(pd.Grouper(key='Timestamp', freq='1Min')).size()
    st.line_chart(df_time)

    # Download
    st.download_button("⬇️ Download Logs", df.to_csv(index=False), "honeypot_logs.csv", "text/csv")

# Footer
st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
