import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc


from app import app

email_input = dbc.FormGroup([dbc.Label("Email", html_for="example-email-row", width=2)
                    , dbc.Col(dbc.Input(type="email"
                                        , id="example-email-row"
                                        , placeholder="Deja tu correo electrónico") 
                                , width=10) 
                        ], row=True)
user_input = dbc.FormGroup([dbc.Label("Nombre", html_for="example-name-row", width=2)
                    ,dbc.Col(dbc.Input(type="text"
                                        , id="example-name-row"
                                        , placeholder="Escribe tu nombre"
                                        , maxLength = 80)
                            , width=10) 
                    ],row=True)
message = dbc.FormGroup([dbc.Label("Mensaje", html_for="example-message-row", width=2)
                    ,dbc.Col(dbc.Textarea(id = "example-message-row"
                                        , className="mb-3"
                                        , placeholder="Escribe tu mensaje"
                                        , required = True)
                            , width=10)
                ], row=True)

markdown = '''# Deje su mensaje (Proximamente)'''


form = html.Div([ dbc.Container([dcc.Markdown(markdown)
            , html.Br()
            , dbc.Card(dbc.CardBody([dbc.Form([email_input, user_input, message])
                ,html.Div(id = 'div-button', children = [
                    dbc.Button('Enviar', color = 'success', id='button-submit', n_clicks=0)
                ]) 
                ])
            )
            , html.Br()
            , html.Br()
        ])
])



layout = html.Div(style={
     'background-image': 'url("/assets/backgroundImage.jpg")'
    , 'background-position': 'center'
    }
    , children = [dbc.Container(id = 'card-cont', children = [form], style = {'background-color':'white', })
       ]                     
    ) 



# @app.callback([Output('div-button', 'children')],
#      [Input("button-submit", 'n_clicks')
#      ,Input("example-email-row", 'value')
#      ,Input("example-name-row", 'value')
#      ,Input("example-message-row", 'value')
#     ])
# def submit_message(n, email, name, message):
    
#     port = 465  # For SSL
#     sender_email = email
#     receiver_email = '<your email address here>'
      
#     # Create a secure SSL context
#     context = ssl.create_default_context()       
    
#     if n > 0:
#         with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
#             server.login("<you email address here>", '<you email password here>')
#             server.sendmail(sender_email, receiver_email, message)
#             server.quit()
#         return [html.P("Message Sent")]
#     else:
#         return[dbc.Button('Submit', color = 'primary', id='button-submit', n_clicks=0)]