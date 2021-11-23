import dash
from dash import html
from dash import dcc

app = dash.Dash(__name__)
server = app.server
app.layout = html.Div([
    
    html.Img(
        src=app.get_asset_url('keller.png'),
        style={
            'display' : 'block',
            'margin-left' : 'auto',
            'margin-right' : 'auto'}),

    dcc.Markdown('''
    ###### o_HC_FUNDINGID
    ''',
    style={
        'textAlign': 'center',
        #'display': 'none'
    }),
    dcc.Dropdown(
        id='o_HC_FUNDINGID_dropdown',
        options=[
            {'label': 'Fed/State', 'value': 0},
            {'label': 'Federal', 'value': 1},
            {'label': 'Local', 'value': 2},
            {'label': 'Private', 'value': 3},
            {'label': 'State', 'value': 4}

        ],
        value=0,
        style={'textAlign': 'center'},
    ),

    dcc.Markdown('''
    ###### br_SEGMENT
    ''',
    style={
        'textAlign': 'center',
        #'display': 'none'
    }),
    dcc.Dropdown(
        id='br_SEGMENT_dropdown',
        options=[
            {'label': 'Nan', 'value': 0},
            {'label': 'Cons-Architect', 'value': 1},
            {'label': 'Cons-Environemntal', 'value': 2},
            {'label': 'Cons-Geotechnical', 'value': 3},
            {'label': 'Cons-Multidisc.', 'value': 4},
            {'label': 'Cons-Other', 'value': 5},
            {'label': 'Cons-Structural', 'value': 6},
            {'label': 'Contractor/CM', 'value': 7},
            {'label': 'Education', 'value': 8},
            {'label': 'Engineer', 'value': 9},
            {'label': 'Goverment', 'value': 10},
            {'label': 'Insurance', 'value': 11},
            {'label': 'Other', 'value': 12},
            {'label': 'Owner-Residental', 'value': 13},
            {'label': 'Owner/Developer', 'value': 14},
            {'label': 'Supplier', 'value': 15}

        ],
        value=0,
        style={'textAlign': 'center'},
    ),

    dcc.Markdown('''
    ###### ql_TechniqueName
    ''',
    style={
        'textAlign': 'center',
        #'display': 'none'
    }),
    dcc.Dropdown(
        id='ql_TechniqueName_dropdown',
        options=[
            {'label': 'Nan', 'value': 0},
            {'label': 'Anchors - Permanent', 'value': 1},
            {'label': 'Anchors - Temporary', 'value': 2},
            {'label': 'Augercast - Displacement', 'value': 3},
            {'label': 'Augercast - Low Headroom', 'value': 4},
            {'label': 'Augercast - RegularS', 'value' : 5},
            {'label': 'Agercast-Reg.<24"D', 'value': 6},
            {'label': 'Cracing', 'value': 7},
            {'label': 'Caissons', 'value': 8},
            {'label': 'Caissons-M. Dry (4-8\'D)', 'value': 9},
            {'label': 'Caissons-S. Dry (4-8\'D)', 'value': 10},
            {'label': '"Caissons-S. Rock (<4\'D)"', 'value': 11},
            {'label': 'Cased Secant Piles (CSP) / Cased Augered Piles', 'value': 12},
            {'label': 'Cement Grouting' , 'value': 13},
            {'label': 'Chemical Grouting', 'value': 14},
            {'label': 'Compaction Grouting', 'value': 15},
            {'label': 'Dewatering-Deep Wells', 'value': 16},
            {'label': 'Dewatering-Other', 'value': 17},
            {'label': 'Dewatering-Well Points', 'value': 18},
            {'label': 'Displacement Piles', 'value': 19},
            {'label': 'Drilled Shafts - Rock Socketed < 8\' Dia.', 'value': 20},
            {'label': 'Drilled Shafts - Slurry Soil <8\' Dia.', 'value': 21},
            {'label': 'Drilling', 'value': 22},
            {'label': 'Drilling - Other', 'value': 23},
            {'label': 'Drilling - Predrill', 'value': 24},
            {'label': 'Dynamic Compaction', 'value': 25},
            {'label': 'EQ Drains', 'value': 26},
            {'label': 'Environmental', 'value': 27},
            {'label': 'Ground Freezing', 'value': 28},
            {'label': 'Groundwater Treatment', 'value': 29},
            {'label': 'Grouting - Other', 'value': 30},
            {'label': 'Helical Piles', 'value': 31},
            {'label': 'Horizontal Drains', 'value': 32},
            {'label': 'Jacked/Helical Piers', 'value': 33},
            {'label': 'Jet Grouting', 'value': 34},
            {'label': 'Macropiles', 'value': 35},
            {'label': 'Micropiles', 'value': 36},
            {'label': 'Mine stabilization', 'value': 37},
            {'label': 'Other', 'value': 38},
            {'label': 'Other-Fluid Treatment', 'value': 39},
            {'label': 'Piles Driven - Precast', 'value': 40},
            {'label': 'Piles Driven - Sheeting', 'value': 41},
            {'label': 'Piles Driven - Steel', 'value': 42},
            {'label': 'Piles Driven - Timber', 'value': 43},
            {'label': 'Piles Driven - Pres. Inj.', 'value': 44},
            {'label': 'Pit Underpining', 'value': 45},
            {'label': 'Polyurethane Grouting', 'value': 46},
            {'label': 'Rapid Impact Compacction', 'value': 47},
            {'label': 'Rigid Inclusions', 'value': 48},
            {'label': 'SB&L - Cantilevered', 'value': 49},
            {'label': 'SB&L - Anchored', 'value': 50},
            {'label': 'SB&L - Braced', 'value': 51},
            {'label': 'Secant Wall', 'value': 52},
            {'label': 'Shotcrete', 'value': 53},
            {'label': 'SlabJacking', 'value': 54},
            {'label': 'Slurry Wall - Hydromill', 'value': 55},
            {'label': 'Soil Mixing - Dry', 'value': 56},
            {'label': 'Soil Mixing - Wet', 'value': 57},
            {'label': 'Soil Nailing - Permanent', 'value': 58},
            {'label': 'Soil Nailing - Temporary', 'value': 59},
            {'label': 'Soldier Beam & Lagging', 'value': 60},
            {'label': 'Tangent/Secant Piles', 'value': 61},
            {'label': 'Vibro - Replacement', 'value': 62},
            {'label': 'Vibro Piers', 'value': 63},
            {'label': 'Waterproofing', 'value': 64},
            {'label': 'Wick Drains', 'value': 65}
        ],
        value=0,
        style={'textAlign': 'center'},
    ),

    #html.Button('Predict', id='predict_button', style={'textAlign': 'center',  'align-items' : 'center'}),
    html.Div(id='probability_div', style={'textAlign': 'center'})
])


if __name__ == '__main__':
    
    print("DUPA")