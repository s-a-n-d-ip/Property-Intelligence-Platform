import pickle
from pathlib import Path
import numpy as np
import pandas as pd
import os


class HousePricePredictionApp:

    def __init__(self):

        # Project root
        BASE_DIR = Path(__file__).resolve().parent.parent

        # Model location
        MODEL_PATH = BASE_DIR / "artifacts" / "final_pipeline.pkl"

        print("Loading model from:")
        print(MODEL_PATH)

        # Load pipeline
        with open(MODEL_PATH, "rb") as f:
            self.model = pickle.load(f)


    # USER INPUT
    def get_user_input(self):

        print("\n--- Enter Property Details ---\n")

        data = {}

        # Bedrooms
        while True:
            try:
                data["bedRoom"] = int(
                    input("Bedrooms: ")
                )

                if data["bedRoom"] > 0:
                    break

                print("❌ Bedrooms must be greater than 0.")

            except ValueError:
                print("❌ Please enter a valid number.")

        # Bathrooms

        while True:
            try:
                data["bathroom"] = int(
                    input("Bathrooms: ")
                )

                if data["bathroom"] > 0:
                    break

                print("❌ Bathrooms must be greater than 0.")

            except ValueError:
                print("❌ Please enter a valid number.")

        # Built-up Area

        while True:
            try:
                data["built_up_area"] = float(
                    input("Built-up Area (sq.ft): ")
                )

                if data["built_up_area"] > 0:
                    break

                print("❌ Area must be greater than 0.")

            except ValueError:
                print("❌ Please enter a valid area.")


        # Servant Room
        while True:

            servant_room = input(
                "Servant Room (0 = No, 1 = Yes): "
            ).strip()

            if servant_room in ["0", "1"]:
                data["servant room"] = int(servant_room)
                break

            print("❌ Please enter 0 or 1.")

        # Store Room

        while True:

            store_room = input(
                "Store Room (0 = No, 1 = Yes): "
            ).strip()

            if store_room in ["0", "1"]:
                data["store room"] = int(store_room)
                break

            print("❌ Please enter 0 or 1.")

        # Property Type

        while True:

            property_type = input(
                "Property Type (flat/house): "
            ).lower().strip()

            if property_type in [
                "flat",
                "house"
            ]:
                data["property_type"] = property_type
                break

            print(
                "❌ Invalid property type."
                " Choose flat or house."
            )

        # Sector

        while True:

            sector = input(
                "Sector Number: "
            ).strip()

            if sector.isdigit():

                data["sector"] = "sector " + sector
                break

            print(
                "❌ Enter only the sector number."
                " Example: 92"
            )

        # Balcony
        while True:

            balcony = input(
                "Balcony (0/1/2/3/3+): "
            ).strip()

            if balcony in [
                "0",
                "1",
                "2",
                "3",
                "3+"
            ]:
                data["balcony"] = balcony
                break

            print(
                "❌ Choose 0, 1, 2, 3 or 3+."
            )

        # Age Possession
        age_mapping = {
            "new": "New Property",
            "relatively new": "Relatively New",
            "moderately old": "Moderately Old",
            "old": "Old Property"
        }

        while True:

            age = input(
                "Age "
                "(new/relatively new/moderately old/old): "
            ).lower().strip()

            if age in age_mapping:

                data["agePossession"] = age_mapping[age]
                break

            print(
                "❌ Invalid age category."
            )

        # Furnishing

        furnishing_mapping = {
            "furnished": "furnished",
            "semi-furnished": "semi-furnished",
            "unfurnished": "unfurnished"
        }

        while True:

            furnishing = input(
                "Furnishing "
                "(furnished/semi-furnished/unfurnished): "
            ).lower().strip()

            if furnishing in furnishing_mapping:

                data["furnishing_type"] = (
                    furnishing_mapping[furnishing]
                )

                break

            print(
                "❌ Invalid furnishing type."
            )

        # Luxury Category

        luxury_mapping = {
            "low": "Low",
            "medium": "Medium",
            "high": "High"
        }

        while True:

            luxury = input(
                "Luxury Category "
                "(low/medium/high): "
            ).lower().strip()

            if luxury in luxury_mapping:

                data["luxury_category"] = (
                    luxury_mapping[luxury]
                )

                break

            print(
                "❌ Invalid luxury category."
            )

        # Floor Category
        floor_mapping = {
            "low": "Low Floor",
            "mid": "Mid Floor",
            "high": "High Floor"
        }

        while True:

            floor = input(
                "Floor Category "
                "(low/mid/high): "
            ).lower().strip()

            if floor in floor_mapping:

                data["floor_category"] = (
                    floor_mapping[floor]
                )

                break

            print(
                "❌ Invalid floor category."
            )


        applicant_df = pd.DataFrame([data])

        return applicant_df


    # PREDICTION
    def predict_price(self, applicant_df):

        # Model predicts log(price)
        log_price_pred = self.model.predict(
            applicant_df
        )

        # Convert log prediction back to original price
        price_pred = np.expm1(
            log_price_pred
        )

        return float(price_pred[0])


    # RUN APPLICATION
    def run(self):

        applicant_df = self.get_user_input()

        print("\n------ INPUT SENT TO MODEL ------")
        print(applicant_df)

        result = self.predict_price(
            applicant_df
        )

        print("\n------ RESULT ------")

        print(
            f"Predicted House Price: ₹{result:.2f} Crore"
        )

        print("\n---------------------\n")

        return result

# MAIN

if __name__ == "__main__":

    house_price_application = HousePricePredictionApp()

    house_price_application.run()