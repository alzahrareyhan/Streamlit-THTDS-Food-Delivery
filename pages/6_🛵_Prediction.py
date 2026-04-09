import streamlit as st
import pandas as pd
import joblib

# ===============================
# CONFIG
# ===============================
st.set_page_config(page_title="Modelling & Prediction", layout="wide")
st.title("🛵 Delivery Time Prediction")
st.markdown("---")

# ===============================
# LOAD MODEL
# ===============================
model = joblib.load("data/best_lr_model.joblib")

# ===============================
# FORM INPUT
# ===============================
st.subheader("🔮 Input Data")

col1, col2, col3 = st.columns(3)

with col1:
    traffic_level = st.selectbox("🚦 Traffic Level", ["Low", "Medium", "High"])
    courier_experience_category = st.selectbox("👨‍✈️ Experience Category", ["Beginner", "Intermediate", "Expert"])
    weather = st.selectbox("🌤️ Weather", ['Clear', 'Rainy', 'Snowy', 'Windy', 'Foggy'])

with col2:
    time_of_day = st.selectbox("⏰ Time of Day", ['Evening', 'Afternoon', 'Morning', 'Night'])
    vehicle_type = st.selectbox("🚗 Vehicle Type", ['Scooter', 'Bike', 'Car', 'Motorcycle'])
    distance_km = st.number_input("📍 Distance (km)", 0.1, 50.0, 7.5)

with col3:
    preparation_time_min = st.number_input("🍳 Preparation Time (min)", 1, 120, 15)
    courier_experience_yrs = st.number_input("📆 Experience (yrs)", 0, 20, 5)

distance_per_experience = distance_km / (courier_experience_yrs + 1)

# ===============================
# PREDICTION
# ===============================
st.markdown("---")

if st.button("🚀 Predict Delivery Time", use_container_width=True):

    input_data = pd.DataFrame([{
        "traffic_level": traffic_level,
        "courier_experience_category": courier_experience_category,
        "weather": weather,
        "time_of_day": time_of_day,
        "vehicle_type": vehicle_type,
        "distance_km": distance_km,
        "preparation_time_min": preparation_time_min,
        "courier_experience_yrs": courier_experience_yrs,
        "distance_per_experience": distance_per_experience
    }])

    input_data = input_data[model.feature_names_in_]
    prediction = model.predict(input_data)[0]

    # ===============================
    # BASELINE
    # ===============================
    avg_time = 30
    diff = prediction - avg_time

    # ===============================
    # RESULT METRICS (CLEAN)
    # ===============================
    st.markdown("### 📦 Prediction Result")

    col1, col2, col3 = st.columns(3)

    col1.metric("Estimated Time", f"{prediction:.2f} min")
    col2.metric("Difference vs Avg", f"{diff:+.2f} min")
    col3.metric("Distance", f"{distance_km:.1f} km")

    # ===============================
    # PROGRESS BAR
    # ===============================
    st.markdown("### 🚚 Delivery Performance")

    progress = min(prediction / 60, 1.0)
    st.progress(progress)
    st.caption("Relative to 60 min benchmark")

    # ===============================
    # BENCHMARK CHART
    # ===============================
    st.markdown("### 📊 Comparison")

    benchmark_df = pd.DataFrame({
        "Type": ["Prediction", "Average"],
        "Time (min)": [prediction, avg_time]
    })

    st.bar_chart(benchmark_df.set_index("Type"))

    # ===============================
    # CATEGORY
    # ===============================
    st.markdown("### 🚦 Delivery Category")

    if prediction <= 20:
        st.info("Fast Delivery")
    elif prediction <= 40:
        st.info("Normal Delivery")
    else:
        st.info("Slow Delivery")

    # ===============================
    # INSIGHT
    # ===============================
    st.markdown("### 🧠 Insight")

    insights = []

    if distance_km > 10:
        insights.append("Long distance significantly increases delivery time")

    if traffic_level == "High":
        insights.append("High traffic contributes to delay")

    if preparation_time_min > 30:
        insights.append("Long preparation time impacts delivery")

    if courier_experience_category == "Beginner":
        insights.append("Less experienced courier may reduce efficiency")

    if insights:
        for i in insights:
            st.write("- " + i)
    else:
        st.write("No significant risk factors detected")

    # ===============================
    # RECOMMENDATION
    # ===============================
    st.markdown("### 💡 Recommendation")

    if prediction > 40:
        st.warning("""
        - Assign closer driver  
        - Use experienced courier  
        - Optimize preparation time  
        """)

    elif prediction > 25:
        st.info("""
        - Monitor traffic  
        - Optimize dispatch timing  
        """)

    else:
        st.success("Delivery performance is optimal")

    # ===============================
    # INPUT SUMMARY
    # ===============================
    st.markdown("### 📊 Input Summary")
    st.dataframe(input_data)
    # ===============================
# FEATURE IMPORTANCE
# ===============================
import plotly.express as px

st.markdown("### 📊 Feature Importance")

try:
    # -------------------------------
    # AMBIL MODEL & PREPROCESSOR
    # -------------------------------
    # auto-detect step terakhir
    model_step = list(model.named_steps.values())[-1]

    # cari preprocessor (biasanya step pertama)
    preprocessor = None
    for name, step in model.named_steps.items():
        if "preprocess" in name.lower() or "transform" in name.lower():
            preprocessor = step

    # -------------------------------
    # GET FEATURE NAMES
    # -------------------------------
    if preprocessor is not None:
        try:
            feature_names = preprocessor.get_feature_names_out()
        except:
            feature_names = model.feature_names_in_
    else:
        feature_names = model.feature_names_in_

    # -------------------------------
    # GET IMPORTANCE
    # -------------------------------
    if hasattr(model_step, "feature_importances_"):
        importance = model_step.feature_importances_

    elif hasattr(model_step, "coef_"):
        importance = model_step.coef_

    else:
        st.warning("Model tidak mendukung feature importance")
        importance = None

    # -------------------------------
    # BUILD DATAFRAME
    # -------------------------------
    if importance is not None:
        feat_imp = pd.DataFrame({
            "feature": feature_names,
            "importance": importance
        })

        # ambil absolute (biar LR kebaca jelas)
        feat_imp["importance"] = feat_imp["importance"].abs()

        feat_imp = feat_imp.sort_values(by="importance", ascending=False)

        # -------------------------------
        # PLOT TOP N
        # -------------------------------
        top_n = 10

        fig = px.bar(
            feat_imp.head(top_n),
            x="importance",
            y="feature",
            orientation="h",
            title="Top Features Influencing Delivery Time"
        )

        fig.update_layout(yaxis=dict(autorange="reversed"))

        st.plotly_chart(fig, use_container_width=True)

        # -------------------------------
        # INSIGHT
        # -------------------------------
        top_feature = feat_imp.iloc[0]["feature"]

        st.success(f"""
        🔍 Feature paling berpengaruh: **{top_feature}**
        
        Artinya, variabel ini memiliki kontribusi terbesar terhadap prediksi waktu pengiriman.
        """)

        # -------------------------------
        # OPTIONAL: TABEL DETAIL
        # -------------------------------
        with st.expander("📋 Detail Feature Importance"):
            st.dataframe(feat_imp)

except Exception as e:
    st.error("Gagal menampilkan feature importance")
    st.write(e)