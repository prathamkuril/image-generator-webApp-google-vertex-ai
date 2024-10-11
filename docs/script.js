document.getElementById('image-generator-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(this);
  
    fetch('https://ai-image-app-67890-ew.s9a.run.app/generate-image', {
        method: 'POST',
        body: formData
      })
      
    .then(response => response.json())
    .then(data => {
      const errorMessage = document.getElementById('error-message');
      errorMessage.style.display = 'none'; // Hide any previous errors
  
      if (data.error) {
        errorMessage.style.display = 'block'; // Display error message
        errorMessage.querySelector('p').textContent = data.error;
      } else {
        const imagesContainer = document.getElementById('images-container');
        imagesContainer.innerHTML = ''; // Clear existing images
  
        data.image_data_list.forEach(imageData => {
          const img = document.createElement('img');
          img.src = imageData.image;
          imagesContainer.appendChild(img);
  
          // Display image generation details (size, generation time, etc.)
          const imgDetails = document.createElement('p');
          imgDetails.textContent = `Generated at: ${imageData.generated_at}, Size: ${imageData.size}, Time: ${imageData.generation_time} seconds`;
          imagesContainer.appendChild(imgDetails);
        });
      }
    })
    .catch(error => {
      const errorMessage = document.getElementById('error-message');
      errorMessage.style.display = 'block';
      errorMessage.querySelector('p').textContent = 'An error occurred while generating images. Please try again.';
    });
  });
  