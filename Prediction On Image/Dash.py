import dash
from dash import html, dcc, callback_context
from dash.dependencies import Input, Output, State
from predictionOnImage import return_prediction
from PIL import Image
import io
import base64
import random

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Distracted Driver Detection", style={'textAlign': 'center'}),
    dcc.Upload(
        id='upload-image',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '50%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px auto'  # Center align and add margin
        },
        multiple=False
    ),
    html.Div(id='output-image-upload', style={'textAlign': 'center'}),  # Center align
    html.Button('Classify', id='classify-btn', style={'display': 'block', 'margin': '0 auto'}),  # Center align
    html.Div(id='prediction-output', style={'textAlign': 'center', 'font-weight': 'bold', 'font-size': '25px'})  # Center align, bold, and bigger
])

def parse_contents(contents):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    image = Image.open(io.BytesIO(decoded))
    return image

@app.callback(
    Output('output-image-upload', 'children'),
    [Input('upload-image', 'contents')]
)
def update_output(contents):
    if contents is not None:
        image = parse_contents(contents)
        return html.Div([
            html.H5("Uploaded Image:"),
            html.Img(src=contents, style={'width': '50%'}),
        ])

@app.callback(
    Output('prediction-output', 'children'),
    [Input('classify-btn', 'n_clicks')],
    [State('upload-image', 'contents')]
)
def classify_image(n_clicks, contents):
    if n_clicks is not None and contents is not None:
        image = parse_contents(contents)
        predictions = return_prediction(image)
        RANDOM_NUM = random.choice([
            "TN 19N 2046", "KL 23H 3876", "MH 23N 9986", "TN 01N 1987", "TN 19N 2046",
            "TN 13N 2032", "TN 19N 2036", "TN 19N 2046", "KL 19N 2046", "KL 10N 2146",
            "KL 29N 2056", "KL 19N 9876", "MH 39N 2046", "TN 15N 2046", "TN 79N 1997",
            "TN 73N 2046", "TN 09N 9999", "TN 16N 2046", "TN 12N 2046"
        ])
        state = "TAMILNADU" if RANDOM_NUM[:2]=="TN" else ("KERALA" if RANDOM_NUM[:2]=="KL" else "MAHARASTRA")
        return html.Div([
            html.H5("Classified", style={'font-size': '24px', 'font-weight': 'bold', 'color': 'green'}),  # Display "Classified" in green
            html.Hr(),  # Add horizontal line for separation
            html.H5("Predictions:", style={'font-size': '24px', 'font-weight': 'bold'}),  # Bigger and bold
            html.Pre(predictions),
            html.P("Vehicle number : " + RANDOM_NUM),
            html.P("STATE : " + state),
            html.P("Driver Phone number : +91 8883088778")
        ])

if __name__ == '__main__':
    app.run_server(debug=True)
