import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.house_price_app import HousePricePredictionApp


app = FastAPI(
    title="House Price Prediction API",
    description="ML API for predicting residential property prices.",
    version="1.0.0"
)


# Load model once when API starts
model = HousePricePredictionApp()


class PropertyData(BaseModel):

    bedRoom: int
    bathroom: int
    built_up_area: float

    servant_room: int
    store_room: int

    property_type: str
    sector: str
    balcony: str

    agePossession: str
    furnishing_type: str
    luxury_category: str
    floor_category: str


@app.get("/")
def home():
    return {
        "message": "House Price Prediction API is running"
    }


@app.post("/predict")
def predict_price(data: PropertyData):

    try:

        # Convert API input into the format
        # expected by the ML pipeline

        applicant_df = data.model_dump()

        # Rename API-friendly fields to model column names
        applicant_df["servant room"] = applicant_df.pop(
            "servant_room"
        )

        applicant_df["store room"] = applicant_df.pop(
            "store_room"
        )

        applicant_df = pd.DataFrame([applicant_df])

        prediction = model.predict_price(applicant_df)

        return {
            "status": "success",
            "predicted_price_crore": prediction
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
