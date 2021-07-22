import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app
import plotly.express as px
import dash_table
import pandas as pd
import dash


originaldf = pd.read_csv('frecuencia.csv', 
                         sep=',', header = 0,
                         names=['ID', 'Nombre', 'Latitud', 'Longitud', 'Altura', 'Año', 'Frecuencia'])


meandf = pd.read_csv('medias_periodos.csv', 
                         sep=',', header = 0,
                         names=['ID', 'Nombre', 'Latitud', 'Longitud', 'Altura', 'Frecuencia', 
                                'Periodo'])                         

Variables = {
    "1960-1979": "1960-1979",
    "1980-1999": "1980-1999",
    "2000-2019": "2000-2019",
    "1960-1999": "1960-1999",
    "1980-2019": "1980-2019",
    "1960-2019": "1960-2019",
}

layout = html.Div(
    children=[
        html.Div(className="row",
            children=[
                dbc.Col(
                    children=[html.Div(
                                children=[
                                    html.H3(['Frecuencia anual',dbc.Badge("info", id= "tooltip",color="info", pill = True,
                                        className="ml-2", style={'font-size': '12px'}),
                                        dbc.Tooltip("Número de eventos de granizo por año",target="tooltip")]),
                                    dbc.Input(id="txtYearFrequency", placeholder="Elije un año...", type="number",min=1930, 
                                            max=2019, step=1,style = {'width' : '30%', 'margin-top' : '5px'}),
                                    dbc.Button("Seleccionar", id="btnAnnual", outline=True, 
                                            color="success", className="mt-3 mb-5"),
                                ]),
                              html.Div(
                                children=[    
                                    html.H3('Promedio anual por periodos'),
                                    dcc.Dropdown(id="ddlPeriod",
                                            options=[
                                                {"label": key, "value": value} for key, value in Variables.items()],
                                                    value="1960-2019", 
                                                    style = {'font-size': '16px', 'white-space': 'nowrap', 'text-overflow': 'ellipsis'}
                                    ),
                                    dbc.Button("Seleccionar", id="btnAnnualPeriod", outline=True, 
                                            color="success", className="mt-3 mb-5"),
                                ],style = {'width' : '90%', 'margin-top' : '5px'})
                            ],md=4),

                dbc.Col(    
                    children=[
                        html.Div(id='htmlContainer'),
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
    [Output("graph", "figure"),
     Output("htmlContainer","children")],
    [Input("btnAnnual","n_clicks"),
     Input("btnAnnualPeriod","n_clicks"),
     State("txtYearFrequency","value"),
     State("ddlPeriod","value")
    ],
)
def update_graph(frequencyA,frequencyP,year,period):

    context = dash.callback_context

    buttonClicked = context.triggered[0]['prop_id'].split('.')[0] 

    if (buttonClicked == "btnAnnual"):

        #Año seleccionado
        data = originaldf[originaldf["Año"] == year]

        data = data[["Latitud", "Longitud", "Frecuencia"]]

        returnAlert= [dbc.Alert(f'Frecuencia de eventos en el año {year}' , color="light",style = {'margin-top' : '5px','text-align': 'center'})]
    else:

        data = meandf[meandf["Periodo"] == period]
        returnAlert= [dbc.Alert(f'Promedio anual de eventos durante el periodo {period}' , color="light",style = {'margin-top' : '5px','text-align': 'center'})]


    fig = px.scatter_mapbox(data, lat="Latitud", lon="Longitud", color="Frecuencia",
                        color_continuous_scale=px.colors.cyclical.IceFire, 
                        range_color=[0,10],zoom=4, height=600)
    fig.update_layout(mapbox_style="open-street-map")

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.update_layout(coloraxis_colorbar=dict(thickness=30,
                            ticklen=1, tickcolor='black',tickvals = [0,1,2,3,4,5,6,7,8,9,10],
                            tickfont=dict(size=15, color='black')))

    fig.update_traces(marker=dict(size=14))

    return(fig,returnAlert)

@app.callback(
      Output("data-table", "children"),
     [Input("btnAnnual","n_clicks"),
     Input("btnAnnualPeriod","n_clicks"),
     State("txtYearFrequency","value"),
     State("ddlPeriod","value"),
         ])

def update_datatable(frequencyA,frequencyP,year,period):

    context = dash.callback_context

    buttonClicked = context.triggered[0]['prop_id'].split('.')[0] 

    if (buttonClicked == "btnAnnual"):

        data = originaldf[originaldf["Año"] == year]

        data = data[["Nombre","Latitud", "Longitud", "Frecuencia"]]
   
    else:
        data = meandf[meandf['Periodo']== period]

        data = data.rename(columns={'Frecuencia':'Promedio anual'})

        data = data[["Nombre","Latitud", "Longitud", "Promedio anual"]]

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