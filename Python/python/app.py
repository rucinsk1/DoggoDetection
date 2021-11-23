import dash
from dash import html
from dash import dcc
from dash.dependencies import Output, Input
from predict import main

app = dash.Dash(__name__)
server = app.server
app.layout = html.Div([
    
    html.I("Link to dog picture: "),
    dcc.Input(id="input1", type="text", placeholder="", style={'marginRight':'10px'}),
    html.Div(id="hidden-div", style={"display":"none"})
])

@app.callback(
    Output("hidden-dive", "children"),
    Input("input1", "value"),
)
def update_output(input1, input2):
    main(input1)
    return u'Link to doggo picture: {}'.format(input1, input2)


if __name__ == '__main__':

    app.run_server(debug=True)
    