# DBS QR Studio

DBS QR Studio is a modern, premium, and easy-to-use web application for generating high-quality QR codes. Built with Python (Flask) for the backend and a stunning Glassmorphism UI for the frontend, it allows you to generate various types of QR codes and download them in absolute resolutions (up to 10000x10000 pixels).

## Features

*   **Beautiful UI/UX**: Premium Dark Mode with Glassmorphism design and smooth animations.
*   **Multiple QR Code Types**:
    *   🔗 **Website URL**: Link to any website.
    *   📝 **Text**: Display a simple text message.
    *   📶 **Wi-Fi**: Share your wireless network connection seamlessly.
    *   📇 **vCard**: Share a digital contact card.
    *   ✉️ **Email**: Send an instant formatted email.
    *   📱 **Social Media**: Instantly link to platforms like Instagram, TikTok, YouTube, LinkedIn, Facebook, and X (Twitter) just by typing a username.
*   **Absolute High-Resolution Outputs**:
    *   Download crisp, non-blurry QR codes in precise sizes: Small (500x500), Medium (1000x1000), Large (4000x4000), and Extra Large (10000x10000).

## Tech Stack

*   **Backend**: Python, Flask, `qrcode`, `Pillow` (PIL).
*   **Frontend**: HTML5, Vanilla CSS3 (Custom Variables, Flexbox, Grid), Vanilla JavaScript.

## Installation & Setup

1. **Clone or Download the Repository**
   Make sure you are in the project directory (`qrcode_generateor`).

2. **Install Dependencies**
   The application requires Flask, `qrcode`, and Pillow to run. Install them using pip:
   ```bash
   pip install flask qrcode pillow
   ```

3. **Run the Application**
   Start the local development server by running:
   ```bash
   python main.py
   ```

4. **Access the Web Interface**
   Open your preferred web browser and navigate to:
   ```text
   http://127.0.0.1:5000
   ```

## How to Use

1. Select the type of QR Code you want to create from the options grid on the left panel.
2. Fill in the required details in the form.
3. Select your desired image resolution (Small, Medium, Large, or Extra Large) at the bottom of the form.
4. Click the **Generate QR Code** button.
5. Preview your QR code on the right panel and click **Download Image** to save it locally.

## License
This project is for personal and educational use. Feel free to modify and expand its features!
