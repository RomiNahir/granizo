import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from app import app
from pages import contacto, home,anual

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Bienvenidos a la plataforma de datos de granizo de Argentina", className="text-center")
                    , className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(html.H5(children='En esta plataforma encontrarán información relacionada con datos climáticos de granizo '
                                        'en Argentina derivado de estaciones meteorológicas', className='text-center')
                    ,className="mb-4")
            ]),

        dbc.Row([
            dbc.Col(html.H5(children=''), className="mb-5")
        ]),
        dbc.Row([
            dbc.Col(dbc.Card(children=[html.H3(children='Datos de frecuencias y medias anuales',
                                               className="text-center"),
                                       dbc.Button("Ir", href="/anual",color="secondary",className="mt-3"),
                                                
                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4"),

            dbc.Col(dbc.Card(children=[html.H3(children='Datos de frecuencias mensuales (proximamente)',
                                               className="text-center"),
                                       dbc.Button("Ir",href="",color="secondary",
                                                  className="mt-3"),
                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4"),

            dbc.Col(dbc.Card(children=[html.H3(children='Más información sobre esta página',
                                               className="text-center"),
                                       dbc.Button("Ir",
                                                  href="",
                                                  color="secondary",
                                                  className="mt-3"),

                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4")
        ], className="mb-5"),
        html.P(
            [html.Span(
                    "Licencia de uso",
                    id="tooltip-target",
                    className="text-info",
                ),
            ]
        ),
        dbc.Tooltip(html.Img(src='/assets/images/license.png',className='img',style={'height':'80%', 'width':'80%'}),
            target="tooltip-target", placement="bottom"
            ),
    ])
])
