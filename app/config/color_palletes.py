'''
Paletas de colores personalizadas para las gráficas de la app.

Contiene diferentes paletas de colores predefinidas que pueden ser 
usadas en plotly para mantener consistencia visual en el dashboard.
'''

# Paleta por defecto (Plotly estándar)
DEFAULT = [
    '#636EFA',  # Azul
    '#EF553B',  # Rojo
    '#00CC96',  # Verde
    '#AB63FA',  # Púrpura
    '#FFA15A',  # Naranja
    '#19D3F3',  # Cian
    '#FF6692',  # Rosa
    '#B6E880',  # Verde lima
    '#FF97FF',  # Magenta
    '#FECB52',  # Amarillo
]

MONOCROMATICO = [
    '#517423',  # Verde oscuro
]

ANALOGO = [
    '#517423', 
    '#CBD546', 
    '#A6BF42', 
    '#90A836', 
    '#9DA889', 
    '#31391C'
]

TRIADICO = [
    '#517423', 
    '#235174', 
    '#742351'
]

COMPLEMENTARIOS = [
    '#517423', 
    '#237456', 
    '#742371'
]

def get_palette(name: str = 'DEFAULT'):
    '''
    Retorna una paleta de colores por nombre.
    
    Parameters
    ----------
    name : str
        Nombre de la paleta. Opciones: 'MONOCROMATICO', 'ANALOGO', 'TRIADICO', 
        'COMPLEMENTARIO', 'DEFAULT'.
        
    Returns
    -------
    list
        Lista de colores en formato hex.
    '''
    palettes = {
        'DEFAULT': DEFAULT,
        'MONOCROMATICO': MONOCROMATICO,
        'ANALOGO': ANALOGO,
        'TRIADICO': TRIADICO,
        'COMPLEMENTARIOS': COMPLEMENTARIOS,
    }
    return palettes.get(name, DEFAULT)