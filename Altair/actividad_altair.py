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

st.title('Actividad - Altair y streamlit')
st.subheader('Ian Julián Estrada Castro')

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
st.altair_chart(graf1)
st.write('''El gráfico de dispersión la puntuación de felicidad contra el Producto Interno Bruto (PIB) de ada país. 
         La gama de colores seleccionada fue la gama triada a partir del color naranja de la empresa FedEx, utilizada en este caso para colorear los países por región.
         Aquí podemos ver que la mayoría de países de África subsahariana están por debajo de los 5.5 puntos de felicidad. 
         Esto destaca la importancia de las visualizaciones, puesto que la anterior gráfica de barras era una suma total de la región.''')

df = df.sort_values(by='Happiness Rank')
paises_mas_felices = df.head(10)
orden = list(paises_mas_felices.sort_values('Happiness Score')['Country'])

graf4 = alt.Chart(paises_mas_felices).mark_bar().encode(
    x=alt.X('Country:N', sort='y'), # ordenar de menor a mayor
    y='Happiness Score:Q',
    color=alt.Color('Country:N',
                    sort=orden,
                    scale=alt.Scale(
                        domain=orden,
                        range=gama_triada_naranja
                    )),
    tooltip=['Happiness Score'],
).properties(
    title='Países más felices',
    width=400,
    height=400
)
st.altair_chart(graf4)
st.write('''El siguiente gráfico de barras muestra la puntuación de felicidad de los 10 países más felices.
            En esta ocasión están ordenados de forma ascendente siguiendo una buena práctica para los gráficos de barras. 
            La gama de color es la misma, siguiendo el mismo patrón ascendente.''')

intervalo = alt.selection_interval()
graf7 = alt.Chart(df).mark_point().encode(
    x='Health (Life Expectancy):Q',
    y='Economy (GDP per Capita):Q',
    color=alt.Color('Region:N',
                    scale=alt.Scale(range=gama_triada_naranja)),
    tooltip=['Country']
).properties(
    title='Espectativa de vida vs PIB',
    width=300,
    height=300
).add_params(intervalo)

graf8 = alt.Chart(df).mark_point().encode(
    x='Health (Life Expectancy):Q',
    y='Economy (GDP per Capita):Q',
    color=alt.Color('Region:N',
                    scale=alt.Scale(range=gama_triada_naranja)),
    tooltip=['Country']
).properties(
    title='Espectativa de vida vs PIB',
    width=300,
    height=300
).transform_filter(intervalo)
st.altair_chart(graf7 | graf8)
st.write('''El gráfico de dispersión muestra la expectativa de vida con respecto al PIB. 
         En este caso, sí parece haber una correlación positiva, donde entre más alto sea el PIB, mayor esperanza de vida. 
         Por ejemplo, los paises correspondientes a Europa occidental se concentran en un área del gráfico.''')

click = alt.selection_point(encodings=['color'])
graf9 = alt.Chart(df).mark_bar().encode(
    x='Region:N',
    y='Happiness Score:Q',
    color=alt.condition(click, alt.Color('Region:N', scale=alt.Scale(range=gama_triada_naranja)), alt.value('#229bf3'))
).properties(
    title='Felicidad por región',
    width=500,
    height=150
).add_params(click)

graf10 = alt.Chart(df).mark_bar().encode(
    x='Happiness Score:Q',
    y='Country:N',
    color='Region',
    tooltip=['Country', 'Happiness Score']
).properties(
    title='Felicidad por país',
    width=500,
    height=300
).transform_filter(click)
st.altair_chart(graf9 & graf10)
st.write('''El gráfico de barras muestra la puntuación de felicidad por región. 
         La gama de colores seleccionada fue la gama triada a partir del color naranja de la empresa FedEx, esto debido a que este gráfico muestra categorías. 
         Las regiones con mayor puntuación son Europa central y del este, junto con África subsahariana. 
         Al seleccionar la región, podemos ver la cantidad de países y su respectiva puntuación de felicidad.''')

st.subheader('Conclusiones')