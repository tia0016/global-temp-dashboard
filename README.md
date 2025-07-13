# 🌍 Global Temperature Dashboard (2000–2025)

This Streamlit dashboard visualizes global temperature anomalies from the year 2000 to 2025 using NASA's GISTEMP dataset. It helps highlight how the Earth's climate has changed over time in a simple, interactive way.

---

## 🔍 Features

- 📈 Interactive line chart showing temperature anomalies
- 🗃 Raw data table from NASA's public climate records
- 🎯 Clean UI built with Streamlit and Plotly

---

## 📊 Data Source

- NASA GISTEMP: [https://data.giss.nasa.gov/gistemp/](https://data.giss.nasa.gov/gistemp/)
- Dataset used: `GLB.Ts+dSST.csv` (Global temperature anomaly data)

---

## 🚀 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/tia0016/global-temp-dashboard.git
   cd global-temp-dashboard
   
Install the requirements:
pip install -r requirements.txt

Run the dashboard:
streamlit run app.py
## 📂 Project Structure

global-temp-dashboard/
│
├── app.py                  # Streamlit dashboard app
├── requirements.txt        # Python dependencies
├── README.md               # Project info
│
├── data/                   # Raw & cleaned datasets
│   └── cleaned_temp_data.csv
│
├── notebook/               # Jupyter notebook for data analysis
│   └── analysis.ipynb
│
└── assets/                 # Optional images/screenshot
