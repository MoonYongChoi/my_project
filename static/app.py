from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)


@app.route('/')
def render_file():
    return render_template('index.html')

@app.route('/fileUpload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('./uploads/' + secure_filename(f.filename))
        return render_template('index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
