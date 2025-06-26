from flask import Flask, request, render_template
from cartoonify import cartoonify_image
import os
import cv2

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_DIR = os.path.abspath(os.path.join(BASE_DIR, '../templates'))
STATIC_DIR = os.path.abspath(os.path.join(BASE_DIR, '../static'))

UPLOAD_FOLDER = os.path.join(STATIC_DIR, 'uploads')
RESULT_FOLDER = os.path.join(STATIC_DIR, 'results')

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["image"]
        if file.filename == "":
            return "No file selected"

        # Save uploaded image
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        # Generate cartoon image
        cartoon = cartoonify_image(filepath)
        image_name = "cartoon_" + file.filename
        result_path = os.path.join(app.config["RESULT_FOLDER"], image_name)
        cv2.imwrite(result_path, cartoon)

        return render_template("index.html", image_name=image_name, uploaded=True)

    return render_template("index.html", uploaded=False)

if __name__ == "__main__":
    app.run(debug=True)
