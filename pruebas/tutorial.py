import os
from flask import Flask, render_template, request, redirect, flash, url_for, request
from werkzeug.utils import secure_filename
from skimage import io
import matplotlib.pyplot as plt

lista = []
name = []

app =  Flask(__name__)
app.secret_key = b'secret'

BASE_PATH = os.path.abspath(str(os.environ.get('HOME')))
ALLOWED_EXTENSION = {'txt', 'pdf', 'jpg', 'gif', 'png'}

def allowed_files(filename: str):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files.get('file')
        ifile = io.imread(request.files.get('file'))

        if file.filename == '' :
            flash('No file was selected')
            return redirect(request.url)

        if file and allowed_files(file.filename):
            filename = secure_filename(file.filename)
            name.append(filename)
            lista.append(ifile)
            flash('File uploaded successfully')
            return redirect(url_for('download'))

    return render_template('index.html')

@app.route('/download', methods=['GET', 'POST'])
def download():
    request.environ.get('werkzeug.server.shutdown')()
    return 'Server shutting down'

if __name__ == '__main__':
    app.run(debug=False)
    plt.imshow(lista[0])
    plt.show()


