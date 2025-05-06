import streamlit as st
import pandas as pd
import requests
import plotly.express as px
from datetime import datetime

# تنظیمات صفحه
st.set_page_config(page_title="Bitcoin Macro Dashboard", layout="wide")

# --- Header ---
st.title("🪙 Bitcoin Macro Scenario Dashboard")
st.markdown("""
This dashboard displays key macroeconomic scenarios and their potential impacts on Bitcoin.
Use the **Refresh Data** button below to reload all charts and the latest price.
""")

# --- Refresh Button ---
if st.button("🔁 Refresh Data"):
    st.experimental_rerun()

# --- دریافت داده‌ها از FRED API ---
def get_fred_data(series_id, api_key):
    url = f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={api_key}&file_type=json"
    response = requests.get(url)
    data = response.json()
    return data['observations']

api_key = "3d1c28f747d422d401d09c747ceae357"  # کلید API شما

# مثال: دریافت داده نرخ بهره از FRED (Federal Funds Rate)
interest_rate_data = get_fred_data("FEDFUNDS", api_key)

# تبدیل داده‌ها به DataFrame
interest_rate_df = pd.DataFrame(interest_rate_data)
interest_rate_df['date'] = pd.to_datetime(interest_rate_df['date'])
interest_rate_df['value'] = interest_rate_df['value'].astype(float)

# نمایش نمودار نرخ بهره
st.subheader("📈 Federal Funds Rate")
fig1 = px.line(interest_rate_df, x='date', y='value', title="Federal Funds Rate Over Time")
st.plotly_chart(fig1, use_container_width=True)

# --- اضافه کردن بیشتر داده‌ها (PCE, GDP, Unemployment, ... ) ---
# شما می‌توانید داده‌های بیشتری مانند PCE Inflation یا GDP را به همین صورت اضافه کنید.

# --- Footer ---
st.markdown("""
---
Made with ❤️ using Streamlit and FRED API
""")
