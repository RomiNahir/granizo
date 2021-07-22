import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
from app import app

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H2("Sobre esta página", className="text-center")
                    , className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(html.H6(children='El granizo es un fenómeno meteorológico que provoca importantes consecuencias '
                                        'por lo que el estudio del mismo es de gran interés. En esta plataforma '
                                        'encontrarán información procesada de datos de eventos de granizo '
                                        'suministrada por el Servicio Meteorológico Nacional (SMN) y el Instituto Nacional '
                                        'de Tecnología Agropecuaria (INTA). Los resultados se basan en lo encontrado en la tesis '
                                        'de licenciatura en ciencias de la atmósfera de Romina Mezher.', className='text-justify')
                    ,className="mb-4")
            ]),
        dbc.Row([
            dbc.Col(html.H4(children='Enlaces de interés', className='text-justify')
                    ,className="mb-4")
            ]),
        dbc.Row([
            dbc.Col(html.H6(children='Climatología de granizo en Argentina', className='text-justify')
                    ,className="mb-2")
            ]),
            html.Button("Tesis", id="btnTesis"), dcc.Download(id="download-pdf")
    ])
])

@app.callback(
    Output("download-pdf", "data"),
    Input("btnTesis", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file(
        "./assets/tesis_licenciatura_mezher.pdf"
    )
