from dash_html_components import Div, Img, Button, H2, H1, P, Hr, A, Span, Label, Details, Summary
import dash_core_components as dcc
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import io
import base64
from PIL import Image
import plotly.graph_objs as go
import re
import numpy as np
import requests
from templates.amazonIframe import amazonMusicProduct


instructions = """
* Stop Words
    - These are words / bigrams that you would like to remove from the word cloud. A set of common stop words are already removed.

* Max Font Size
    - The maximum font size allowed in the word cloud. 0 sets it to the height of the canvas.

* Min Font Size
    - The minimum font size allowed in the word cloud.

* Width
    - The width of the image (does not apply when using Image Mask)

* Height
    - The height of the image (does not apply when using Image Mask)

* Scale
    - This is used to scale the size of the image (faster than a larger canvas but less accurate word placement)

* Frq/Rnk
    - This determined how the font size of the words scale with word frequency and word rank.
    A value of 1 means that font size is scaled only by frequency. A value of zero means
    that only the rank is considered.

* Max words
    - The maximum number of words to display

* Color Scale
    - The color scale for the words. This is ignored if an RGB image mask is used.

* Background
    - The background color of the image. Blank will render a transparent background. Accepts HEX colors.

* Image Mask
    - The URL of a png/jpg used to draw the shape of the word cloud. If the image doesn't work try another!

This app is powered by [amueller's word_cloud](https://github.com/amueller/word_cloud) see the API reference for more details.

"""

def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def wordloud_controls(id_prefix, default_mask=None, min_font_size=4):

    c = Div([
        Div([
            Div([
                Div([
                    Div([Span('Stop Words', className='input-group-text')], className='input-group-prepend'),
                    dcc.Input(id='{0}-stopwords'.format(id_prefix), value='show,episode,season,series,episodes,time,first,character,characters', placeholder='Stop Words (,)', className='form-control')
                ], className='col input-group mb-2')
            ], className='row'),
            Div([
                Div([
                    Div([
                        Div([Span('Width', className='input-group-text')], className='input-group-prepend'),
                        dcc.Input(id='{0}-width'.format(id_prefix), value=1000, inputmode='numeric', type='number', min=200, max=2000, className='form-control'),

                    ], className='input-group mb-2')
                ], className='col-6 col-md-4'),
                    Div([
                        Div([
                            Div([Span('Height', className='input-group-text')], className='input-group-prepend'),
                            dcc.Input(id='{0}-height'.format(id_prefix), value=500, inputmode='numeric', type='number', min=200, max=2000, className='form-control'),

                        ], className='input-group mb-2')
                    ], className='col-6 col-md-4'),
                    Div([
                        Div([
                            Div([Span('Scale', className='input-group-text')], className='input-group-prepend'),
                            dcc.Input(id='{0}-scale'.format(id_prefix), value=1, inputmode='numeric', type='number', min=1, max=10, className='form-control'),
                        ], className='input-group mb-2')
                    ], className='col-12 col-md-4')
            ], className='row'),
            Div([
                Div([
                    Div([
                        Div([Span('Colorscale', className='input-group-text')], className='input-group-prepend'),
                        Div([
                            dcc.Dropdown(options=[{'label': i, 'value': i} for i in plt.colormaps()], value='viridis', id='{0}-colormap'.format(id_prefix), clearable=False)
                        ], style={'padding': 0, 'border': 0, 'background-color': 'rgba(0,0,0,0)'}, id='{0}-colormap-container'.format(id_prefix), className='form-control')
                    ], className='input-group mb-2')
                ], className='col-lg-6 col-md-6'),
                Div([
                    Div([
                        Div([Span('Background', className='input-group-text')], className='input-group-prepend'),
                        dcc.Input(id='{0}-background-color'.format(id_prefix), value='#ffffff', type='color', inputmode='numeric', className='form-control', style={'padding': 0, 'height': 38})
                    ], className='input-group mb-2'),
                ], className='col-lg-6 col-md-6'),
            ], className='row')
        ], className='col-lg-6'),
        Div([
            Div([
                Div([
                    Div([
                        Div([Span('Max font', className='input-group-text')], className='input-group-prepend'),
                        dcc.Input(id='{0}-max-font'.format(id_prefix), value=0, inputmode='numeric', type='number', min=0, max=100, className='form-control'),
                    ], className='input-group mb-2')
                ], className='col-6'),
                    Div([
                        Div([
                            Div([Span('Min font', className='input-group-text')], className='input-group-prepend'),
                            dcc.Input(id='{0}-min-font'.format(id_prefix), value=min_font_size, inputmode='numeric', type='number', min=1, max=100, className='form-control'),
                        ], className='input-group mb-2')
                    ], className='col-6')
            ], className='row'),
            Div([
                Div([
                    Div([
                        Div([Span('Frq/Rnk', className='input-group-text')], className='input-group-prepend'),
                        Div([dcc.Slider(id='{0}-scaling'.format(id_prefix), value=0.5, min=0, max=1, step=0.01, marks={0: '0', 1: '1'})], className='form-control pb-0'),
                    ], className='input-group mb-2')
                ], className='col-lg-6 col-md-6'),
                Div([
                    Div([
                        Div([Span('Max Words', className='input-group-text')], className='input-group-prepend'),
                        dcc.Input(id='{0}-nwords'.format(id_prefix), value=200, inputmode='numeric', type='number', min=10, max=500, step=10, className='form-control'),
                    ], className='input-group mb-2')
                ], className='col-lg-6 col-md-6')
            ], className='row'),
            Div([
                Div([
                    Div([
                        Div([Span('Mask URL', className='input-group-text')], className='input-group-prepend'),
                        dcc.Input(id='{0}-image-mask-url'.format(id_prefix), value=default_mask,
                        inputmode='text', type='search', className='form-control'),
                    ], className='input-group mb-2')
                ], className='col-lg-8 col-md-6'),
                Div([
                    Button('Generate', className="btn btn-success", n_clicks=1, id='{0}-generate-wordcloud'.format(id_prefix))
                ], className='col-lg-2 col-md-2 mb-2'),
                Div([
                    A('Save', download='wordcloud.png', href="", target="_blank", className="btn btn-primary", id='{0}-save-wordcloud'.format(id_prefix))
                ], className='col-lg-2 col-md-2 mb-2')
            ], className='row')
        ], className='col-lg-6'),
        Div([
            Details([
                Summary('Help'),
                dcc.Markdown(instructions)
            ], className='col-sm-12')
        ])
    ], className='row')

    return c

