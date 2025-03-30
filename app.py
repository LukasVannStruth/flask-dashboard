from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

template_dir = os.path.join(os.getcwd(), 'templates')
index_file = os.path.join(template_dir, 'index.html')



@app.route("/")
def render_index():
    stylefile_path = url_for('static', filename='styles.css')
    return render_template('index.html', stylesheet=stylefile_path)
    
