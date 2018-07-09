from dash_html_components import Div, Img, Button, H2, H1, P, Hr, A, Span, Label
from templates.wordcloud import wordloud_controls
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from app import app
from templates.wordcloud import make_word_cloud, footer

body = Div([
    Div([
        Div([
            H1("Text Upload Word Cloud Generator", className='display-4'),
            Hr(),
            P('This is the text upload word cloud generator. Simply upload a UTF-8 encoded .txt file.'),
        ], className='container')
    ], className="jumbotron jumbotron-fluid"),
    Div([
        Div([
            Div('Text Upload Wordcloud', className='card-header'),
            Div([
                H2('', className='card-title'),
                Div([Img(src='', className='card-img-top', width='100%')], style={'height': 500}),
            ], className='card-body', id='text-upload-wordcloud'),
            Div([
                Div([
                    Div([
                        dcc.Upload([Button('Drag and Drop or Click to Upload .txt', className="btn btn-link")], style={
                                    'width': '100%',
                                    'height': '60px',
                                    'lineHeight': '60px',
                                    'borderWidth': '1px',
                                    'borderStyle': 'dashed',
                                    'borderRadius': '5px',
                                    'textAlign': 'center'},
                                    className='mb-2',
                                id='text-upload', filename='Moby Dick.txt')
                    ], className='col-12')
                ], className='row'),
                wordloud_controls('text-upload', default_mask='http://getdrawings.com/img/whale-silhouette-26.jpg')
            ], className='card-footer')
        ], className='card mt-3')
    ], className='container'),
    footer
])


@app.callback(Output('text-upload-wordcloud', 'children'),
              [Input('text-upload-generate-wordcloud', 'n_clicks'),
               Input('text-upload', 'contents')],
               [State('text-upload-image-mask-url', 'value'),
                State('text-upload-scaling', 'value'),
                State('text-upload-nwords', 'value'),
                State('text-upload-stopwords', 'value'),
                State('text-upload-width', 'value'),
                State('text-upload-height', 'value'),
                State('text-upload-background-color', 'value'),
                State('text-upload-colormap', 'value'),
                State('text-upload-max-font', 'value'),
                State('text-upload-min-font', 'value'),
                State('text-upload', 'filename'),
                State('text-upload-scale', 'value')])
def update(n_clicks, text, imagemaskurl, relative_scaling, nwords, customstopwords,
           width, height, color, colormap, maxfont, minfont, filename, scale):
    """Serves the logo image."""
    from wordcloud import STOPWORDS
    if text is not None:
        try:
            text = re.search(r'base64,(.*)', text).group(1)
            text = base64.b64decode(text).decode('utf-8')
        except:
            text = 'Invalid File'
    else:
        text = open('data/Moby Dick.txt', 'r', encoding='utf-8').read()

    if maxfont == 0:
        maxfont = None

    customstopwords = customstopwords.split(',')
    title = Div(filename)
    children = make_word_cloud(imagemaskurl, relative_scaling, nwords, text,
                               title, customstopwords, width, height, color,
                               colormap, maxfont, minfont, scale)

    return children
