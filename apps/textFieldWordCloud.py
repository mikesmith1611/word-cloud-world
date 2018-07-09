from dash_html_components import Div, Img, Button, H2, H1, P, Hr, A, Span, Label
from templates.wordcloud import wordloud_controls
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from app import app
from templates.wordcloud import make_word_cloud, footer
import lorem

body = Div([
    Div([
        Div([
            H1("Copy & Paste Word Cloud Generator", className='display-4'),
            Hr(),
            P('This is the copy & paste word cloud generator. Simply copy and paste the text into the box below.'),
        ], className='container')
    ], className="jumbotron jumbotron-fluid"),
    Div([
        Div([
            Div('Text Field Wordcloud', className='card-header'),
            Div([
                H2('', className='card-title'),
                Div([Img(src='', className='card-img-top', width='100%')], style={'height': 500}),
            ], className='card-body', id='text-field-wordcloud'),
            Div([
                P('This is the text field word cloud generator. Simply copy and paste the text into the box below.'),
                Div([
                    Div([
                        dcc.Textarea(id='text-field', style={'height': 250, 'width': '100%'}, value=lorem.paragraph())
                    ], className='col-lg-12')
                ], className='row'),  
                    wordloud_controls('text-field')
            ], className='card-footer')
        ], className='card mt-3')
    ], className='container'),
    footer
])


@app.callback(Output('text-field-wordcloud', 'children'),
              [Input('text-field-generate-wordcloud', 'n_clicks')],
               [State('text-field-image-mask-url', 'value'),
                State('text-field-scaling', 'value'),
                State('text-field-nwords', 'value'),
                State('text-field', 'value'),
                State('text-field-stopwords', 'value'),
                State('text-field-width', 'value'),
                State('text-field-height', 'value'),
                State('text-field-background-color', 'value'),
                State('text-field-colormap', 'value'),
                State('text-field-max-font', 'value'),
                State('text-field-min-font', 'value'),
                State('text-field-scale', 'value')])
def update(n_clicks, imagemaskurl, relative_scaling, nwords, text, customstopwords,
           width, height, color, colormap, maxfont, minfont, scale):
    """Serves the logo image."""

    if maxfont == 0:
        maxfont = None
    from wordcloud import STOPWORDS

    customstopwords = customstopwords.split(',')
    title = Div()
    children = make_word_cloud(imagemaskurl, relative_scaling, nwords, text,
                               title, customstopwords, width, height, color,
                               colormap, maxfont, minfont, scale)

    return children