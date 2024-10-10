# Image Generator WebApp with Google Vertex AI

This repository, `image-generator-webApp-google-vertex-ai`, contains a web application powered by **Google Vertex AI** that generates AI-driven images based on user prompts. The web application is designed with a clean, responsive front-end and integrates Google’s advanced machine learning models on the back-end. Users can customize the number of images, their size, and the input prompt, with generated images displayed directly on the webpage.

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

- **AI-Powered Image Generation**: Generates images using Google's Vertex AI image generation models based on user-provided prompts.
- **Real-Time Image Display**: Images are generated and displayed on the web page instantly in base64 format, removing the need for file storage.
- **Customization Options**: Users can customize:
  - The number of images to generate (up to 5)
  - Image size (512x512, 1024x1024, or 2048x2048)
  - Text prompt describing the desired image
- **Error Handling**: Provides clear error messages, including handling for API rate limits or when out of credits.
- **Responsive and User-Friendly Design**: The application features a clean, professional UI inspired by Apple’s design principles, optimized for desktop and mobile use.

## Technologies Used

### Frontend:

- **HTML5** and **CSS3**: For a responsive and clean user interface.
- **JavaScript**: For form handling, sending API requests, and displaying results.
- **Base64 Encoding**: For directly displaying images in the browser without the need for file storage.

### Backend:

- **Flask**: Python web framework used to handle API requests and integration with Google Vertex AI.
- **Google Vertex AI**: For AI-driven image generation.

## Installation

### Prerequisites

1. **Google Cloud Account**: Set up your Google Cloud account with billing enabled.
2. **Google Cloud Project**: Create a project on Google Cloud and enable the **Vertex AI API**.
3. **Python 3.8+**: Ensure you have Python installed locally.

### 1. Clone the Repository

```bash
git clone https://github.com/prathamkuril/image-generator-webApp-google-vertex-ai.git
cd image-generator-webApp-google-vertex-ai
```
