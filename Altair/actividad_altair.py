import pandas as pd
import altair as alt
import streamlit as st

# Gama de colores triada a partir del naranja
gama_triada_naranja = ['#F37A22',
                       '#E29A00',
                       '#C6B700',
                       '#A0D120',
                       '#64E85C',
                       '#00EA9C',
                       '#00D1EB',
                       '#00B1FF',
                       '#0083FF',
                       '#7A22F3']
complementario_naranja = '#229bf3'
naranja_triada = ['#f37a22', '#22f37a', '#7a22f3']
morado_triada = ['#462e92', '#92462e', '#2e9246']

st.write('Actividad - Altair y streamlit')
st.write('Ian Julián Estrada Castro')

df = pd.read_csv('../2016-1.csv')
df.info()
df

graf1 = alt.Chart(df).mark_point().encode(
    x='Happiness Score:Q',
    y='Economy (GDP per Capita):Q',
    color=alt.Color('Region:N',
                    scale=alt.Scale(range=gama_triada_naranja)),
    tooltip=['Country']
).properties(
    title='Felicidad vs PIB',
    width=400,
    height=400
).interactive()

graf1