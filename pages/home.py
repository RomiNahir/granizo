import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from app import app


layout = dbc.Row(
        dbc.Col(
            [   html.H5('Bienvenidos a "Climatología de granizo en Argentina"'),
                html.Br(),

                html.H6('En esta plataforma encontrarán mapas e información relacionada con el granizo en Argentina'),
                html.Br(),
            ],
            width=6
        )
    )
