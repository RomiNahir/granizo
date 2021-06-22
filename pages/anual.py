import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app
import plotly.express as px
import dash_table
import pandas as pd

originaldf = pd.read_csv('frecuencia.csv', 
                         sep=',', header = 0,
                         names=['ID', 'Nombre', 'Latitud', 'Longitud', 'Altura', 'Año', 'Frecuencia'])

prueba_tabla = originaldf.head()

Variables = {
    "1960-1979": "Dew Point Temperature",
    "1980-1999": "Air Temperature",
    "2000-2019": "Precipitation",
    "1960-1999": "Pressure",
    "1980-2019": "Cloud Fraction",
    "1960-2019": "Wind Direction",
}

layout = html.Div(
    children=[
        html.Div(className="row",
            children=[
                dbc.Col(
                    children=[html.Div(
                                children=[
                                    html.H3(['Frecuencia anual',dbc.Badge("info", color="info", pill = True,
                                        className="ml-2", style={'font-size': '12px'})]),
                                    dbc.Input(id="txtYearFrequency", placeholder="Elije un año...", type="number",min=1930, 
                                            max=2019, step=1,style = {'width' : '30%', 'margin-top' : '5px'}),
                                    dbc.Button("Seleccionar", id="btnFrequency", outline=True, 
                                            color="success", className="mt-3 mb-5"),
                                ]),
                              html.Div(
                                children=[    
                                    html.H3('Promedio anual por periodos'),
                                    dcc.Dropdown(id="variable-dropdown",
                                            options=[
                                                {"label": key, "value": value} for key, value in Variables.items()],
                                                    value="Air Temperature", 
                                                    style = {'font-size': '16px', 'white-space': 'nowrap', 'text-overflow': 'ellipsis'}
                                    )
                                ],style = {'width' : '90%', 'margin-top' : '5px'})
                            ],md=4),

                dbc.Col(    
                    children=[
                        dbc.Tabs(
                            [
                                dbc.Tab(dcc.Graph(id="graph"), label="Mapa", labelClassName="text-success"),
                                dbc.Tab(id='data-table', label="Tabla de Datos",
                                    labelClassName="text-success"),
                            ]),
                    ],md=8),
            ]
        )
    ]
)


# Update Map Graph
@app.callback(
    Output("graph", "figure"),
    [Input("btnFrequency","n_clicks"),
     State("txtYearFrequency","value"),
    ],
)
def update_graph(n_clicks,value):
    
    #Año seleccionado
    data = originaldf[originaldf["Año"] == value]

    data = data[["Latitud", "Longitud", "Frecuencia"]]

    fig = px.scatter_mapbox(data, lat="Latitud", lon="Longitud", color="Frecuencia",
                        color_continuous_scale=px.colors.cyclical.IceFire, 
                        range_color=[0,10],zoom=4, height=600)
    fig.update_layout(mapbox_style="open-street-map")

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.update_layout(coloraxis_colorbar=dict(thickness=30,
                           ticklen=1, tickcolor='black',tickvals = [0,1,2,3,4,5,6,7,8,9,10],
                           tickfont=dict(size=15, color='black')))

    fig.update_traces(marker=dict(size=14))

    returnedToast = dbc.Toast([html.P("Search Cleared")], header=("Success"), icon="success", dismissable=True, style={
            "position": "fixed", "top": 66, "right": 20, "width": 350, "background-color": "green", "color": "white"})

    return fig

@app.callback(
      Output("data-table", "children"),
     [Input("btnFrequency","n_clicks"),
      State("txtYearFrequency","value"),
         ])

def update_datatable(n_clicks,value):

    data = originaldf[originaldf["Año"] == value]

    data = data[["Nombre","Latitud", "Longitud", "Frecuencia"]]

    tabla = data.to_dict('records')
    
    columns =  [{"name": i, "id": i,} for i in (data.columns)]
   
    return ([dash_table.DataTable(
                sort_action="native",
                page_action="native",
                page_current= 0,
                page_size= 20,            
                # Con style header estilamos el encabezado de la tabla (CSS)
                style_header={
                    'backgroundColor': '#376418',
                    'textAlign': 'left',
                    'padding': '10px',
                    'color': '#fff',
                    'font-weight': 'bold'
                },
                # Con style cell estimamos las celdas de la tabla (CSS)
                style_cell={
                    'backgroundColor': '#fff',
                    'color': '#000',
                    'textAlign': 'center',
                    'font-family': 'Helvetica',
                    'font-size': '15px',
                },
                data=tabla,columns=columns)])