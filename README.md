# Background Removal API | briaai-RMBG-1.4-model

## Description

This API allows users to remove the background from an image using a pre-trained model from Hugging Face called "RMBG-1.4". The API is built using Flask and can handle image uploads, process them to remove the background, and return the resulting image. Additionally, both the original and transformed images are saved on the server with UNIX timestamps for easy tracking and management.

## Features

- **Image Upload:** Users can upload an image via the API.
- **Background Removal:** Utilizes the "RMBG-1.4" model from Hugging Face to remove the background from the uploaded image.
- **Image Saving:** Both the original and the processed images are saved on the server with UNIX timestamps.
- **API Integration:** Can be easily integrated into any background removal project.

## Technologies Used

- **Flask:** For creating the web API.
- **Transformers:** For loading and using the "RMBG-1.4" model.
- **PIL (Pillow):** For handling image processing.
- **OpenCV:** For additional image processing.
- **Datetime:** For generating UNIX timestamps for saved images.

## Usage

1. **Image Upload:** Users can upload an image through the API endpoint.
2. **Background Removal:** The API processes the image to remove the background.
3. **Receive Processed Image:** The processed image with the background removed is returned to the user.
4. **Image Saving:** Both the original and the transformed images are saved on the server with UNIX timestamps.

