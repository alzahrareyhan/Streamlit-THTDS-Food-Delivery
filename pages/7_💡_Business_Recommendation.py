import streamlit as st
import pandas as pd
import plotly.express as px

# ===============================
# CONFIG
# ===============================
st.set_page_config(page_title="Business Recommendation", layout="wide")
st.title("💡 Business Recommendation")

# ===============================
# LOAD DATA
# ===============================
df = pd.read_csv("data/Food_Delivery_Times_final.csv")

# ===============================
# KPI (REAL DATA)
# ===============================
st.markdown("### 📊 Key Performance Indicators")

avg_time = df["delivery_time_min"].mean()
sla_rate = (df["delivery_time_min"] <= 30).mean() * 100

# dummy satisfaction logic (based on SLA)
customer_sat = min(100, sla_rate + 15)

col1, col2, col3 = st.columns(3)

col1.metric("Avg Delivery Time", f"{avg_time:.1f} min")
col2.metric("SLA ≤ 30 min", f"{sla_rate:.1f}%")
col3.metric("Est. Customer Satisfaction", f"{customer_sat:.0f}%")

# ===============================
# PERFORMANCE DISTRIBUTION
# ===============================
st.markdown("### 📈 Delivery Performance Overview")

fig = px.histogram(
    df,
    x="delivery_time_min",
    nbins=30,
    title="Distribution of Delivery Time"
)
st.plotly_chart(fig, use_container_width=True)

# ===============================
# KEY DRIVERS
# ===============================
st.markdown("### 🔍 Key Drivers of Delay")

col1, col2 = st.columns(2)

with col1:
    fig = px.box(df, x="traffic_level", y="delivery_time_min",
                 title="Traffic Impact")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.scatter(df, x="distance_km", y="delivery_time_min",
                     title="Distance Impact")
    st.plotly_chart(fig, use_container_width=True)

# ===============================
# STRATEGIC PRIORITY
# ===============================
st.markdown("### 🎯 Strategic Priorities")

priority_df = pd.DataFrame({
    "Strategy": [
        "Optimize Driver Allocation",
        "Reduce Preparation Time",
        "Traffic-based Dispatch",
        "Courier Training Program"
    ],
    "Impact Score": [9, 8, 7, 6]
})

fig = px.bar(priority_df, x="Impact Score", y="Strategy",
             orientation="h", title="Strategy Impact Priority")

fig.update_layout(yaxis=dict(autorange="reversed"))

st.plotly_chart(fig, use_container_width=True)

# ===============================
# RECOMMENDATIONS
# ===============================
st.markdown("### 📌 Actionable Recommendations")

with st.expander("🚴 Driver Optimization"):
    st.write("""
    - Gunakan model prediksi untuk alokasi kurir secara dinamis  
    - Prioritaskan motor di area padat  
    """)

with st.expander("🍽️ Restaurant Efficiency"):
    st.write("""
    - Sinkronisasi preparation time dengan pickup  
    - Target waktu masak < 30 menit  
    """)

with st.expander("💙 Customer Experience"):
    st.write("""
    - Tampilkan ETA real-time  
    - Gunakan kategori delivery (Fast/Normal/Slow)  
    """)

with st.expander("🎁 Courier Strategy"):
    st.write("""
    - Berikan insentif untuk kurir cepat  
    - Training untuk kurir baru  
    """)

# ===============================
# BUSINESS IMPACT
# ===============================
st.markdown("### 💰 Expected Business Impact")

st.success("""
- ⬆️ Customer satisfaction meningkat  
- ⬇️ Delay & complaint berkurang  
- ⬆️ Efisiensi operasional  
- ⬆️ Retention & repeat order  
""")