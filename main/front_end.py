import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.losses import MeanSquaredError
import joblib

@st.cache_resource
def load_revenue_model():
    return load_model("D:/Mini projects/Movie Box Office Prediction/main/model/movie_revenue_model.h5", custom_objects={'mse': MeanSquaredError()})

@st.cache_resource
def load_preprocessor():
    return joblib.load('D:/Mini projects/Movie Box Office Prediction/main/model/preprocessor.pkl')
model = load_revenue_model()
preprocessor = load_preprocessor()

st.title("Movie Revenue Prediction")
st.image("D:/Mini projects/Movie Box Office Prediction/image/Movie_BoxOffice_Prediction_AI_generated_Image.webp", use_column_width=True)

st.write("Predict the box office collection for an upcoming movie based on its features.")

movie_title = st.text_input("Movie Title")
genres = st.multiselect("Genre", [
"Action", "Comedy", "Drama", "Horror", "Thriller",
"Romance", "Adventure", "Crime", "Animation", "Biography"
])

director = st.text_input("Director")
actor = st.text_input("Actor")
year = st.number_input("Year", min_value=2010, max_value=2040, step=1)
previous_collection = st.number_input("Previous_Collection", step=1.0)
hype_factor = st.selectbox("Hype Factor",["Star Actor","Trailer Views","Director's Reputation","Song Popularity"
])

if st.button("Predict Revenue"):
    input_data = pd.DataFrame({
        'Genre': [', '.join(genres)],
        'Director': [director],
        'Actor': [actor],
        'Year': [year],
        'Previous_Collection': [previous_collection],
        'Hype Factor': [hype_factor]
    })
    try:
        processed_data = preprocessor.transform(input_data)
        revenue_prediction = model.predict(processed_data)
        st.markdown(
            f"<h2>Prediction for: {movie_title}</h2>" if movie_title else "<h2>Prediction Results:</h2>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<h3 style='font-size: 2em;'>Predicted Box Office Collection: Rs. {revenue_prediction[0][0]:,.2f} crores</h3>",
            unsafe_allow_html=True
        )
    except Exception as e:
        st.error("Error in prediction. Please ensure all required fields are filled correctly.")
        st.error(f"Error details: {str(e)}")