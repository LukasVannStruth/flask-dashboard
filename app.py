from flask import Flask, render_template, url_for
import os
from __init__ import __version__

app = Flask(__name__)

template_dir = os.path.join(os.getcwd(), 'templates')
index_file = os.path.join(template_dir, 'index.html')


envvars = {}


@app.route("/")
def render_index():
    stylefile_path = url_for('static', filename='styles.css')


    # define envvars for the page
    envvars["stylesheet"] = stylefile_path 
    envvars["version"] = __version__

    return render_template('index.html', envvars=envvars)
    
