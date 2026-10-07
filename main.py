from flask import Flask, request, jsonify, render_template
import qrcode
from io import BytesIO
import base64
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    # Use render_template to serve the index.html file from the templates folder
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    payload = request.json
    qr_data = payload.get('data') or payload.get('url')
    resolution = payload.get('resolution', 'medium')
    
    if not qr_data:
        return jsonify({'error': 'Data is required'}), 400
        
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10, # Base size
        border=2,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    
    # Generate the QR Code image
    qr_img = qr.make_image(fill_color="#0f172a", back_color="white") 
    
    # Extract the original PIL Image object
    pil_img = qr_img.get_image()
    
    # Define exact pixel sizes
    sizes = {
        'small': 500,        # 500x500
        'medium': 1000,      # 1000x1000
        'large': 4000,       # 4000x4000
        'extra_large': 10000 # 10000x10000
    }
    target_size = sizes.get(resolution, 1000)
    
    # Resize using NEAREST method to keep the QR Code boxes sharp (no blur/anti-aliasing)
    pil_img = pil_img.resize((target_size, target_size), Image.NEAREST)
    
    # Save image to bytes buffer
    buffered = BytesIO()
    pil_img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    
    return jsonify({'image': f'data:image/png;base64,{img_str}'})

if __name__ == '__main__':
    print("Starting DBS QR Studio Server...")
    app.run(debug=True, port=5000)
