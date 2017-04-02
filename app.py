import os
from flask import Flask, render_template, send_from_directory, url_for

# initialization
app = Flask(__name__)
app.config.update(
    DEBUG = True,
)

# controllers
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name)


@app.route('/static/css/style.css')
def send_css(path):
    return send_from_directory('static', path)

app.static_folder = 'static'

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