def make_word_cloud(imagemaskurl, relative_scaling, nwords, text, title,
                    customstopwords, width, height, color, colormap, maxfont,
                    minfont, scale):
    if imagemaskurl is not None and imagemaskurl != '':
        # imgstr = re.search(r'base64,(.*)', imagemask).group(1)
        try:
            if imagemaskurl.startswith('data:image'):
                imgstr = re.search(r'base64,(.*)', imagemask).group(1)
                b = base64.b64decode(imgstr)
            else:
                r = requests.get(imagemaskurl)
                b = r.content
            image_bytes = io.BytesIO(b)
            im = Image.open(image_bytes).convert('RGBA')
            canvas = Image.new('RGBA', im.size, (255, 255, 255, 255))
            canvas.paste(im, mask=im)
            mask = np.array(canvas)
            width, height = im.size
        except:
            mask = None
            text = 'Invalid Image Mask!'
    else:
        mask = None
    from wordcloud import STOPWORDS
    STOPWORDS = list(STOPWORDS)

    for word in customstopwords:
        STOPWORDS.append(word)
        STOPWORDS.append(word + 's')
        STOPWORDS.append(word + "'s")
    if color == '':
        color = None
    cloud = WordCloud(width=width, height=height, mask=mask, background_color=color,
                      stopwords=STOPWORDS, max_words=nwords, colormap=colormap,
                      max_font_size=maxfont, min_font_size=minfont,
                      random_state=42, scale=scale, mode='RGBA',
                      relative_scaling=relative_scaling).generate(text)
    try:
        coloring = ImageColorGenerator(mask)
        cloud.recolor(color_func=coloring)
    except:
        pass
    image = cloud.to_image()

    print(image.size)
    byte_io = io.BytesIO()
    image.save(byte_io, 'PNG')
    byte_io.seek(0)
    data_uri = base64.b64encode(byte_io.getvalue()).decode('utf-8').replace('\n', '')
    src = 'data:image/png;base64,{0}'.format(data_uri)
    x = np.array(list(cloud.words_.keys()))
    y = np.array(list(cloud.words_.values()))
    order = np.argsort(y)[::-1]
    x = x[order]
    y = y[order]
    trace = go.Bar(x=x, y=y)
    layout = go.Layout(margin=go.Margin(l=10, r=00),
                       title='Relative frequency of words/bigrams')
    fig = go.Figure(data=[trace], layout=layout)
    children = [
        H2(title, className='card-title'),
        Img(src=src, width=image.size[0], height=image.size[1],
            style={'max-width': '100%', 'height': 'auto',
                   'margin': '0 auto', 'display': 'block'}),
        dcc.Graph(id='word-freq', figure=fig, config={'displayModeBar': False})
    ]

    return children

footer = Div([
        Div([
            'This web app is powered by Dash and WordCloud.'
        ], className='container')
    ], className='footer', style={'margin-top': 200})