from flask import Flask, request, jsonify
from PIL import Image
import io
import random
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configure upload folder (optional)
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed image extensions (optional)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/detect_fake_review', methods=['POST'])
def detect_fake_review():
    if 'reviewText' not in request.form and 'reviewImage' not in request.files:
        return jsonify({'error': 'No review text or image provided'}), 400

    review_text = request.form.get('reviewText', '')
    image_file = request.files.get('reviewImage')

    image_data = None
    if image_file and allowed_file(image_file.filename):
        try:
            image = Image.open(io.BytesIO(image_file.read()))
            # Here you might perform image analysis using your ML model
            image_data = "Image data received and processed (simulated)"
            # Optionally save the image
            filename = secure_filename(image_file.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        except Exception as e:
            return jsonify({'error': f'Error processing image: {str(e)}'}), 400
    elif image_file:
        return jsonify({'error': 'Invalid image file type'}), 400

    # --- Here is where your actual fake review detection logic would go ---
    # You would use your trained ML model to analyze:
    # - review_text (natural language processing)
    # - image_data (image feature extraction and analysis)
    # - potentially combine the results

    # Simulate a detection result
    is_fake = random.random() < 0.6  # Simulate higher probability of fake for demo
    confidence = random.uniform(0.7, 0.95) if is_fake else random.uniform(0.1, 0.3)

    result = {
        'is_fake': is_fake,
        'confidence': confidence,
        'analysis': 'Simulated analysis based on received data.'
    }
    

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
    