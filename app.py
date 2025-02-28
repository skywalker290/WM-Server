import os
from gemini_stable import *
from functions import download_image
from flask import Flask, request, jsonify
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100 MB

# Enable CORS for all routes
CORS(app, resources={r"/fileupload": {"origins": "*"},r"/scan": {"origins": "*"}})


if not os.path.exists('Images'):
    os.makedirs('Images')

@app.route('/')
def home():
    return jsonify({"hello":"Water Meter Here!"})

@app.route('/urlupload', methods=['POST'])
def upload_image():
    image_url = request.json.get('image_url')
    if image_url:
        image_path = download_image(image_url)
        if not image_path:
            return jsonify({"error": "Failed to download image"}), 400
        return jsonify({"output": "Image uploaded successfully"}), 200
    return jsonify({"error": "Image URL not provided"}), 400


@app.route('/fileupload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    # Save the image to the 'Images' folder
    image_path = os.path.join('Images', file.filename)
    file.save(image_path)

    # Respond with the image name for further processing
    print(file.filename)
    return jsonify({"image_name": file.filename}), 200

@app.route('/scan',methods = ['POST'])
def inference():
    image_name = request.json.get('image_name')
    image_path = os.path.join('Images', image_name)
    image_name = "water01.jpeg"
    
    if image_path:
        reading = gemini(image_path)
        if type(reading) is str:
            return jsonify({"reading": int(reading)}), 200
            # return str(reading)
        else:
            return jsonify({"Error":reading}), 400 
    else:
        return jsonify({"error": "Image Not Found"}), 400
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)

