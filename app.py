import logging
from flask import Flask, request
from PIL import Image
from tesseract.ocr import image_to_string

app = Flask(__name__)


@app.route("/convert",  methods=['POST'])
def convert():
    try:
        img = Image.open(request.files.get('image'))
        img_ocr = image_to_string()
        return img_ocr.img_to_string(img)
    except Exception as e:
        logging.error(e)
        return "Error while uploading or processing image"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
