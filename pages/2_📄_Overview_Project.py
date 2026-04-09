import streamlit as st

# ===============================
# CONFIG
# ===============================
st.set_page_config(
    page_title="Project Overview",
    page_icon="📄",
    layout="wide"
)

# ===============================
# CUSTOM STYLE
# ===============================
st.markdown("""
<style>
    .title {
        font-size: 38px;
        font-weight: 700;
        color: #FF4B4B;
    }

    .card-hover {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 14px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.06);
        margin-bottom: 15px;
        transition: all 0.3s ease;
        cursor: pointer;
    }

    .card-hover:hover {
        transform: translateY(-6px) scale(1.02);
        box-shadow: 0px 14px 28px rgba(0,0,0,0.2);
        border: 1px solid #FF4B4B;
    }

    .section-title {
        font-size: 22px;
        font-weight: 600;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ===============================
# HEADER
# ===============================
st.markdown('<h1 class="title">📄 Project Overview</h1>', unsafe_allow_html=True)

# ===============================
# METRICS (INTERAKTIF FEEL)
# ===============================
st.markdown("### 📌 Project Impact")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🎯 Objective", "Prediction")
    st.caption("Estimasi waktu delivery")

with col2:
    st.metric("📊 Approach", "ML")
    st.caption("Machine Learning Model")

with col3:
    st.metric("🚀 Output", "Insight")
    st.caption("Business Recommendation")

# ===============================
# BUSINESS UNDERSTANDING
# ===============================
st.markdown("### 🏢 Business Understanding")

st.markdown("""
<div class="card-hover">
Dalam industri <b>food delivery</b>, ketepatan waktu pengiriman menjadi faktor krusial yang berdampak langsung pada:
<ul>
    <li>✅ Kepuasan pelanggan</li>
    <li>✅ Loyalitas & repeat order</li>
    <li>✅ Daya saing perusahaan</li>
</ul>
Keterlambatan pengiriman dapat menurunkan pengalaman pengguna dan berpotensi mengurangi pendapatan bisnis.
</div>
""", unsafe_allow_html=True)

with st.expander("💡 Insight"):
    st.success("Delivery time menjadi key driver utama dalam customer experience dan retention.")

# ===============================
# BACKGROUND
# ===============================
st.markdown("### 📌 Background")

st.markdown("""
<div class="card-hover">
Pertumbuhan pengguna aplikasi food delivery 📱 meningkatkan kompleksitas operasional:
<ul>
    <li>Variasi kondisi eksternal (cuaca, traffic, jarak)</li>
    <li>Lonjakan order di waktu tertentu</li>
</ul>

Tanpa sistem prediksi:
<ul>
    <li>⏱ Estimasi tidak akurat</li>
    <li>📉 Kepuasan menurun</li>
    <li>🚴 Inefisiensi driver</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ===============================
# OBJECTIVES
# ===============================
st.markdown("### 🎯 Project Objectives")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card-hover">
    <b>Model Development</b>
    <ul>
        <li>🔹 Prediksi waktu delivery</li>
        <li>🔹 Meningkatkan akurasi</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card-hover">
    <b>Business Value</b>
    <ul>
        <li>🔹 Identifikasi faktor utama</li>
        <li>🔹 Insight berbasis data</li>
        <li>🔹 Optimasi operasional</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ===============================
# QUESTIONS
# ===============================
st.markdown("### ❓ Key Business Questions")

st.markdown("""
<div class="card-hover">
<ul>
    <li>🔍 Faktor utama delay?</li>
    <li>📉 Cara mengurangi keterlambatan?</li>
    <li>📊 Seberapa akurat model?</li>
    <li>💡 Bagaimana implementasi bisnis?</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ===============================
# MINI INTERACTION 🔥
# ===============================
st.markdown("### 🎮 Quick Thinking")

choice = st.selectbox(
    "Menurut kamu faktor paling berpengaruh?",
    ["Distance", "Traffic", "Weather", "Preparation Time"]
)

if choice == "Traffic":
    st.success("✅ Correct! Traffic biasanya punya dampak terbesar terhadap delay.")
else:
    st.info("💡 Insight: Traffic biasanya menjadi faktor dominan dalam delivery time.")

# ===============================
# FOOTER
# ===============================
st.markdown("---")
st.caption("✨ Data-Driven Decision Making | Food Delivery Analytics Project")