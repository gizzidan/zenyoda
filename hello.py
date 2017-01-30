from flask import Flask, url_for, render_template
from flask_scss import Scss
from flask_frozen import Freezer


app = Flask(__name__)
app.config.from_pyfile('settings.py')
Scss(app)
Scss(app, static_dir='static', asset_dir='assets')
freezer = Freezer(app)



@app.route('/')
def index():
    return render_template('index.html')
