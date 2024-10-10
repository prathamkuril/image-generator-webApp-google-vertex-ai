# Image Generator WebApp with Google Vertex AI

Hey! This is a web app I built that uses **Google Vertex AI** to generate images based on custom text prompts. The frontend is simple, responsive, and easy to use, while the backend integrates directly with Vertex AI's image generation models. You can customize everything—prompt, number of images, size—and see the results directly in your browser.

## Table of Contents

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Running the Application](#running-the-application)
6. [Deployment](#deployment)
7. [Project Structure](#project-structure)
8. [License](#license)

## Features

- **AI-Driven Image Generation**: The app generates images using Vertex AI’s machine learning models, driven by the prompt you enter.
- **Real-Time Image Display**: Images show up directly on the webpage in real time—no saving, no downloads.
- **Customizable Inputs**: Choose how many images you want (up to 5), set the size (512x512, 1024x1024, or 2048x2048), and describe what you want.
- **Error Handling**: If something goes wrong (like hitting the API limit), you'll get a clear error message, so you know exactly what happened.
- **Responsive, User-Friendly Design**: Clean, professional UI that works well on both desktop and mobile.

## Technologies Used

### Frontend:

- **HTML5** and **CSS3**: For a clean and responsive UI.
- **JavaScript**: To handle the form, fetch data from the API, and display results.
- **Base64 Image Encoding**: The images are encoded and displayed directly on the page, which speeds things up.

### Backend:

- **Flask**: The Python framework that handles API requests and sends them to Google Vertex AI.
- **Google Vertex AI**: This is the brain behind the app—it generates the images from the prompts.

## Installation

### Prerequisites

1. **Google Cloud Account**: You'll need this to set up Vertex AI.
2. **Google Cloud Project**: Create a project and enable **Vertex AI API**.
3. **Python 3.8+**: Make sure you have Python installed.

### 1. Clone the Repo

```bash
git clone https://github.com/prathamkuril/image-generator-webApp-google-vertex-ai.git
cd image-generator-webApp-google-vertex-ai
```
