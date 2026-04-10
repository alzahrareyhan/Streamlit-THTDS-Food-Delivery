import streamlit as st
from PIL import Image

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="About Me - Reyhan",
    page_icon="👩‍💻",
    layout="wide"
)

# ===============================
# CUSTOM STYLE (HOVER + UI)
# ===============================
st.markdown("""
<style>
    .subtitle {
        font-size: 18px;
        color: #6c757d;
    }

    /* CARD STYLE */
    .card-hover {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        transition: all 0.3s ease;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.08);
        cursor: pointer;
        margin-top: 20px;
    }

    /* HOVER EFFECT */
    .card-hover:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0px 12px 25px rgba(0,0,0,0.2);
        border: 1px solid #FF4B4B;
    }
</style>
""", unsafe_allow_html=True)

# ===============================
# HEADER
# ===============================
st.title("👩‍💻 About Me")

# ===============================
# PROFILE SECTION
# ===============================
col1, col2 = st.columns([1.5, 2])
with col1:
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
    st.image("images/Reyhan.jpeg", width=1550)
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown("""
    ### 👋 Halo, saya **Reyhan Nandita Al Zahra**
    <p class="subtitle">
    Saya merupakan seorang <b>Data Analyst</b> dengan ketertarikan pada <b>Data Science, Business Intelligence, dan Machine Learning</b>.  
    Saya memiliki kemampuan dalam mengolah dan menganalisis data untuk menghasilkan insight yang relevan, guna mendukung pengambilan keputusan bisnis yang lebih efektif dan strategis.
    </p>
    """, unsafe_allow_html=True)
    st.success("""
        🔬 **Featured Project**
                
        🍔 **Food Delivery Time Prediction**
                
        End-to-end project:
        - Business Understanding  
        - Data Preparation & EDA  
        - Machine Learning Modeling  
        - Business Insight & Recommendation  
               
        🚀 Built with interactive Streamlit dashboard
    """)
# ===============================
# METRICS / HIGHLIGHT
# ===============================
st.markdown("---")
col1, col2, col3 = st.columns(3)
col1.metric("📊 Projects", "5+")
col2.metric("🛠️ Tools", "10+")
col3.metric("📈 Focus", "Data & ML")

# ===============================
# SKILLS
# ===============================
st.markdown("---")
st.subheader("🛠️ Skills & Tools")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    **📊 Data Analysis**
    - Data Cleaning & Preprocessing  
    - Exploratory Data Analysis (EDA)  
    - Statistical Analysis
    """)
with col2:
    st.markdown("""
    **🤖 Tech Stack**
    - Python (Pandas, Scikit-learn)  
    - Visualization (Matplotlib, Plotly)  
    - BI Tools (Tableau, Power BI)  
    - Streamlit
    """)

# ===============================
# EDUCATION
# ===============================
st.markdown("---")
st.subheader("🎓 Education")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="card-hover">
    🎯 <b>Data Analyst & Data Science Bootcamp</b><br>
    Dibimbing.id
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="card-hover">
    🎓 <b>Teknik Informatika</b><br>
    Universitas Negeri Semarang
    </div>
    """, unsafe_allow_html=True)

# ===============================
# MOTTO
# ===============================
st.markdown("---")
st.subheader("💡 Motto")
st.markdown("""
<div class="card-hover">
“Committed to leveraging data and analytical skills to generate impactful insights, 
drive business decisions, and continuously adapt to evolving technologies.”
</div>
""", unsafe_allow_html=True)

# ===============================
# RESOURCES
# ===============================
st.markdown("---")
st.subheader("🔗 Project Links")
st.markdown("""
- 📄 [Project Slide Deck]https://canva.link/zvnpg8s700roux1)  
- 🍔 [Dataset – Kaggle](https://www.kaggle.com/datasets/denkuznetz/food-delivery-time-prediction)
""")

# ===============================
# FOOTER
# ===============================
st.markdown("---")
st.caption("✨ Built with Streamlit | © 2026 Reyhan Nandita Al Zahra")
