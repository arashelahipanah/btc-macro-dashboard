
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Bitcoin Macro Dashboard", layout="wide")

# --- Header ---
st.title("🪙 Bitcoin Macro Scenario Dashboard")
st.markdown("""
This dashboard displays key macroeconomic scenarios and their potential impacts on Bitcoin.
Use the **Refresh Data** button below to reload all charts.
""")

# --- Refresh Button ---
if st.button("🔁 Refresh Data"):
    st.experimental_rerun()

# --- Data Setup ---
data = pd.DataFrame({
    "Scenario": [
        "Interest Rate stays at 5.25%",
        "PCE Inflation remains high",
        "GDP returns to positive growth",
        "Unemployment remains stable",
        "LEI continues to decline",
        "Consumer Confidence drops again",
        "LAG indicates mild recession",
        "Trade Deficit improves slightly",
        "CEI remains stable"
    ],
    "Probability (%)": [95, 60, 65, 80, 75, 60, 70, 50, 90],
    "BTC Impact": [
        "Neutral to slightly bullish (expectation priced in)",
        "Short-term bearish, long-term bullish",
        "Short-term bearish, long-term neutral",
        "Neutral (priced in)",
        "Bullish - safe haven appeal grows",
        "Volatile - market uncertainty",
        "Cautious bullish - stress asset",
        "Mild support if USD weakens",
        "Little to no direct impact"
    ]
})

# --- Readable Chart ---
st.subheader("📊 Scenario Probabilities and BTC Impact")
fig1 = px.bar(
    data,
    y="Scenario",
    x="Probability (%)",
    orientation='h',
    color="Probability (%)",
    text="BTC Impact",
    color_continuous_scale="Teal",
    height=600
)
fig1.update_traces(textposition='outside')
fig1.update_layout(xaxis_title="Probability of Occurrence (%)", yaxis_title="Scenario")
st.plotly_chart(fig1, use_container_width=True)

# --- Priority Chart ---
priority_data = pd.DataFrame({
    "Indicator": [
        "Interest Rate (IR)", "PCE Inflation", "GDP", "Unemployment Rate", "LEI",
        "Consumer Confidence", "LAG", "Trade Balance", "CEI"
    ],
    "Impact Priority (1=High)": [1, 2, 3, 4, 5, 6, 7, 8, 9]
})

st.subheader("🔥 Priority of Macro Indicators Affecting Bitcoin")
fig2 = px.bar(
    priority_data.sort_values("Impact Priority (1=High)"),
    x="Impact Priority (1=High)",
    y="Indicator",
    orientation='h',
    color="Impact Priority (1=High)",
    color_continuous_scale="Reds"
)
st.plotly_chart(fig2, use_container_width=True)

# --- Footer ---
st.markdown("""
---
Made with ❤️ using Streamlit
""")
