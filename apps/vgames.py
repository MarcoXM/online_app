import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib
from app import app

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

dfv = pd.read_csv(DATA_PATH.joinpath("SW_data_4_sites.csv"))  # GregorySmith Kaggle


layout = html.Div([
    html.H1('Comsumer Company Visualization', style={"textAlign": "center"}),

    html.Div([
        html.Div(dcc.Dropdown(
            id='genre-dropdown', value='visits', clearable=False,
            options=[
                        {'label': 'numbers of visits', 'value': 'visits'},
                        {'label': 'bounce rate', 'value': 'bounce_rate'},
                        {'label': 'average visit duration(mins)', 'value': 'average_visit_duration'},
                        {'label': 'number of unique visitor', 'value': 'unique_visitors'},
                        {'label': 'number of pages in a visit', 'value': 'pages_per_visit'},
                        {'label': 'total page view per visit', 'value': 'total_page_views'}
                ],
            style={"width": "50%"}
        ), className='six columns'),

    ], className='row'),

    dcc.Graph(id='my-bar', figure={}),
])


@app.callback(
    Output(component_id='my-bar', component_property='figure'),
    [Input(component_id='genre-dropdown', component_property='value')]
)
def display_value(genre_chosen):
    # print(genre_chosen)
    linechart = px.line(
            data_frame = dfv,
            x = "date",
            y = genre_chosen)
    return linechart
