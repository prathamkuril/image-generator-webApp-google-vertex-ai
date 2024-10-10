document.getElementById('image-generator-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(this);
  
    fetch('https://your-cloud-run-url.com/generate-image', {
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
  
        data.image_data_list.forEach(base64Image => {
          const img = document.createElement('img');
          img.src = base64Image;
          imagesContainer.appendChild(img);
        });
      }
    })
    .catch(error => {
      const errorMessage = document.getElementById('error-message');
      errorMessage.style.display = 'block';
      errorMessage.querySelector('p').textContent = 'An error occurred while generating images. Please try again.';
    });
  });
  