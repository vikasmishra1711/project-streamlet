import streamlit as st
import pandas as pd
import numpy as np

# 1. Page Setup
st.set_page_config(
    page_title="Pure Streamlit Dashboard",
    page_icon="📈",
    layout="wide"
)

# 2. Generate Random Mock Data using Pandas/Numpy
@st.cache_data
def get_data():
    dates = pd.date_range(start="2026-01-01", periods=30, freq="D")
    return pd.DataFrame({
        "Date": dates,
        "Revenue": np.random.randint(10000, 25000, size=30),
        "Signups": np.random.randint(50, 200, size=30),
        "Category": np.random.choice(["SaaS", "Hardware", "Consulting"], size=30)
    }).set_index("Date")

df = get_data()

# 3. Sidebar Filtering
st.sidebar.header("Dashboard Filters")
selected_category = st.sidebar.selectbox(
    "Choose Business Unit:",
    options=["All Categories"] + list(df["Category"].unique())
)

# Filter Data
if selected_category != "All Categories":
    filtered_df = df[df["Category"] == selected_category]
else:
    filtered_df = df

# 4. Header Zone
st.title("📈 large development Business Overview")
st.caption("A clean, production-ready dashboard built entirely with native Streamlit features.")
st.divider()

# 5. Native KPI Cards
m1, m2, m3 = st.columns(3)

with m1:
    total_rev = filtered_df["Revenue"].sum()
    st.metric(label="Total Revenue", value=f"${total_rev:,}", delta="+12%")

with m2:
    total_signups = filtered_df["Signups"].sum()
    st.metric(label="New Signups", value=f"{total_signups:,}", delta="+45")

with m3:
    avg_deal = int(filtered_df["Revenue"].mean())
    st.metric(label="Average Daily Revenue", value=f"${avg_deal:,}", delta="-2%")

st.divider()

# 6. Native Visualizations
left_chart, right_chart = st.columns(2)

with left_chart:
    st.subheader("Revenue Progression")
    # Streamlit line charts automatically style beautifully based on the theme
    st.line_chart(filtered_df["Revenue"], color="#0066cc")

with right_chart:
    st.subheader("Signups Breakdown")
    # Native bar chart
    st.bar_chart(filtered_df["Signups"], color="#ff4b4b")

st.divider()

# 7. Inline Data View
with st.expander("🔍 Inspect Underlying Data Table"):
    st.dataframe(filtered_df, use_container_width=True)