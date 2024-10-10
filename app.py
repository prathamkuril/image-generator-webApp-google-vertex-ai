from flask import Flask, request, jsonify
import vertexai
from vertexai.preview.vision_models import ImageGenerationModel
import os
import base64
from io import BytesIO

app = Flask(__name__)

# Fetch Google Cloud project ID and region from environment variables
PROJECT_ID = os.getenv('GOOGLE_CLOUD_PROJECT_ID')
REGION = os.getenv('GOOGLE_CLOUD_REGION')

@app.route('/')
def index():
    return "Google Cloud Flask API is running"

@app.route('/generate-image', methods=['POST'])
def generate_image():
    try:
        # Get the data from the POST request
        prompt = request.form.get('prompt')
        num_images = int(request.form.get('num_images', 1))
        image_size = request.form.get('image_size', '512x512')

        if not prompt:
            return jsonify({'error': 'Prompt is required.'}), 400

        # Initialize Vertex AI using environment variables
        vertexai.init(project=PROJECT_ID, location=REGION)
        model = ImageGenerationModel.from_pretrained("imagegeneration@002")

        # Generate images based on the prompt and user selections
        images = model.generate_images(prompt=prompt, number_of_images=num_images, seed=1, add_watermark=False, size=image_size)

        # Convert images to base64 and return them directly
        image_data_list = []
        for image in images:
            img_buffer = BytesIO()
            image.save(img_buffer, format="JPEG")
            img_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
            image_data_list.append(f"data:image/jpeg;base64,{img_base64}")

        return jsonify({'image_data_list': image_data_list})

    except Exception as e:
        if 'RESOURCE_EXHAUSTED' in str(e):
            return jsonify({'error': 'We ran out of credits to process the request. Please try again later.'}), 503
        return jsonify({'error': 'An API error occurred. Please try again later.'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)), debug=True)
