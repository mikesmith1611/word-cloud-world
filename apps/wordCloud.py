from dash_html_components import Div, Img, Button, H2, H1, H5, P, Hr, A, Span, Label
import dash_core_components as dcc
from templates.wordcloud import footer


def card(img_src, title, text, btn_text, btn_href):

    body = Div([
            Div([
                Img(src=img_src, className='card-img-top', width='100%')
            ]),
            Div([
                H5(title, className='card-title'),
                P(text, className='card-text')
            ], className='card-body'),
            Div([
                dcc.Link(btn_text, href=btn_href, className='btn btn-primary', style={'color': 'white'})
            ], className='card-footer')
        ], className='card')

    return body

body = Div([
    Div([
        Div([
            Div([
                H1("Word Cloud World", className='display-4 text-center'),
                Img(src="/static/world.png", width="300", height="300", alt="",
                    style={'display': 'block', 'margin': '0 auto'})
            ], className=''),
            P("Welcome!", className="lead text-center"),
            Hr(),
            P("Explore random and user defined Wikipedia articles, song lyrics or create your own word cloud by cutting and pasting or by uploading a textfile!",
              className="text-center"),
        ], className='container')
    ], className="jumbotron jumbotron-fluid", style={'background-image': '/static/world.png'}),
    Div([
        H5('Some Inspiration'),
        Div([
            card('/static/wiki-word-cloud.png',
                'Wikipedia', 'Create word clouds from Wikipedia articles', 'Explore!', '/wordcloud/wikipedia'),
            card('/static/lyrics.png',
                'Song Lyrics', 'Create word clouds from song lyrics', 'Explore!', '/wordcloud/lyrics')
        ], className='card-deck mb-2 mt-2'),
        H5('Create Your Own'),
        Div([
            card('/static/upload.png',
                'Text Upload', 'Create word clouds from uploaded text files', 'Explore!', '/wordcloud/textupload'),
            card('/static/field.png',
                'Copy & Paste', 'Create word clouds from your clipboard', 'Explore!', '/wordcloud/textfield')
        ], className='card-deck mb-2 mt-2')
    ], className='container'),
    footer
])


