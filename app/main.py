import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set Streamlit config
st.set_page_config(page_title="Solar Potential Comparison", layout="wide")

def load_data():
    return pd.read_csv("/home/alki/10_academy/solar-data-discovery-Week0/data/Data_merged.csv")

Data_merged = load_data()

# Sidebar: Controls
st.sidebar.header("Filters")
selected_countries = st.sidebar.multiselect(
    "Select countries", 
    options=Data_merged["country"].unique(), 
    default=list(Data_merged["country"].unique())
)

selected_metric = st.sidebar.selectbox(
    "Select Metric", 
    options=["GHI", "DNI", "DHI"]
)

# Filtered Data
filtered_Data_merged = Data_merged[Data_merged["country"].isin(selected_countries)]

# Title
st.title("Solar Potential Cross-Country Dashboard")
st.markdown(f"### Metric: {selected_metric}")

# --- BOXPLOT ---
st.subheader(f"{selected_metric} Distribution by Country")
fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(data=filtered_Data_merged, x="country", y=selected_metric, palette="Set2", ax=ax)
st.pyplot(fig)

# --- SUMMARY TABLE ---
st.subheader("Summary Statistics")
summary = (
    filtered_Data_merged
    .groupby("country")[["GHI", "DNI", "DHI"]]
    .agg(["mean", "median", "std"])
    .round(2)
)
st.dataframe(summary)

# --- BAR CHART ---
st.subheader("Average GHI per Country")
avg_ghi = Data_merged.groupby("country")["GHI"].mean().sort_values(ascending=False)
fig2, ax2 = plt.subplots()
avg_ghi.plot(kind="bar", color="orange", ax=ax2)
ax2.set_ylabel("Average GHI")
st.pyplot(fig2)

# Footer
st.markdown("---")
st.markdown("Built by Ali Kibret | Solar Potential Dashboard | © 2025")
