import streamlit as st
import pandas as pd
import plotly.express as px

# ===============================
# CONFIG
# ===============================
st.set_page_config(
    page_title="Data Understanding",
    page_icon="📚",
    layout="wide"
)

# ===============================
# HELPER (ANTI ERROR 🔥)
# ===============================
def safe_df(df):
    return df.astype(str)

# ===============================
# LOAD DATA
# ===============================
df = pd.read_csv("data/Food_Delivery_Times_final.csv")
df_raw = pd.read_csv("data/Food_Delivery_Times.csv")

# ===============================
# HEADER
# ===============================
st.title("📚 Data Understanding")

st.markdown("""
Dataset ini digunakan untuk memprediksi **waktu pengiriman makanan** dengan mempertimbangkan berbagai faktor operasional seperti:

- 🚴‍♂️ Jarak pengiriman  
- 🌧️ Kondisi cuaca  
- 🚦 Tingkat lalu lintas  
- 🕒 Waktu pemesanan  
- 👨‍🍳 Pengalaman kurir  

Pendekatan ini relevan dalam konteks **logistik & operational optimization**.
""")

# ===============================
# METRICS
# ===============================
st.markdown("### 📌 Dataset Overview")

col1, col2, col3 = st.columns(3)
col1.metric("Jumlah Data", f"{df_raw.shape[0]:,}")
col2.metric("Jumlah Fitur", f"{df_raw.shape[1]:,}")
col3.metric("Missing Values", int(df_raw.isna().sum().sum()))

# ===============================
# DATA TYPES + MISSING
# ===============================
st.markdown("### 📂 Struktur Data")

col1, col2 = st.columns(2)

# 🔥 FIX DATA TYPE
df_types = df_raw.dtypes.reset_index()
df_types.columns = ["Column", "Data Type"]
df_types["Data Type"] = df_types["Data Type"].astype(str)

with col1:
    st.dataframe(df_types, use_container_width=True)

# 🔥 FIX MISSING
missing = df_raw.isna().sum().reset_index()
missing.columns = ["Column", "Missing Values"]

with col2:
    st.dataframe(safe_df(missing), use_container_width=True)

# ===============================
# DATA PREVIEW (INTERAKTIF)
# ===============================
st.markdown("### 🔍 Data Preview")

col1, col2 = st.columns([2,1])

with col2:
    selected_weather = st.selectbox(
        "Filter Weather",
        options=["All"] + sorted(df["weather"].dropna().unique().tolist())
    )

# filter
filtered_df = df.copy()
if selected_weather != "All":
    filtered_df = df[df["weather"] == selected_weather]

with col1:
    st.dataframe(safe_df(filtered_df.sample(5)), use_container_width=True)

# ===============================
# TARGET DISTRIBUTION
# ===============================
st.markdown("### 📈 Delivery Time Distribution")

fig = px.histogram(
    filtered_df,
    x="delivery_time_min",
    nbins=30,
    title="Distribution of Delivery Time",
    marginal="box"
)

st.plotly_chart(fig, use_container_width=True)

# ===============================
# RELATIONSHIP
# ===============================
st.markdown("### 🔗 Key Feature Relationship")

col1, col2 = st.columns(2)

with col1:
    fig_distance = px.scatter(
        filtered_df,
        x="distance_km",
        y="delivery_time_min",
        title="Distance vs Delivery Time"
    )
    st.plotly_chart(fig_distance, use_container_width=True)

with col2:
    fig_traffic = px.box(
        filtered_df,
        x="traffic_level",
        y="delivery_time_min",
        title="Traffic Level Impact"
    )
    st.plotly_chart(fig_traffic, use_container_width=True)

# ===============================
# FEATURE GROUPING
# ===============================
st.markdown("### 📋 Feature Groups")

with st.expander("Lihat detail feature"):
    st.markdown("""
    - **Order Info** → `order_id`  
    - **Delivery Condition** → `distance_km`, `weather`, `traffic_level`, `time_of_day`  
    - **Courier** → `courier_experience_yrs`, `courier_experience_category`  
    - **Restaurant** → `preparation_time_min`  
    - **Target** → `delivery_time_min`  
    """)

# ===============================
# INSIGHT DINAMIS 🔥
# ===============================
st.markdown("### 💡 Insight")

avg_time = filtered_df["delivery_time_min"].mean()

if avg_time > 35:
    st.warning(f"⏱️ Rata-rata delivery tinggi ({avg_time:.1f} min) → perlu optimasi")
elif avg_time > 25:
    st.info(f"📊 Delivery dalam range normal ({avg_time:.1f} min)")
else:
    st.success(f"🚀 Delivery cepat ({avg_time:.1f} min)")

# ===============================
# FOOTER
# ===============================
st.markdown("---")
st.caption("✨ Data Understanding | Food Delivery Analytics")