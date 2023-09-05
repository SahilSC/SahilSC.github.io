from flask import Flask, render_template, send_from_directory

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "static/files"

@app.route('/')
def mainpage():
    return render_template('index.html')
@app.route('/contactinfo.html')
def contactwebpage():
    return render_template('contactinfo.html')

@app.route('/hobbies.html')
def hobbies():
    return render_template('hobbies.html')

@app.route('/download')
def download():
    return send_from_directory(app.config['UPLOAD_FOLDER'],"Resume.pdf", as_attachment=True)

if __name__=='__main__':
    app.run(debug=True)