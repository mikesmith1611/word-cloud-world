import matplotlib
matplotlib.use('Agg')
from dash_html_components import Div, Img, Button, H2, H1, P, Hr, A, Span, Label, Hr, Footer, Ul, Li, Meta
import dash_core_components as dcc
from dash.dependencies import Output, Input, State

from apps import wikipediaWordCloud, lyricsWordCloud, textFieldWordCloud, textUploadWordCloud, wordCloud
from app import app
from templates.wordcloud import footer

server = app.server
navbar = Div([
    Div(['Word Cloud World',
    ], className='navbar-brand'),
    Button(Span(className='navbar-toggler-icon'),
            className='navbar-toggler',
            type="button", **{'data-toggle': "collapse", 'data-target': "#navbarNav",
            'aria-controls': "navbarNav", 'aria-expanded': "false", 'aria-label': "Toggle navigation"}),
    Div([
        Ul([
            Li(dcc.Link('Home', href="/", className='nav-link'), className='nav-item', style={'cursor': 'pointer'}),
            Li(dcc.Link('Wiki Cloud', href="/wordcloud/wikipedia", className='nav-link'), className='nav-item', style={'cursor': 'pointer'}),
            Li(dcc.Link('Lyrics Cloud', href="/wordcloud/lyrics", className='nav-link'), className='nav-item', style={'cursor': 'pointer'}),
            Li(dcc.Link('Upload Cloud', href="/wordcloud/textupload", className='nav-link'), className='nav-item', style={'cursor': 'pointer'}),
            Li(dcc.Link('Copy & Paste Cloud', href="/wordcloud/textfield", className='nav-link'), className='nav-item', style={'cursor': 'pointer'})
        ], className='navbar-nav')
    ], className='collapse navbar-collapse', id="navbarNav")
], className='navbar navbar-dark bg-dark navbar-expand-lg')

app.layout = Div([
    Meta(name="viewport", content="width=device-width, initial-scale=1, shrink-to-fit=no"),
    dcc.Location(id='url', pathname=None, refresh=False),
    navbar,
    Div(id='body')
])

@app.callback(Output('body', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):

    if pathname is None or pathname == '/':
        return wordCloud.body
    if pathname.rstrip('/') == '/wordcloud/wikipedia':
        return wikipediaWordCloud.body
    elif pathname.rstrip('/') == '/wordcloud/lyrics':
        return lyricsWordCloud.body
    elif pathname.rstrip('/') == '/wordcloud/textupload':
        return textUploadWordCloud.body
    elif pathname.rstrip('/') == '/wordcloud/textfield':
        return textFieldWordCloud.body
    else:
        return '404'



for i in ['custom-wiki', 'text-field', 'text-upload']:
    @app.callback(Output(i + '-save-wordcloud', 'href'),
                  [Input(i + '-wordcloud', 'children')])
    def update_href(children):

        return children[1]['props']['src']


if __name__ == "__main__":
    app.run_server(host='0.0.0.0', debug=True)