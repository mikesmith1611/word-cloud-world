
from flask import Flask, send_from_directory
from dash import Dash

class CustomDashIndex(Dash):
    def index(self, *args, **kwargs):  # pylint: disable=unused-argument
        scripts = self._generate_scripts_html()
        css = self._generate_css_dist_html()
        config = self._generate_config_html()
        title = getattr(self, 'title', 'Dash')
        return '''
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="UTF-8">
                <title>{}</title>
                {}
                <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
                <script>
                (adsbygoogle = window.adsbygoogle || []).push({{
                    google_ad_client: "ca-pub-8733001003187835",
                    enable_page_level_ads: true
                }});
                </script>
            </head>
            <body>
                <div id="react-entry-point">
                    <div class="_dash-loading">
                        Loading...
                    </div>
                </div>
                <footer>
                    {}
                    {}
                </footer>
            </body>
        </html>
        '''.format(title, css, config, scripts)


server = Flask(__name__, static_folder='static')
app = CustomDashIndex(server=server)

app.css.append_css({'external_url': "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"})
app.css.append_css({'external_url': "/static/custom.css"})

app.scripts.append_script({'external_url': "https://code.jquery.com/jquery-3.3.1.slim.min.js"})
app.scripts.append_script({'external_url': "https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"})
app.scripts.append_script({'external_url': "https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"})

app.config.suppress_callback_exceptions = True


@server.route('/static/<path:path>')
def serveStaticPath(path):
    send_from_directory(os.path.join(server.root_path, 'static'))