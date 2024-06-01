from flask import Flask, request, render_template, redirect, url_for, jsonify
from PIL import Image
import pytesseract
import os
import base64
from io import BytesIO

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/', methods=['GET', 'POST'])
def index():
    extracted_text = ""
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            extracted_text = extract_text(file_path)
    return render_template('index.html', extracted_text=extracted_text)

@app.route('/upload_paste', methods=['POST'])
def upload_paste():
    data = request.json
    if 'image' in data:
        image_data = data['image']
        image_data = image_data.split(",")[1]
        image = Image.open(BytesIO(base64.b64decode(image_data)))
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'pasted_image.png')
        image.save(image_path)
        extracted_text = extract_text(image_path)
        return jsonify({'extracted_text': extracted_text})
    return jsonify({'error': 'No image data received'}), 400

def extract_text(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
