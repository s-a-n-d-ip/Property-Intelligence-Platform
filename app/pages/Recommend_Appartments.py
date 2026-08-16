import streamlit as st
import pickle
import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"

@st.cache_resource
def load_artifacts():
    with open(ARTIFACTS_DIR / "location_df.pkl", "rb") as f:
        location_df = pickle.load(f)
    with open(ARTIFACTS_DIR / "cosine_sim1.pkl", "rb") as f:
        cosine_sim1 = pickle.load(f)
    with open(ARTIFACTS_DIR / "cosine_sim2.pkl", "rb") as f:
        cosine_sim2 = pickle.load(f)
    with open(ARTIFACTS_DIR / "cosine_sim3.pkl", "rb") as f:
        cosine_sim3 = pickle.load(f)
    return location_df, cosine_sim1, cosine_sim2, cosine_sim3

location_df, cosine_sim1, cosine_sim2, cosine_sim3 = load_artifacts()

def recommend_properties_with_scores(property_name, top_n=5):
    cosine_sim_matrix = 30 * cosine_sim1 + 20 * cosine_sim2 + 8 * cosine_sim3
    property_index = location_df.index.get_loc(property_name)
    sim_scores = list(enumerate(cosine_sim_matrix[property_index]))
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_scores = sorted_scores[1:top_n + 1]
    top_indices = [item[0] for item in top_scores]
    similarity_scores = [item[1] for item in top_scores]
    top_properties = location_df.index[top_indices].tolist()
    recommendations_df = pd.DataFrame({
        "PropertyName": top_properties,
        "SimilarityScore": similarity_scores
    })
    return recommendations_df

st.set_page_config(page_title="Recommend Apartments")

if "show_apartments" not in st.session_state:
    st.session_state.show_apartments = False

st.title("Select Location and Radius to Recommend Apartments")

location = st.selectbox("Select Location", location_df.columns.tolist())
radius = st.number_input("Enter Radius in KMs", min_value=1, step=1)

st.write("You selected:", location, "with a radius of", radius, "KMS")

if st.button("Recommend Apartments"):
    st.session_state.show_apartments = True

if st.session_state.show_apartments:
    result = location_df[location_df[location] < radius * 1000][location].sort_values()

    if result.empty:
        st.warning("No apartments found within this radius.")
    else:
        st.subheader("Apartments Within Selected Radius")

        selected_apartment = st.radio("Select an apartment", result.index.tolist())

        distance = result[selected_apartment]

        st.write(f"📍 **{selected_apartment}** is **{distance / 1000:.2f} KMs** away.")

        if st.button("Show Recommendations", key="show_recommendations"):
            st.subheader(f"Recommendations for {selected_apartment}")

            recommendation_df = recommend_properties_with_scores(selected_apartment, top_n=5)

            st.dataframe(recommendation_df, use_container_width=True, hide_index=True)