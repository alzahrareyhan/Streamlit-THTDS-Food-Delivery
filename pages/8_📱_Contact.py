import streamlit as st

# ===============================
# CONFIG
# ===============================
st.set_page_config(page_title="Contact", layout="wide")

# ===============================
# HEADER
# ===============================
st.markdown("## 🤝 Let's Connect!")

st.markdown("""
Hi, I'm **Reyhan Nandita Al Zahra** 👋  
A passionate **Data Analyst** who loves turning data into actionable insights.

I'm open to:
- 📊 Data Analyst opportunities  
- 🤝 Collaboration & projects  
- 💬 Discussions about data & tech  
""")

st.markdown("---")

# ===============================
# CONTACT CARDS
# ===============================
st.markdown("### 🔗 Reach Me Here")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **💼 LinkedIn**  
    👉 https://www.linkedin.com/in/reyhan-nandita-al-zahra-64a82a278/

    **🐙 GitHub**  
    👉 https://github.com/alzahrareyhan
    """)

with col2:
    st.markdown("""
    **📱 WhatsApp**  
    👉 https://wa.me/6289607070668

    **📧 Email**  
    👉 alzahrareyhan@gmail.com   
    """)

# ===============================
# CTA
# ===============================
st.markdown("---")

st.success("""
🚀 Feel free to reach out anytime — I'm always excited to connect, collaborate, and grow together!
""")

# ===============================
# OPTIONAL MINI CTA BUTTON STYLE
# ===============================
st.markdown("### 📩 Quick Action")

st.markdown("""
- 💼 Connect on LinkedIn  
- 📧 Send me an email  
- 💬 Chat via WhatsApp  
""")

# ===============================
# FOOTER
# ===============================
st.markdown("---")
st.caption("✨ Built with Streamlit | Personal Portfolio")