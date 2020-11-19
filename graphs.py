import plotly
import plotly.graph_objs as go

import pandas as pd
import numpy as np
import json
from ghaint_chart import xyfunc
from basicGraph import basic_graph, basic_graph2
from savingsGraph import savings, savings2


def savingGraph():

    x, y = savings()
    df = pd.DataFrame({"x": x, "y": y})  # creating a sample dataframe

    data = [
        go.Scatter(x=df["x"], y=df["y"], mode="lines", name="Monthly")
    ]  # assign x as the dataframe column 'x'

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


def savingGraph2():

    x, y = savings2()
    df = pd.DataFrame({"x": x, "y": y})  # creating a sample dataframe

    data = [
        go.Scatter(x=df["x"], y=df["y"], mode="lines", name="Aggregate")
    ]  # assign x as the dataframe column 'x'

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


def baseGraph():

    x, y = basic_graph()
    df = pd.DataFrame({"x": x, "y": y})  # creating a sample dataframe

    data = [
        go.Scatter(x=df["x"], y=df["y"], mode="lines", name="Daily")
    ]  # assign x as the dataframe column 'x'

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


def baseGraph2():

    x, y = basic_graph2()
    df = pd.DataFrame({"x": x, "y": y})  # creating a sample dataframe

    data = [
        go.Scatter(x=df["x"], y=df["y"], mode="lines", name="Aggregate")
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
