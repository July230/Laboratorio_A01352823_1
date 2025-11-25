import pickle
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

st.set_page_config(layout='wide')
st.title('Demo del modelo para penguins')
st.write('Esta app nos permite generar predicciones de especies de pinguinos')

# Procedemos a cargar el modelo guardado como pickle
with open('random_forest_classifier.pickle', 'rb') as rf_pickle:
    rfc = pickle.load(rf_pickle)
    rf_pickle.close()

with open('output_penguins.pickle', 'rb') as map_pickle:
    unique_penguin_mapping = pickle.load(map_pickle)
    map_pickle.close()

with st.form('user_input'):
    island = st.selectbox('Penguin Island', options=['Torgersen', 'Biscoe', 'Dream'])
    sex = st.selectbox('Sex', options=['Male', 'Female'])
    bill_length_mm = st.number_input('Bill lenght (mm)', min_value=0)
    bill_depth_mm = st.number_input('Bill depth (mm)', min_value=0)
    flipper_length_mm = st.number_input('Flipper length (mm)', min_value=0)
    body_mass_g = st.number_input('Body mass (g)', min_value=0)
    st.form_submit_button()

# codificar inputs
island_torgersen, island_biscoe, island_dream = 0, 0, 0
if island == 'Torgersen':
    island_torgersen = 1
if island == 'Biscoe':
    island_biscoe = 1
if island == 'Dream':
    island_dream = 1

sex_female, sex_male = 0, 0
if sex == 'Female':
    sex_female = 1
if sex == 'Male':
    sex_male = 1
