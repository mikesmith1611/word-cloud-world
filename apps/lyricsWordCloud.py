from dash_html_components import Div, Img, Button, H2, H1, P, Hr, A, Span, Label
from templates.wordcloud import wordloud_controls
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from app import app
from PyLyrics import PyLyrics
from templates.wordcloud import remove_html_tags, make_word_cloud, footer
from templates.amazonIframe import amazonMusicProduct 

body = Div([
    Div([
        Div([
            H1("Lyrics Word Cloud Generator", className='display-4'),
            Hr(),
            P('This is the Lyrics word cloud generator. Simply Enter the Artist Name and Song and click generate.'),
        ], className='container')
    ], className="jumbotron jumbotron-fluid"),
    Div([
        amazonMusicProduct,
        Div([
            Div('Lyrics Wordcloud', className='card-header'),
            Div([
                H2('', className='card-title'),
                Div([Img(src='', className='card-img-top', width='100%')], style={'height': 500})
            ], className='card-body', id='lyrics-wordcloud'),
            Div([
                Div([
                    Div([
                        Div([Span('Artist', className='input-group-text')], className='input-group-prepend'),
                        dcc.Input(id='lyrics-artist', value='Rick Astley', placeholder='Artist', className='form-control'),
                    ], className='col-sm-6 input-group mb-2'),
                    Div([
                        Div([Span('Song', className='input-group-text')], className='input-group-prepend'),
                        dcc.Input(id='lyrics-song', value='Never Gonna Give You Up', placeholder='Song', className='form-control'),
                    ], className='col-sm-6 input-group mb-2')
                ], className='row'),
                wordloud_controls('lyrics')
            ], className='card-footer')
        ], className='card mt-3')
    ], className='container', id='container'),
    footer
])


@app.callback(Output('lyrics-wordcloud', 'children'),
              [Input('lyrics-generate-wordcloud', 'n_clicks')],
               [State('lyrics-image-mask-url', 'value'),
                State('lyrics-scaling', 'value'),
                State('lyrics-nwords', 'value'),
                State('lyrics-artist', 'value'),
                State('lyrics-song', 'value'),
                State('lyrics-stopwords', 'value'),
                State('lyrics-width', 'value'),
                State('lyrics-height', 'value'),
                State('lyrics-background-color', 'value'),
                State('lyrics-colormap', 'value'),
                State('lyrics-max-font', 'value'),
                State('lyrics-min-font', 'value'),
                State('lyrics-scale', 'value')])
def update(n_clicks, imagemaskurl, relative_scaling, nwords, artist, song, customstopwords,
           width, height, color, colormap, maxfont, minfont, scale):
    """Serves the logo image."""
    try:
        text = PyLyrics.getLyrics(artist, song).replace('\n', ' ')
    except ValueError:
        text = 'Song or Singer does not exist or the API does not have Lyric'.replace(' ', '_')
    
    text = remove_html_tags(text)
    if maxfont == 0:
        maxfont = None
    from wordcloud import STOPWORDS

    customstopwords = customstopwords.split(',')
    title = Div()
    children = make_word_cloud(imagemaskurl, relative_scaling, nwords, text,
                               title, customstopwords, width, height, color,
                               colormap, maxfont, minfont, scale)

    return children