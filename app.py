import pandas as pd
import json
import plotly.graph_objects as go
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html

state_geo1 = json.load(open('TL_SCCO_CTPRVN.json', encoding='utf-8'))
trace1 = []
trace1.append(go.Choroplethmapbox(
    geojson=state_geo1,
    visible=False,
    
))
trace1[0]['visible'] = True

latitude = 35.565
longitude = 127.986

layout = go.Layout(
    title={'text': 'Number of people in Korea / Local extinction in 2018',
           'font': {'size': 28,
                    'family': 'Arial'}},
    autosize=True,

    mapbox1=dict(
        domain={'x': [0.3, 1], 'y': [0, 1]},
        center=dict(lat=latitude, lon=longitude),
        style="open-street-map",
        # accesstoken = mapbox_accesstoken,
        zoom=5),

    xaxis2={
        'zeroline': False,
        "showline": False,
        "showticklabels": True,
        'showgrid': True,
        'domain': [0, 0.25],
        'side': 'left',
        'anchor': 'x2',
    },
    yaxis2={
        'domain': [0.4, 0.9],
        'anchor': 'y2',
        'autorange': 'reversed',
    },
    margin=dict(l=100, r=20, t=70, b=70),
    paper_bgcolor='rgb(204, 204, 204)',
    plot_bgcolor='rgb(204, 204, 204)',
)

fig = go.Figure(data=trace1, layout=layout)
external_stylesheets= ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets = external_stylesheets)
server = app.server

app.layout = html.Div([
    html.Div(children=[
        dcc.Graph(
            id='example-graph-1',
            figure=fig
        )
    ])
])

# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output
# import plotly.graph_objects as go

# app = dash.Dash(__name__)


# app.layout = html.Div([
#     html.H4('Interactive color selection with simple Dash example'),
#     html.P("Select color:"),
#     dcc.Dropdown(
        
#         options=[
#             {'label': "Gold" , "value":"Gold"},
#             {'label': "MediumTurquoise", "value" : "MediumTurquoise"},
#             {'label': "LightGreen", "value" : "LightGreen"}
#             ],
#         value='Gold',
#         clearable=False,
#         id="dropdown",
        
#     ),
#     dcc.Graph(id="graph"),
# ])


# @app.callback(
#     Output("graph", "figure"), 
#     Input("dropdown", "value"))
# def display_color(color):
#     fig = go.Figure(
#         data=go.Bar(y=[2, 3, 1], # replace with your own data source
#                     marker_color=color))
#     return fig


app.run_server(debug=True)
