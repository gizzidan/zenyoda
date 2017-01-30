from flask import Flask, url_for, render_template
from flask_scss import Scss


app = Flask(__name__)
Scss(app)
Scss(app, static_dir='static', asset_dir='assets')


@app.route('/')
def index():
    return render_template('index.html')
