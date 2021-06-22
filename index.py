import dash_core_components as dcc
import dash_bootstrap_components as dbc

import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import server
from app import app
from pages import contacto, home,anual


dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Home", href="/"),
        dbc.DropdownMenuItem("Frecuencias Anuales", href="/anual"),
        dbc.DropdownMenuItem("Frecuencias Mensuales", href="/"),
    ],
    nav = True,
    in_navbar = True,
    label = "Explorar",
)



navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(dcc.Link(html.I(id='btn-home', n_clicks=0, className='fa fa-cloud',
                                                style={'color': 'white', 'fontSize': '2rem'}), href='/')),
                        dbc.Col(dbc.NavbarBrand(
                            "Climatología de granizo en Argentina", className="ml-2")),
                    ],
                    align="left",
                    className="ml-auto",
                    no_gutters=True,
                ),
            ),
            dbc.NavbarToggler(id="navbar-toggler"),
            dbc.Collapse(
                dbc.Nav([dropdown],
                    className="ml-auto", navbar=True
                ),
                id="navbar-collapse",
                navbar=True,
            ),
            dbc.Col(dcc.Link(html.I(id='btn-contact', n_clicks=0, className='far fa-envelope',
                                                style={'color': 'white', 'fontSize': '2rem'}), href='/contacto'))
        ],
    ),
    color="#4E7F2D",
    dark=True
)

# link = [dbc.NavLink("Frecuencia mensual", href="/mensual", active="exact", 
#                     style={"font-size": "19px", "padding-left": "0px"})                    
#         ]

buttons = [dbc.Button("Contacto", color="info", href='/contacto', className="mr-1 btn-space"),
           ]

content = html.Div(id="page-content", className="content")


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,content
])




@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(Output("page-content", "children"), 
                [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/":
        return home.layout
    elif pathname == "/contacto":
        return contacto.layout
    elif pathname == "/anual":
        return anual.layout
    # elif pathname == "/mensual":
    #     return mensual.layout         
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )    

if __name__ == '__main__':
    app.run_server(debug=True)
