# Image to Text Extraction Application

This project is a web application that allows users to upload images or paste images using `Ctrl+V`, and then extracts the text from these images using Tesseract OCR. The application is built using Flask and is designed to be deployed on Vercel.

## Features

- Upload an image to extract text.
- Paste an image using `Ctrl+V` to extract text.
- Responsive design for different screen sizes.
- Extracted text is displayed in a textarea for easy copying.

## Technologies Used

- Flask
- Tesseract OCR
- HTML, CSS, JavaScript
- Vercel for deployment

## Project Structure


## Setup Instructions

### Prerequisites

- Python 3.x
- Flask
- pytesseract
- Pillow
- Vercel CLI

### Local Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/rohit-motwani/Image-Text.git
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    python app.py
    ```

4. Open your browser and navigate to `http://127.0.0.1:5000/` to see the application in action.

### Deployment on Vercel

1. Install Vercel CLI if you haven't already:

    ```bash
    npm install -g vercel
    ```

2. Create a `vercel.json` file in the root of your project directory with the following content:

    ```json
    {
    "version": 2,
    "builds": [
      {
        "src": "app.py",
        "use": "@vercel/python"
      },
      {
        "src": "static/**/*",
        "use": "@vercel/static"
      },
      {
        "src": "templates/**/*",
        "use": "@vercel/static"
      }
    ],
    "routes": [
      {
        "src": "/(.*)",
        "dest": "/app.py"
      }
    ],
    "env": {
      "PYTHONUNBUFFERED": "1",
      "PIP_NO_CACHE_DIR": "off",
      "PIPENV_YES": "1",
      "PIPENV_VENV_IN_PROJECT": "1"
    },
    "functions": {
      "vc_handler_python": {
        "runtime": "python3.12",
        "includeFiles": "libjpeg.so.62"
      }
    }
  }
  
    ```

3. Deploy the application:

    ```bash
    vercel
    ```

4. Follow the prompts to deploy your application. Vercel will build your project based on the configuration in `vercel.json` and deploy it.

### Usage

- **Upload an Image**: Click the "Choose an image" button, select an image, and click "Extract Text".
- **Paste an Image**: Copy an image to your clipboard, click inside the paste area, and press `Ctrl+V`.

### Breakpoints

- Mobile: `<=480px`
- Mobile (Landscape): `<=768px`
- Tablet: `<=834px`
- Tablet (Landscape): `<=1024px`
- Laptop: `<=1440px`
- Desktop: `<=1440px`

## Contributing

Feel free to submit issues or pull requests. Contributions are always welcome!

## License

This project is licensed under the MIT License.
