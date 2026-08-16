import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="Property Analytics"
)

st.title("Analytics")

# Project root
BASE_DIR = Path(__file__).resolve().parents[2]

ARTIFACTS_DIR = BASE_DIR / "artifacts"

with open(ARTIFACTS_DIR / "data_viz1.pkl", "rb") as f:
    new_df = pickle.load(f)

with open(ARTIFACTS_DIR / "WordCloud_feature_text.pkl", "rb") as f:
    feature_text = pickle.load(f)

group_df = (
    new_df
    .groupby('sector')[[
        'price',
        'price_per_sqft',
        'built_up_area',
        'latitude',
        'longitude'
    ]]
    .mean()
)


st.header("Sector Price per Sqft Geomap")

fig = px.scatter_mapbox(
    group_df,
    lat="latitude",
    lon="longitude",
    color="price_per_sqft",
    size="built_up_area",
    color_continuous_scale=px.colors.cyclical.IceFire,
    zoom=10,
    mapbox_style="open-street-map",
    height=700,
    hover_name=group_df.index
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.header("Features Wordcloud")

wordcloud = WordCloud(
    width=800,
    height=800,
    background_color="black",
    stopwords=set(["s"]),
    min_font_size=10
).generate(feature_text)

fig, ax = plt.subplots(figsize=(8, 8))

ax.imshow(
    wordcloud,
    interpolation="bilinear"
)

ax.axis("off")
fig.tight_layout(pad=0)

st.pyplot(fig)

plt.close(fig)

st.header("Area Vs Price")

property_type = st.selectbox(
    "Select Property Type",
    ["flat", "house"]
)

filtered_df = new_df[
    new_df["property_type"] == property_type
]

fig1 = px.scatter(
    filtered_df,
    x="built_up_area",
    y="price",
    color="bedRoom",
    title="Area Vs Price"
)

fig1.update_layout(
    plot_bgcolor="#1E1E1E",
    paper_bgcolor="#1E1E1E",
    font=dict(color="white")
)

st.plotly_chart(
    fig1,
    use_container_width=True,
    key="area_vs_price"
)

st.header('BHK Pie Chart')

sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0,'overall')

selected_sector = st.selectbox('Select Sector', sector_options)

if selected_sector == 'overall':

    fig2 = px.pie(new_df, names='bedRoom')

    st.plotly_chart(fig2, use_container_width=True)
else:

    fig2 = px.pie(new_df[new_df['sector'] == selected_sector], names='bedRoom')

    st.plotly_chart(fig2, use_container_width=True)
    
st.header('Side by Side BHK price comparison')

fig3 = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price', title='BHK Price Range')

st.plotly_chart(fig3, use_container_width=True)


st.header('Side by Side Distplot for property type')

fig3 = plt.figure(figsize=(10, 4))
sns.distplot(new_df[new_df['property_type'] == 'house']['price'],label='house')
sns.distplot(new_df[new_df['property_type'] == 'flat']['price'], label='flat')
plt.legend()
st.pyplot(fig3)