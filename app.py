import streamlit as st
import pandas as pd
import numpy as np

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(page_title="Food Delivery Project", page_icon="🍔", layout="wide")

# ===============================
# CUSTOM CSS HOVER CARD
# ===============================
st.markdown("""
<style>
.card-hover {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 15px;
    transition: all 0.3s ease;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.08);
    cursor: pointer;
    margin-bottom: 15px;
}
.card-hover:hover {
    transform: translateY(-5px) scale(1.02);
    box-shadow: 0px 12px 25px rgba(0,0,0,0.2);
    border: 1px solid #FF4B4B;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# HERO SECTION
# ===============================
st.title("🍔 Food Delivery Time Prediction")
st.subheader("Turning Data into Faster Delivery 🚴")
st.write("""
Aplikasi ini membantu menganalisis dan memprediksi waktu pengiriman makanan
berdasarkan berbagai faktor operasional seperti jarak, cuaca, traffic, dan pengalaman kurir.
""")
st.markdown("---")

# ===============================
# WORKFLOW (INTERAKTIF)
# ===============================
st.subheader("🔎 Project Workflow")

dot = """
digraph {
    rankdir=LR
    node [shape=box, style="rounded,filled", fillcolor="#F4F6F7"]

    A [label="About Me"]
    B [label="Project Overview"]
    C [label="Data Understanding"]
    D [label="Data Preparation"]
    E [label="EDA"]
    F [label="Modeling"]
    G [label="Recommendation"]
    H [label="Contact"]

    A -> B -> C -> D -> E -> F -> G -> H
}
"""

with st.expander("Klik untuk lihat alur project"):
    st.graphviz_chart(dot, use_container_width=True)

st.markdown("---")

# ===============================
# VALUE PROPOSITION (HOVER CARDS)
# ===============================
st.subheader("🚀 Project Value")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="card-hover">
    ⏱️ <b>Accuracy</b><br>Estimasi lebih akurat
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card-hover">
    🚴 <b>Efficiency</b><br>Pengiriman lebih cepat
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card-hover">
    😊 <b>Customer</b><br>Kepuasan meningkat
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card-hover">
    📊 <b>Insight</b><br>Berbasis data
    </div>
    """, unsafe_allow_html=True)
st.markdown("---")

# ===============================
# SIMULATION (INTERAKTIF)
# ===============================
st.subheader("🎮 Delivery Simulation")
col1, col2 = st.columns(2)

with col1:
    distance = st.slider("📍 Distance (km)", 1, 20, 5)
    traffic = st.selectbox("🚦 Traffic", ["Low", "Medium", "High"])

with col2:
    weather = st.selectbox("🌤️ Weather", ['Clear', 'Rainy', 'Snowy', 'Windy', 'Foggy'])
    prep_time = st.slider("🍳 Preparation Time (min)", 5, 60, 15)

# Prediksi delivery dengan faktor traffic & cuaca
traffic_factor = {"Low":0, "Medium":5, "High":10}
weather_factor = {"Clear":0, "Rainy":5, "Snowy":10, "Windy":3, "Foggy":7}
pred_time = distance*2 + prep_time + traffic_factor[traffic] + weather_factor[weather]
pred_time = max(pred_time, prep_time)

# Result
st.metric("📦 Estimated Delivery Time", f"{pred_time} min")

# Insight
st.markdown("### 💡 Quick Insight")
if pred_time > 40:
    st.warning(f"Delivery berpotensi lama → {pred_time} min, perlu optimasi")
elif pred_time > 25:
    st.info(f"Delivery dalam kondisi normal → {pred_time} min")
else:
    st.success(f"Delivery cepat & optimal → {pred_time} min")

# Chart simulasi
st.markdown("### 🔢 Predicted Time by Distance")
distances = np.arange(1,21)
times = distances*2 + prep_time + np.array([traffic_factor[traffic]]*20) + np.array([weather_factor[weather]]*20)
df_chart = pd.DataFrame({"Distance (km)": distances, "Predicted Time (min)": times})
st.line_chart(df_chart.set_index("Distance (km)"))

st.markdown("---")

# ===============================
# PROJECT DESCRIPTION (HOVER CARD)
# ===============================
st.subheader("📌 What This Project Does")
desc_card = """
<div class="card-hover">
- 📊 Menganalisis faktor utama yang mempengaruhi waktu pengiriman<br>
- 🧠 Membangun model prediksi berbasis machine learning<br>
- 📈 Memberikan insight untuk meningkatkan efisiensi operasional<br>
- 💡 Menyediakan rekomendasi strategis berbasis data
</div>
"""
st.markdown(desc_card, unsafe_allow_html=True)

st.markdown("---")

# ===============================
# CTA
# ===============================
if st.button("🚀 Explore Full Analysis"):
    st.success("Scroll ke atas untuk menjelajahi seluruh analisis!")