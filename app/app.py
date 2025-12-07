from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import os

app = Dash(__name__, 
           external_stylesheets=[
               dbc.themes.BOOTSTRAP,
               dbc.icons.BOOTSTRAP,
               'https://fonts.googleapis.com/css?family=MuseoModerno',
           ],
           suppress_callback_exceptions=True) # Permite callbacks en páginas no cargadas

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

# ==================== Layout Components ====================

# ======================== Sidebar ==========================
sidebar = html.Div(
    [
        html.H6('Sidebar', className='display-4', style={'font-family': 'MuseoModerno'}),
        html.Hr(),
        html.P('Navegación', className='lead', style={'font-family': 'MuseoModerno'}),
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.I(className='bi bi-house-door-fill', style={'margin-right': '0.5rem'}),
                        html.Span('Dashboard')
                    ],
                    href='/dashboard',
                    className='nav-link',
                    active='exact',
                ),
                dbc.NavLink(
                    [
                        html.I(className='bi bi-truck', style={'margin-right': '0.5rem'}),
                        html.Span('Rutas')
                    ],
                    href='/otra-pagina',
                    className='nav-link',
                    active='exact',
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

tooltip = html.Div(
    [
        html.I(
            id='tooltip-target',
            className='bi bi-info-circle-fill me-2', 
            style={'margin-right': '0.5rem'},
        ),
        dbc.Tooltip(
            'Sube un archivo haciendo click o arrastrando aquí.',
            target='tooltip-target',
            style={'font-family': 'MuseoModerno'},
        ),
    ]
)

# ======================== Pages ==========================
# Dashboard Page
dashboard_content = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1(
                'Dashboard', 
                style={'textAlign': 'left', 'font-family': 'MuseoModerno'}
            ),
            tooltip
        ],
        style={
            'display': 'flex',
            'alignItems': 'center',
            'gap': '0.5rem',
            'justifyContent': 'left',
            'width': '100%'
        }
        ),
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='plot-1', className='dashboard-graph')
                ])
            ], className='shadow-sm mb-3', style={'minHeight': '300px'})
        ], width='auto'),
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='plot-2', className='dashboard-graph')
                ])
            ], className='shadow-sm mb-3', style={'minHeight': '300px'})
        ], width='auto'),
    ]),


    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='plot-3', className='dashboard-graph')
                ])
            ], className='shadow-sm mb-3', style={'minHeight': '300px'})
        ], width='auto'),
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='plot-4', className='dashboard-graph')
                ])
            ], className='shadow-sm mb-3', style={'minHeight': '300px'})
        ], width='auto'),
    ])
])

# Other Page
other_page = dbc.Container([
    dbc.Row([
        html.Div([
            html.H1('Otra página', style={'textAlign': 'left', 'font-family': 'MuseoModerno'}),
            html.P('Contenido para otra página')
        ])
    ]),
])

content = html.Div(id='page-content', className='page-content', style=CONTENT_STYLE)

app.layout = dbc.Container([
    dcc.Location(id='url', refresh=False), # Componente para manejar la URL
    sidebar, # Barra lateral de navegación
    content # Contenedor para el contenido de la página
], fluid=True)


# ==================== Callback functions ====================
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    '''
    Actualiza el contenido de la página según la URL.

    Parameters
    ----------
    pathname : str
        Ruta actual de la URL.

    Returns
    -------
    dash.html.Div
        Contenido correspondiente a la página solicitada.
    '''
    if not pathname or pathname == '/' or pathname == '/dashboard':
        return dashboard_content
    if pathname == '/otra-pagina':
        return other_page
    return html.H1('404: Página no encontrada', style={'color': 'red'})
    
# ==================== Utility Functions ====================
def get_data_path(filename):
    '''
    Retorna la ruta absoluta hacia un archivo dentro de /data

    Parameters
    ----------
    filename : str
        Nombre del archivo dentro de la carpeta /data.
    
    Returns
    -------
    str
        Ruta absoluta hacia el archivo solicitado.
    '''
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    data_dir = os.path.join(base_dir, '..', 'data')
    return os.path.join(data_dir, filename)

# ==================== Run the app ====================
if __name__ == '__main__':
    app.run(debug=True)