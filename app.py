import os
from flask import Flask, render_template

# initialization
app = Flask(__name__, static_url_path='/static/')
app.config.update(
    DEBUG = True,
)

# controllers
@app.route("/")
def index():
    return render_template('index.html')
    url_for('static', filename='css/style.css')

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)