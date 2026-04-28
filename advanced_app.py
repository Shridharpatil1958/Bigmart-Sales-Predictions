import pandas as pd
import numpy as np
import joblib
import streamlit as st

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="BigMart Sales Predictor", layout="wide")

# -------------------------------
# Load Model & Scaler (Cached)
# -------------------------------
@st.cache_resource
def load_models():
    scaler = joblib.load("sc.sav")
    model = joblib.load("lr.sav")
    return scaler, model

scaler, model = load_models()

# -------------------------------
# Title & Description
# -------------------------------
st.title("🛒 BigMart Sales Prediction App")
st.markdown("Predict the sales of a product based on its features.")

# -------------------------------
# Layout (Columns)
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    Item_Weight = st.number_input("Item Weight", min_value=0.0, format="%.2f")
    Item_Visibility = st.number_input("Item Visibility", min_value=0.0, format="%.4f")
    Item_MRP = st.number_input("Item MRP", min_value=0.0, format="%.2f")

with col2:
    Outlet_Establishment_Year = st.slider("Outlet Establishment Year", 1985, 2010)
    Item_Fat_Content = st.selectbox("Item Fat Content", ["Low Fat", "Regular"])
    Outlet_Size = st.selectbox("Outlet Size", ["Small", "Medium", "High"])
    Outlet_Location_Type = st.selectbox("Outlet Location Type", ["Tier 1", "Tier 2", "Tier 3"])
    Outlet_Type = st.selectbox("Outlet Type", ["Grocery Store", "Supermarket Type1", "Supermarket Type2", "Supermarket Type3"])

# -------------------------------
# Encoding Functions
# -------------------------------
def encode_inputs():
    fat_map = {"Low Fat": 1, "Regular": 0}
    size_map = {"Small": 0, "Medium": 1, "High": 2}
    location_map = {"Tier 1": 0, "Tier 2": 1, "Tier 3": 2}
    outlet_map = {
        "Grocery Store": 0,
        "Supermarket Type1": 1,
        "Supermarket Type2": 2,
        "Supermarket Type3": 3
    }

    return [
        Item_Weight,
        fat_map[Item_Fat_Content],
        Item_Visibility,
        Item_MRP,
        Outlet_Establishment_Year,
        size_map[Outlet_Size],
        location_map[Outlet_Location_Type],
        outlet_map[Outlet_Type]
    ]

# -------------------------------
# Prediction Button
# -------------------------------
if st.button("🔍 Predict Sales"):
    try:
        features = encode_inputs()

        # Convert to numpy array
        X = np.array(features).reshape(1, -1)

        # Scale input
        X_scaled = scaler.transform(X)

        # Predict
        prediction = model.predict(X_scaled)

        # Output
        st.success(f"💰 Estimated Sales: ₹ {prediction[0]:,.2f}")

    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit")