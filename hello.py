import os
from flask import Flask, url_for, render_template
from flask_compress import Compress
from flask_scss import Scss

app = Flask(__name__)
Scss(app)
Scss(app, static_dir='static', asset_dir='assets')
Compress(app)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
