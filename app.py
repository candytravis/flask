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

@app.route('/portrait/<name>')
def hello(name=None):
    return render_template('portrait.html', name=name)

@app.route('/templates/portrait.html')
def send_html(path):
    return send_from_directory('templates', path)


@app.route('/static/stylesheets/style.css')
def send_css(path):
    return send_from_directory('static', path)


url_for('static', filename='style.css')

app.static_folder = 'static'

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

