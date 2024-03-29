from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, session
import os

# app = Flask(__name__, static_folder='static', static_url_path='')
app = Flask(__name__, template_folder='.')
app.config['SECRET_KEY'] = "213123"
app.config['UPLOAD_FOLDER'] = "static/files"

@app.route('/')
def mainpage():
    return render_template('index.html')

@app.route('/contactinfo')
def contactwebpage():
    return render_template('contactinfo.html')

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')

@app.route('/download')
def download(): 
    uploads = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory = uploads, path = "resume.pdf", as_attachment=True)

if __name__=='__main__':
    app.run(debug=True)