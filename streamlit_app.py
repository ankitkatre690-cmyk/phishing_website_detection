import streamlit as st
import joblib
import pandas as pd
import shap
import matplotlib.pyplot as plt

from src.feature_extraction import extract_features

# Load model + features
model = joblib.load("models/phishing_model.pkl")
features_list = joblib.load("models/features.pkl")

st.title("🛡️ Phishing Website Detection System")

st.write("Enter a URL to analyze")

url = st.text_input("🌐 Enter Website URL")

if st.button("🔍 Analyze URL"):

    if url:

        # Extract features
        extracted = extract_features(url)

        # Create input dataframe
        input_data = pd.DataFrame(columns=features_list)
        input_data.loc[0] = 0

        for key in extracted:
            if key in input_data.columns:
                input_data[key] = extracted[key]

        # Prediction
        prediction = model.predict(input_data)[0]
        prob = model.predict_proba(input_data)[0][1]

        if prediction == 1:
            st.error(f"🚨 Phishing Website (Confidence: {prob:.2f})")
        else:
            st.success(f"✅ Legitimate Website (Confidence: {1 - prob:.2f})")

        # 🔥 SHAP EXPLANATION
        st.subheader("🔍 Why this prediction?")

        # Create explainer
        explainer = shap.Explainer(model, input_data)
        shap_values = explainer(input_data)

        # Plot
        fig, ax = plt.subplots()
        shap.plots.waterfall(shap_values[0][:, 1], show=False)

        st.pyplot(fig)

    else:
        st.warning("⚠️ Please enter a URL")