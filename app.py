import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
@st.cache_data
def load_data():
    data = pd.read_csv("data/GLB.Ts+dSST.csv", skiprows=1)
    data = data[['Year', 'J-D']]
    data = data[(data['Year'] >= 2000) & (data['Year'] <= 2025)]
    data.columns = ['Year', 'Temp_Anomaly']
    return data

# App Title
st.set_page_config(page_title="Global Temperature Trends", layout="centered")
st.title("🌍 Global Temperature Anomaly Dashboard (2000–2025)")
st.caption("Data source: NASA GISTEMP ")

# Load and show data
df = load_data()

# Line Chart
fig = px.line(df, x='Year', y='Temp_Anomaly',
              title='📈 Yearly Global Temperature Anomaly (°C)',
              markers=True,
              labels={'Temp_Anomaly': 'Temperature Anomaly (°C)'})
fig.update_layout(template="plotly_dark", xaxis_title="Year", yaxis_title="Anomaly (°C)")

st.plotly_chart(fig)

# Show Data Table
with st.expander("📄 View Raw Data"):
    st.dataframe(df)