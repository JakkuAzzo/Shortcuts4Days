from flask import Flask, request, render_template
import os

app = Flask(__name__)

# This is insecure! Do not use in production!
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'File uploaded successfully.'

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
