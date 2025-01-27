MOVIE BOX-OFFICE PREDICTION:

> This project is designed to predict the box office collection of movies based on various features such as title, genre, actor, director, and more. 
> By leveraging the power of neural networks, the project aims to provide an accurate prediction of a movie's revenue.


FEATURES:

> The dataset used in this project includes the following columns:
Movie Title          : Name of the movie.
Genres               : Categories like Action, Comedy, Drama, etc.
Actor                : Lead actor in the movie.
Director             : Director of the movie.
Year                 : Year of release.
Previous Collection  : Revenue collected by the previous movie(s) of the actor/director.
Hype Factor          : Factors influencing the movie’s hype such as Star Actor, Trailer Views, Director's Reputation, Song Popularity.


COMPONENTS:

> This repository contains the following files:

1) Movie_BoxOffice_Prediction.ipynb:
> Jupyter Notebook that includes the implementation of the neural network model.
> Preprocessing of the dataset, model training, and evaluation.

2) front_end.py:
> Streamlit-based front-end application for user interaction.
> Allows users to input movie details and get revenue predictions.


HOW IT WORKS:

1) Data Preprocessing:
> The dataset is cleaned and transformed to fit the model's requirements.
> Categorical variables are encoded, and numerical values are scaled.

2) Neural Network Model:
> The model is built using TensorFlow/Keras with Mean Squared Error as the loss function.
> Optimized to minimize prediction errors on the validation set.

3) Prediction Interface:
> A user-friendly interface built with Streamlit.
> Users can input movie details and instantly see the predicted box office collection.



HOW TO RUN:

Prerequisites:
> Python 3.8+
> Required libraries: tensorflow, pandas, numpy, joblib, streamlit



SCOPE OF THIS PROJECT:

> Integration of additional features such as runtime, production budget, and release month.
> Experimenting with other machine learning models for performance comparison.
> Deployment on cloud platforms like AWS or Heroku for public access.



> IF YOU FIND THIS PROJECT USEFUL,FEEL FREE TO STAR THIS REPSITORY AND SHARE YOUR FEEDBACK!
