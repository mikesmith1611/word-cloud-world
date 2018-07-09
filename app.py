
from flask import Flask, send_from_directory
from dash import Dash

server = Flask(__name__, static_folder='static')
app = Dash(server=server)

app.css.append_css({'external_url': "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"})
app.css.append_css({'external_url': "/static/custom.css"})

app.scripts.append_script({'external_url': "https://code.jquery.com/jquery-3.3.1.slim.min.js"})
app.scripts.append_script({'external_url': "https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"})
app.scripts.append_script({'external_url': "https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"})

app.config.suppress_callback_exceptions = True


@server.route('/static/<path:path>')
def serveStaticPath(path):
    send_from_directory(os.path.join(server.root_path, 'static'))