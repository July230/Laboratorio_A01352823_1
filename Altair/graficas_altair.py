# pip install streamplit

import streamlit as st
import altair as alt
import pandas as pd
import seaborn as sns
import plotly.express as px

df = sns.load_dataset('penguins')

st.title('Gráficas con Altair')
st.write('Este es el primer párrafo de mi aplicativo web con streamlit')
st.write('Este es el segundo párrafo de mi aplicativo web con streamlit')
st.table(df.sample(10))

bar = alt.Chart(df).mark_bar().encode(
    x='count()',
    y='species:N',
    color='species'
)

st.altair_chart(bar)
#streamlit run archivi.py
#python3 -m streamlit run archivo.py

st.subheader("Gráfica con Plotly Express")
plot_chart = px.strip(df, x='species', y='bill_depth_mm',
                      color='species')
st.plotly_chart(plot_chart)

st.write('Conclusiones')
st.balloons()