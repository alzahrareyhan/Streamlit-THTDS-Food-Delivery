import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# ===============================
# CONFIG
# ===============================
st.set_page_config(page_title="EDA", page_icon="📊", layout="wide")
st.title("📊 Exploratory Data Analysis (EDA)")

# ===============================
# LOAD DATA
# ===============================
df = pd.read_csv("data/Food_Delivery_Times_final.csv")

# ===============================
# SIDEBAR FILTER
# ===============================
st.sidebar.header("🔍 Filter")

weather_filter = st.sidebar.multiselect(
    "Weather",
    df["weather"].unique(),
    default=df["weather"].unique()
)

traffic_filter = st.sidebar.multiselect(
    "Traffic",
    df["traffic_level"].unique(),
    default=df["traffic_level"].unique()
)

df = df[
    (df["weather"].isin(weather_filter)) &
    (df["traffic_level"].isin(traffic_filter))
]

# ===============================
# KEY METRICS
# ===============================
st.markdown("### 📌 Key Metrics")

col1, col2, col3 = st.columns(3)
col1.metric("Avg Delivery Time", f"{df['delivery_time_min'].mean():.1f} min")
col2.metric("Max Delivery Time", f"{df['delivery_time_min'].max():.1f} min")
col3.metric("Avg Distance", f"{df['distance_km'].mean():.1f} km")

# ===============================
# TABS
# ===============================
tab1, tab2, tab3 = st.tabs(["📌 Univariate", "🔗 Bivariate", "🌐 Multivariate"])

# ===============================
# TAB 1 - UNIVARIATE
# ===============================
with tab1:
    st.subheader("📌 Univariate Analysis")

    col1, col2 = st.columns(2)

    with col1:
        fig = px.histogram(df, x="delivery_time_min", nbins=30,
                           title="Delivery Time Distribution")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.histogram(df, x="distance_km", nbins=30,
                           title="Distance Distribution")
        st.plotly_chart(fig, use_container_width=True)

    # FIXED VALUE COUNTS (NO ERROR)
    col3, col4 = st.columns(2)

    with col3:
        weather_counts = df["weather"].value_counts().rename_axis("weather").reset_index(name="count")
        fig = px.bar(weather_counts, x="weather", y="count", title="Weather Distribution")
        st.plotly_chart(fig, use_container_width=True)

    with col4:
        traffic_counts = df["traffic_level"].value_counts().rename_axis("traffic_level").reset_index(name="count")
        fig = px.bar(traffic_counts, x="traffic_level", y="count", title="Traffic Distribution")
        st.plotly_chart(fig, use_container_width=True)

    st.info("👉 Operasional didominasi kondisi normal, namun variasi tetap perlu diperhatikan.")

# ===============================
# TAB 2 - BIVARIATE
# ===============================
with tab2:
    st.subheader("🔗 Bivariate Analysis")

    col1, col2 = st.columns(2)

    with col1:
        fig = px.scatter(
            df,
            x="distance_km",
            y="delivery_time_min",
            color="traffic_level",
            size="courier_experience_yrs",
            hover_data=["weather", "vehicle_type"],
            title="Distance vs Delivery Time"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.box(df, x="traffic_level", y="delivery_time_min",
                     title="Traffic Impact")
        st.plotly_chart(fig, use_container_width=True)

    st.success("""
    Insight:
    - Distance adalah faktor utama delivery time  
    - Traffic memperbesar delay secara signifikan  
    """)

    # EXTRA VISUAL
    st.subheader("🚗 Vehicle Impact")
    fig = px.box(df, x="vehicle_type", y="delivery_time_min", color="vehicle_type")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("🕒 Time of Day Impact")
    fig = px.box(df, x="time_of_day", y="delivery_time_min", color="time_of_day")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("🍳 Preparation Time Effect")
    fig = px.scatter(df, x="preparation_time_min", y="delivery_time_min",
                     color="traffic_level")
    st.plotly_chart(fig, use_container_width=True)

# ===============================
# TAB 3 - MULTIVARIATE
# ===============================
with tab3:
    st.subheader("🌐 Multivariate Analysis")

    fig = px.scatter(
        df,
        x="distance_km",
        y="delivery_time_min",
        color="traffic_level",
        facet_col="weather",
        title="Multi-factor Analysis"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.success("""
    Insight:
    - Delivery time dipengaruhi kombinasi faktor  
    - Problem bersifat multi-variable  
    """)

    # HEATMAP
    st.subheader("Correlation Heatmap")

    fig, ax = plt.subplots(figsize=(8,6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

# ===============================
# FINAL INSIGHT
# ===============================
st.markdown("## 💡 Key Business Insights")

st.success("""
1. Distance adalah faktor utama delivery time  
2. Traffic memperbesar keterlambatan secara signifikan  
3. Weather berperan sebagai faktor tambahan  
4. Kurir berpengalaman lebih efisien  
5. Problem bersifat multi-factor → cocok untuk machine learning  
""")