# pip install streamplit

import streamlit as st
import altair as alt
import pandas as pd
import seaborn as sns

df = sns.load_dataset('penguins')

st.title('Gráficas con Altair')
st.write('Este es el primer párrafo de mi aplicativo web con streamlit')
st.write('Este es el segundo párrafo de mi aplicativo web con streamlit')
st.table(df.sample(10))