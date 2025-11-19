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
    height=200
)
graf1 = graf1.interactive()

df_ordenado = df.sort_values(by='Happiness Rank')
paises_mas_felices = df_ordenado.head(10)
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
    height=200
)

intervalo = alt.selection_interval()
graf7 = alt.Chart(df).mark_point().encode(
    x='Health (Life Expectancy):Q',
    y='Economy (GDP per Capita):Q',
    color=alt.Color('Region:N',
                    scale=alt.Scale(range=gama_triada_naranja)),
    tooltip=['Country']
).properties(
    title='Espectativa de vida vs PIB',
    width=400,
    height=300
)
graf7 = graf7.add_params(intervalo)

graf8 = alt.Chart(df).mark_point().encode(
    x='Health (Life Expectancy):Q',
    y='Economy (GDP per Capita):Q',
    color=alt.Color('Region:N',
                    scale=alt.Scale(range=gama_triada_naranja)),
    tooltip=['Country']
).properties(
    title='Espectativa de vida vs PIB (Área seleccionada)',
    width=400,
    height=300
)
graf8 = graf8.transform_filter(intervalo)

click = alt.selection_point(encodings=['color'])
graf9 = alt.Chart(df).mark_bar().encode(
    x='Region:N',
    y='Happiness Score:Q',
    color=alt.condition(click, alt.Color('Region:N', scale=alt.Scale(range=gama_triada_naranja)), alt.value('#229bf3'))
).properties(
    title='Felicidad por región',
    width=800,
    height=150
)
graf9 = graf9.add_params(click)

graf10 = alt.Chart(df).mark_bar().encode(
    x='Happiness Score:Q',
    y='Country:N',
    color='Region',
    tooltip=['Country', 'Happiness Score']
).properties(
    title='Felicidad por país',
    width=800,
    height=300
)
graf10 = graf10.transform_filter(click)

parte1 = (graf1 | graf4).resolve_scale(
    x='independent',
    y='independent',
    color='independent'
)
parte2 = graf7 | graf8
st.altair_chart(parte1)
st.altair_chart(parte2)
st.altair_chart(graf9 & graf10)

st.subheader('Conclusiones')
st.write('¿Cuál es la importancia de una buena elección de color para la representación de datos?')
st.write('')
st.write('''La importancia radica en que el color influye directamente en una primera impresión. Asociamos los colores a cosas, por ejemplo: Verde para algo bueno y rojo para algo malo.''')
st.write('''En este caso, usamos colores que respetaban cierta identidad, la empresa FedEx, tomando los colores principales del logo y usando diferentes esquemas.''')
st.write('''Si la paleta de colores fuera diferente o incoherente con la identidad de la empresa o aplicación, sería extraño.''')
st.write('')
st.write('¿Altair es una buena librería para realizar gráficas? Comenta ventajas y desventajas')
st.write('''Altair es buena, especialmente para crear gráficos interactivos y transformaciones como el caso de gráficas donde se puede seleccionar una columna y que se vea reflejado en la gráfica secundaria.''')
st.write('''Sin embargo, una de las desventajas es en cuanto el orden. Incluso si usas un dataframe ordenado, altair usa su propio orden, por lo que es necesario volverlos a ordenar desde altair. 
         Adicionalmente, los colores también se tienen que sincronizar para que sean acordes al orden, lo que implica indicar muchas veces el orden a seguir cuando otras librerías lo hacen con una sola sentencia.''')
st.write('''Otra desventaja es la sintaxis, la cual resulta algo extraña tomando en cuenta que hemos trabajado con librerías como pandas, matplotlib, seaborn las cuales siguen una sintaxis similar entre sí.''')
st.write('''Además, es necesario tener cuidad al momento de unir gráficas con | y &, pues estas pueden romperse si se trabaja con interacciones.''')