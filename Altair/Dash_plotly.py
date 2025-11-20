from dash import Dash, dcc, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# Incorporar datos a la app
df = pd.read_csv('../../2016-1.csv')

# Crear aplicación de Dash
app = Dash(__name__, external_stylesheets=[dbc.themes.VAPOR])


# Componentes
# Vacío pues se modificará según componente Dropdown
mytitle = dcc.Markdown(children='# Título del gráfico')
graf = dcc.Graph(figure={})
menu = dcc.Dropdown(options=['Bar Plot', 'Scatter Plot', '3D Scatter Plot'],
                    value='Bar Plot',
                    clearable=False) # el usuario no puede borrar el valor
titulo_menu = dcc.Markdown(children='Seleccione el tipo de gráfico')

# Personalizar el layout
app.layout = dbc.Container([mytitle, graf, titulo_menu, menu])

# Las callback functions permiten interactividad
@app.callback(
        Output(graf, component_property='figure'),
        Output(mytitle, component_property='children'),
        Input(menu, component_property='value')
)
def update_graph(user_input):
    if user_input == 'Bar Plot':
        fig_plotly = px.bar(df, x='Country', 
                            y='Happiness Score', 
                            color='Region')
        titulo = 'Gráfica de barras'
    elif user_input == 'Scatter Plot':
        fig_plotly = px.scatter(df, x='Happiness Score', 
                                y='Economy (GDP per Capita)', 
                                color='Region')
        titulo = 'Gráfica de dispersión'
    elif user_input == '3D Scatter Plot':
        fig_plotly = px.scatter_3d(df, x='Happiness Score', 
                                y='Economy (GDP per Capita)', 
                                z='Health (Life Expectancy)',
                                color='Region', size='Health (Life Expectancy)')
        titulo = 'Gráfica de dispersión en 3D'
    return fig_plotly, '# ' + titulo

# Iniciar app
if __name__ == '__main__':
    app.run()