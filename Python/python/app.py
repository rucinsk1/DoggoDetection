import dash
from dash import html
from dash import dcc
from dash.dependencies import Output, Input
import flask
from flask import request
from predict import main



server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)
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

@app.route('/predict', methods = ['GET'])
def predict():
    pictureUrl= request.args.get('pictureUrl')
    returned_value = main(pictureUrl)
    if len(returned_value) > 0:
        dogType = returned_value['tagName']
    return {"dogType": dogType}



if __name__ == '__main__':

    app.run_server(debug=True)
    