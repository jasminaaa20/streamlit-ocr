# Streamlit OCR Image Text Extractor

This is a web-based application that allows users to upload an image containing text and extract the text using Optical Character Recognition (OCR) technology. The application is built with [Streamlit](https://streamlit.io) and uses [Tesseract OCR](https://github.com/tesseract-ocr) for text extraction.

## Features

- Upload images in PNG, JPEG, or JPG formats.
- Extract text from images using Tesseract OCR.
- Simple and interactive web interface.
- Dockerized for easy deployment.

---

## Prerequisites

- **Python 3.9+**
- **Tesseract OCR**

### Installing Tesseract OCR

#### Windows
1. Download the installer from the [UB Mannheim Tesseract page](https://github.com/UB-Mannheim/tesseract/wiki).
2. Install the application and add the installation directory to your `PATH` environment variable.
3. Verify installation:
   ```bash
   tesseract --version
   ```

#### macOS
1. Install via Homebrew:
   ```bash
   brew install tesseract
   ```
2. Verify installation:
   ```bash
   tesseract --version
   ```

#### Linux
1. Install via the package manager:
   ```bash
   sudo apt update
   sudo apt install tesseract-ocr
   ```
2. Verify installation:
   ```bash
   tesseract --version
   ```

---

## Local Development

### Clone the Repository
```bash
git clone https://github.com/jasminaaa20/streamlit-ocr.git
cd streamlit-ocr
```

### Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Run the Application
```bash
streamlit run main.py
```

Visit `http://localhost:8501` in your browser to use the app.

---

## Docker Deployment

### Build the Docker Image
```bash
docker build -t streamlit-ocr .
```

### Run the Docker Container
```bash
docker run -p 8501:8501 streamlit-ocr-app
```

Access the app at `http://localhost:8501`.

---

## Deploy to Google Cloud Run

### Prerequisites
- Install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/install).
- Authenticate with your Google Cloud account:
  ```bash
  gcloud auth login
  ```
- Enable the Cloud Run API:
  ```bash
  gcloud services enable run.googleapis.com
  ```

### Steps to Deploy

1. **Build and Push the Image to Google Container Registry**
   ```bash
   gcloud builds submit --tag gcr.io/<PROJECT-ID>/streamlit-ocr-app
   ```

2. **Deploy to Cloud Run**
   ```bash
   gcloud run deploy streamlit-ocr-app \
       --image gcr.io/<PROJECT-ID>/streamlit-ocr-app \
       --platform managed \
       --region <REGION> \
       --allow-unauthenticated
   ```

   Replace `<PROJECT-ID>` with your Google Cloud project ID and `<REGION>` with your desired region.

3. **Access the Application**
   After deployment, you’ll receive a URL to access your app.

---

## Application Structure

```
.
├── Dockerfile           # Docker configuration file
├── requirements.txt     # Python dependencies
├── app.py               # Streamlit application
├── README.md            # Documentation
```

---

## Technologies Used

- **Streamlit**: For building the web interface.
- **Tesseract OCR**: For text extraction from images.
- **Docker**: For containerization.
- **Google Cloud Run**: For deployment.

---

## License

TBD

---

## Author

[Akmal Ali Jasmin](https://github.com/jasminaaa20)

Feel free to contribute or raise issues in the repository. Enjoy extracting text from images!

