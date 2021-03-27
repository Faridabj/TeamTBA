import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html


df = pd.read_csv("TeamTBA_data_cleaning.csv")

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(
    dcc.Graph(
        id='Graph1',
        figure={
            'data': [
                {'x': df.index, 'y': df.iloc[:,0], 'type': 'line', 'name': 'data'},
            ]
        }
    )
)

if __name__ == '__main__':
    app.run_server(debug=True)
#"""