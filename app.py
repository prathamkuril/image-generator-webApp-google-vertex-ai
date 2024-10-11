import os
import logging
from flask import Flask, request, jsonify
import vertexai
from vertexai.preview.vision_models import ImageGenerationModel
from google.auth import default
from google.auth.exceptions import DefaultCredentialsError
from google.oauth2 import service_account
from io import BytesIO
import base64
from datetime import datetime

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Attempt to fetch credentials from environment variables or use service account JSON
SERVICE_ACCOUNT_FILE = os.getenv('SERVICE_ACCOUNT_FILE', 'service-account.json')

try:
    if 'GOOGLE_APPLICATION_CREDENTIALS' in os.environ:
        credentials, project = default()
        logging.info("Using credentials from environment variables.")
    else:
        credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)
        logging.info("Using service account credentials from JSON file.")
except DefaultCredentialsError as e:
    logging.error("No valid credentials found. Please set up Google Cloud API credentials properly.")
    raise e

# Initialize Vertex AI with credentials
vertexai.init(credentials=credentials)

@app.route('/')
def index():
    """Return a status message indicating that the API is running."""
    return "Google Cloud Vertex AI Image Generator API is running."

@app.route('/generate-image', methods=['POST'])
def generate_image():
    """
    Generate images using the Vertex AI image generation model.

    This endpoint expects a POST request with three form data fields:

    - prompt: The text prompt to generate images from.
    - num_images: The number of images to generate. Defaults to 1.
    - image_size: The size of the generated images. Defaults to 512x512.

    The function logs the request details, initializes the Vertex AI model,
    generates images, and converts them to base64. It returns a JSON response
    containing a list of image objects with the following keys:

    - image: The base64 encoded image data.
    - size: The size of the image.
    - generated_at: The timestamp when the image was generated.
    - generation_time: The time taken to generate the images in seconds.

    If the request fails, the function logs the error and returns a JSON
    response with an error message and HTTP status code 400, 500, or 503.
    """
    try:
        # Extract user inputs from the request
        prompt = request.form.get('prompt')
        num_images = int(request.form.get('num_images', 1))
        image_size = request.form.get('image_size', '512x512')

        if not prompt:
            logging.warning("Prompt is required but not provided.")
            return jsonify({'error': 'Prompt is required.'}), 400

        # Log request details
        logging.info(f"Image generation request received: Prompt='{prompt}', NumImages={num_images}, ImageSize={image_size}")

        # Initialize the Vertex AI model for image generation
        model = ImageGenerationModel.from_pretrained("imagegeneration@002")

        # Generate images
        start_time = datetime.now()
        images = model.generate_images(prompt=prompt, number_of_images=num_images, seed=1, add_watermark=False, size=image_size)
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()

        logging.info(f"Image generation completed in {duration:.2f} seconds.")

        # Convert images to base64 and return them directly
        image_data_list = []
        for image in images:
            img_buffer = BytesIO()
            image.save(img_buffer, format="JPEG")
            img_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
            image_data_list.append({
                'image': f"data:image/jpeg;base64,{img_base64}",
                'size': image_size,
                'generated_at': end_time.strftime("%Y-%m-%d %H:%M:%S"),
                'generation_time': duration
            })

        return jsonify({'image_data_list': image_data_list})

    except Exception as e:
        logging.error(f"Error during image generation: {str(e)}")
        if 'RESOURCE_EXHAUSTED' in str(e):
            return jsonify({'error': 'We ran out of credits to process the request. Please try again later.'}), 503
        return jsonify({'error': 'An API error occurred. Please try again later.'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 8080)), debug=True)
