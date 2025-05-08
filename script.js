document.addEventListener('DOMContentLoaded', () => {
    const reviewTextarea = document.getElementById('reviewText');
    const imageInput = document.getElementById('reviewImage');
    const imagePreview = document.getElementById('imagePreview');
    const detectButton = document.getElementById('detectButton');
    const resultSection = document.getElementById('resultSection');
    const detectionResultParagraph = document.getElementById('detectionResult');

    imageInput.addEventListener('change', (event) => {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                imagePreview.innerHTML = `<img src="${e.target.result}" alt="Review Image" style="max-width: 100%; height: auto;">`;
            };
            reader.readAsDataURL(file);
        } else {
            imagePreview.innerHTML = '';
        }
    });

    detectButton.addEventListener('click', () => {
        const reviewText = reviewTextarea.value.trim();
        const imageFile = imageInput.files[0];

        if (!reviewText && !imageFile) {
            alert('Please enter a review or upload an image.');
            return;
        }
    if(reviewText&&!imageFile){
        alert('please upload an image')
    }

       
        const isFake = Math.random() < 0.75; 

        detectionResultParagraph.textContent = isFake ? 'This review is likely FAKE.' : 'This review appears to be GENUINE.';
        resultSection.classList.remove('hidden');
    });
});
detectButton.addEventListener('click', async () => {
    // ... (getting reviewText and imageFile) ...

    const formData = new FormData();
    if (reviewText) {
        formData.append('reviewText', reviewText);
    }
    if (imageFile) {
        formData.append('reviewImage', imageFile);
    }

    try {
        const response = await fetch('/detect_fake_review', {
            method: 'POST',
            body: formData,
        });

        // ... (handling the response) ...

    } catch (error) {
        // ... (handling errors) ...
    }
});