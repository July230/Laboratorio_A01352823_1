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