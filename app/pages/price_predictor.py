import streamlit as st
import pandas as pd

from house_price_app import HousePricePredictionApp


st.set_page_config(
    page_title=" Property Price Predictor",
    page_icon="🏠"
)


st.title("🏠 Property Price Prediction")

st.write(
    "Enter property details to estimate the property price."
)

@st.cache_resource
def load_model():

    return HousePricePredictionApp()


model = load_model()


# =========================================================
# PROPERTY DETAILS
# =========================================================

property_type = st.selectbox(
    "Property Type",
    ["flat", "house"]
)


sector = st.text_input(
    "Sector",
    placeholder="Example: sector 92"
)


bedRoom = st.number_input(
    "Number of Bedrooms",
    min_value=1,
    step=1
)


bathroom = st.number_input(
    "Number of Bathrooms",
    min_value=1,
    step=1
)


balcony = st.selectbox(
    "Number of Balconies",
    ["0", "1", "2", "3", "3+"]
)


agePossession = st.selectbox(
    "Property Age",
    [
        "New Property",
        "Relatively New",
        "Moderately Old",
        "Old Property"
    ]
)


built_up_area = st.number_input(
    "Built-up Area (sq.ft)",
    min_value=1.0,
    step=100.0
)


servant_room = st.selectbox(
    "Servant Room",
    [0, 1]
)


store_room = st.selectbox(
    "Store Room",
    [0, 1]
)


furnishing_type = st.selectbox(
    "Furnishing Type",
    [
        "furnished",
        "semi-furnished",
        "unfurnished"
    ]
)


luxury_category = st.selectbox(
    "Luxury Category",
    [
        "Low",
        "Medium",
        "High"
    ]
)


floor_category = st.selectbox(
    "Floor Category",
    [
        "Low Floor",
        "Mid Floor",
        "High Floor"
    ]
)


# =========================================================
# PREDICTION
# =========================================================

if st.button("Predict Price"):

    data = {

        "bedRoom": bedRoom,

        "bathroom": bathroom,

        "built_up_area": built_up_area,

        "servant room": servant_room,

        "store room": store_room,

        "property_type": property_type,

        "sector": sector.strip().lower(),

        "balcony": balcony,

        "agePossession": agePossession,

        "furnishing_type": furnishing_type,

        "luxury_category": luxury_category,

        "floor_category": floor_category
    }


    applicant_df = pd.DataFrame([data])


    # =====================================================
    # PREDICTION THROUGH PYTHON CLASS
    # =====================================================

    try:

        result = model.predict_price(
            applicant_df
        )


        st.success(
            "Prediction Successful"
        )


        st.metric(
            "Estimated Property Price",
            f"₹{result:.2f} Crore"
        )


    except Exception as e:

        st.error(
            f"Prediction failed: {e}"
        )

