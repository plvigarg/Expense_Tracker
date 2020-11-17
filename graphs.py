import plotly
import plotly.graph_objs as go

import pandas as pd
import numpy as np
import json
from ghaint_chart import xyfunc


def create_plot():

    N = 40
    x = np.linspace(0, 1, N)
    y = np.random.randn(N)
    df = pd.DataFrame({"x": x, "y": y})  # creating a sample dataframe

    data = [
        go.Pie(
            labels=df["x"],
            values=df["y"],
            # textinfo="label+percent",
            insidetextorientation="radial",
            hole=0.3,
            name="CO2 Emissions",
        )
    ]  # assign x as the dataframe column 'x'

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


def ghaint_chart():

    x, y = xyfunc()
    df = pd.DataFrame({"x": x, "y": y})  # creating a sample dataframe

    data = [
        go.Pie(
            labels=df["x"],
            values=df["y"],
            # textinfo="label+percent",
            # insidetextorientation="radial",
            hole=0.4,
            title="This Months expenses",
        )
    ]  # assign x as the dataframe column 'x'

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

