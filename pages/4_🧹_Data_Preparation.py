import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="Data Preparation",
    page_icon="🧹",
    layout="wide"
)

st.title("🧹 Data Preparation")

# ===============================
# LOAD DATA
# ===============================
df_raw = pd.read_csv("data/Food_Delivery_Times.csv")
df_clean = pd.read_csv("data/Food_Delivery_Times_final.csv")

# ===============================
# DATA QUALITY SUMMARY
# ===============================
st.markdown("### 📊 Data Quality Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Raw Data", f"{df_raw.shape[0]:,} rows")
col2.metric("Clean Data", f"{df_clean.shape[0]:,} rows")
col3.metric("Missing Values (Clean)", df_clean.isna().sum().sum())

# ===============================
# 1. MISSING VALUE
# ===============================
with st.expander("1️⃣ Missing Value Handling", expanded=True):

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**📍 Before Cleaning**")
        st.dataframe(df_raw.isnull().sum())

    with col2:
        st.markdown("**✅ After Cleaning**")
        st.dataframe(df_clean.isnull().sum())

    st.success("""
    ✔ Semua missing value telah ditangani.  
    ✔ Dataset siap digunakan untuk analisis dan modeling tanpa bias akibat data kosong.
    """)

# ===============================
# 2. DUPLICATE
# ===============================
with st.expander("2️⃣ Duplicate Check"):

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Before Cleaning", df_raw.shape[0])
    with col2:
        st.metric("After Cleaning", df_clean.shape[0])

    st.info("""
    Tidak ditemukan duplikasi data, sehingga tidak diperlukan proses deduplikasi.
    """)

# ===============================
# 3. OUTLIER
# ===============================
with st.expander("3️⃣ Outlier Treatment"):

    st.markdown("""
    📍 Outlier dianalisis pada variabel **delivery_time_min** karena berpengaruh langsung terhadap target model.
    
    - Sebelum cleaning: terdapat nilai ekstrem yang dapat mengganggu performa model  
    - Setelah cleaning: distribusi lebih stabil dan representatif
    """)

    fig, axes = plt.subplots(1, 2, figsize=(12,5))

    sns.boxplot(y=df_raw['Delivery_Time_min'], ax=axes[0])
    axes[0].set_title("Before Cleaning", weight="bold")

    sns.boxplot(y=df_clean['delivery_time_min'], ax=axes[1])
    axes[1].set_title("After Cleaning", weight="bold")

    st.pyplot(fig)

    st.success("""
    ✔ Outlier berhasil diatasi  
    ✔ Distribusi data menjadi lebih normal  
    ✔ Potensi peningkatan performa model
    """)

# ===============================
# 4. FEATURE ENGINEERING
# ===============================
with st.expander("4️⃣ Feature Engineering"):

    st.markdown("""
    Feature engineering dilakukan untuk meningkatkan kemampuan model dalam menangkap pola data.

    **Fitur baru:**
    - 🧠 `courier_experience_category` → kategorisasi pengalaman kurir  
    - 📏 `distance_per_experience` → efisiensi kurir dalam menempuh jarak
    """)

    st.dataframe(
        df_clean[['courier_experience_yrs',
                  'courier_experience_category',
                  'distance_km',
                  'distance_per_experience']].head()
    )

    st.success("""
    ✔ Fitur tambahan memberikan representasi data yang lebih informatif  
    ✔ Membantu model memahami hubungan kompleks antar variabel
    """)

# ===============================
# FINAL INSIGHT
# ===============================
st.markdown("### 💡 Key Takeaways")

st.success("""
- Dataset telah bersih dari missing value dan outlier  
- Tidak ditemukan duplikasi data  
- Feature engineering meningkatkan kualitas representasi data  
- Dataset siap untuk tahap modeling dengan risiko bias yang lebih rendah  
""")