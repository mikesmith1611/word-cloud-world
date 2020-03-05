from dash_html_components import Div, Img, Button, H2, H1, P, Hr, A, Span, Label
from templates.wordcloud import wordloud_controls
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from templates.wordcloud import make_word_cloud, footer
from templates.amazonIframe import amazonPrimeVideoProduct
from app import app
import wikipedia

body = Div([
    Div([
        Div([
            H1("Wikipedia Word Cloud Generator", className='display-4'),
            Hr(),
            P('This is the Wikipedia word cloud generator. Simply Enter the Article Name (exactly as seen on the wiki page) and click generate. Alternatively\
               grab a random wikipedia article with the click of a button.')], className='lead container')
    ], className="jumbotron jumbotron-fluid"),
    Div([
        # amazonPrimeVideoProduct,
        Div([
            Div('Wikipedia Wordcloud', className='card-header'),
            dcc.Loading(Div([
                H2('', className='card-title'),
                Div([Img(src='', className='card-img-top', width='100%')], style={'height': 500}),
            ], className='card-body', id='custom-wiki-wordcloud'), style={'paddingTop': 200, 'paddingBottom': 200}, type='dot'),
            Div([
                Div([
                    Div([
                        Div([Span('Article', className='input-group-text')], className='input-group-prepend'),
                        dcc.Input(id='custom-wiki-url', value='The Simpsons', placeholder='Article Name', className='form-control'),
                        Div([Button('Random!', className="btn btn-outline-secondary", id='cusotm-wiki-random')], className='input-group-append')
                    ], className='col-sm-12 input-group mb-2')
                ], className='row'),
                wordloud_controls('custom-wiki', min_font_size=1, default_mask='https://dg.imgix.net/did-the-simpsons-ruin-a-generation-0vesxi7v-en/landscape/did-the-simpsons-ruin-a-generation-0vesxi7v-8db3d7e901330e08ffa012baf31e939b.jpg?ts=1521130409&ixlib=rails-2.1.4&w=700&h=394&dpr=2&ch=Width%2CDPR&auto=format%2Ccompress&fit=min')
            ], className='card-footer')
        ], className='card mt-3')
    ], className='container'),
    footer
])

@app.callback(Output('custom-wiki-url', 'value'),
              [Input('cusotm-wiki-random', 'n_clicks')])
def update(n_clicks):

    if n_clicks == None:
        return 'The Simpsons'
    while True:
        try:
            article = wikipedia.random()
            break
        except:
            pass

    return article

@app.callback(Output('loaded', 'children'),
              [Input('url', 'pathname')])
def update(n_clicks):

    return 1

@app.callback(Output('custom-wiki-wordcloud', 'children'),
              [Input('custom-wiki-generate-wordcloud', 'n_clicks')],
               [State('custom-wiki-image-mask-url', 'value'),
                State('custom-wiki-scaling', 'value'),
                State('custom-wiki-nwords', 'value'),
                State('custom-wiki-url', 'value'),
                State('custom-wiki-stopwords', 'value'),
                State('custom-wiki-width', 'value'),
                State('custom-wiki-height', 'value'),
                State('custom-wiki-background-color', 'value'),
                State('custom-wiki-colormap', 'value'),
                State('custom-wiki-max-font', 'value'),
                State('custom-wiki-min-font', 'value'),
                State('custom-wiki-scale', 'value')])
def update(n_clicks, imagemaskurl, relative_scaling, nwords, article,
           customstopwords, width, height, color, colormap, maxfont, minfont,
           scale):
    """Serves the logo image."""

    if maxfont == 0:
        maxfont = None
    
    title = []
    try:
        page = wikipedia.page(article)
        text = page.content + ' ' + page.summary
        title = [Div([page.title])]
        words = article.strip(',').split(' ') + page.title.split(' ')
    except:
        text = 'Invalid Page!'
        words = ['yes']
    customstopwords = customstopwords.split(',') + words

    children = make_word_cloud(imagemaskurl, relative_scaling, nwords, text,
                               title, customstopwords, width, height, color,
                               colormap, maxfont, minfont, scale)

    return children