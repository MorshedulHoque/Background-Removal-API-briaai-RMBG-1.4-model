from flask import Flask, request, render_template, url_for
from transformers import pipeline
import os
from PIL import Image
from datetime import datetime
import cv2

app = Flask(__name__)

# Static subdirectories for uploaded and processed images
UPLOAD_FOLDER = os.path.join(app.static_folder, 'uploads')
PROCESSED_FOLDER = os.path.join(app.static_folder, 'processed')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {'png', 'jpg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file and allowed_file(file.filename):
            # Sanitize the original filename
            original_filename = file.filename.replace(" ", "_")
            # Generate a timestamp
            timestamp = int(datetime.now().timestamp())
            # Create a new filename with the timestamp
            new_filename = f"{timestamp}_{original_filename}"

            # Save the uploaded image
            file_path = os.path.join(UPLOAD_FOLDER, new_filename)
            file.save(file_path)

            # Convert PNG image to RGB format
            img = Image.open(file_path)
            img = img.convert('RGB')
            img.save(file_path)

            # Process the image to remove the background
            pipe = pipeline("image-segmentation", model="briaai/RMBG-1.4", trust_remote_code=True)
            pillow_mask = pipe(file_path, return_mask=True)
            pillow_image = pipe(file_path)  # Apply mask on input and return a pillow image

            # Define the processed file path with PNG extension and the new filename
            processed_filename = f"{timestamp}_{os.path.splitext(original_filename)[0]}_removed.png"
            processed_file_path = os.path.join(PROCESSED_FOLDER, processed_filename)
            
            # Save the processed image in PNG format
            pillow_image.save(processed_file_path)

            # Generate URLs for the uploaded and processed images
            uploaded_img_url = url_for('static', filename=f'uploads/{new_filename}')
            processed_img_url = url_for('static', filename=f'processed/{processed_filename}')

            # Render a template to display both images
            return render_template('show_images.html', uploaded_img_url=uploaded_img_url, processed_img_url=processed_img_url)
        else:
            return 'Only PNG and JPG files are allowed'

    return render_template('show_images.html')

if __name__ == '__main__':
    app.run(debug=True)
