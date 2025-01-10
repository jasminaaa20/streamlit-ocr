import pytesseract
import streamlit as st
from PIL import Image
import os

port = int(os.environ.get("PORT", 8501))

# Page configuration
st.set_page_config(
    page_title="Streamlit OCR", 
    page_icon=":mag:"
)

# Sidebar
with st.sidebar:
    st.title("ℹ️ About")
    st.info("This app uses Tesseract OCR to extract text from images. Upload an image, and the text will be extracted for you.")
    st.write("Powered by [Streamlit](https://streamlit.io) and [Tesseract OCR](https://github.com/tesseract-ocr)")

# Title
st.title("📄 OCR Text Extractor")

# File uploader
uploaded_file = st.file_uploader(
    "📤 Upload your image (PNG, JPG, JPEG)", 
    type=["png", "jpg", "jpeg"]
)

# Example Image Button
if st.button("Use Example Image"):
    example_image_path = "test\data\example_image.png"  # Add an example image to your project folder
    uploaded_file = example_image_path

if uploaded_file:
    # Display the image and extracted text
    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    with st.spinner("Extracting text..."):
        extracted_text = pytesseract.image_to_string(image)
    st.text_area("Extracted Text", extracted_text, height=300)
    st.download_button(
        label="Download Extracted Text",
        data=extracted_text,
        file_name="extracted_text.txt",
        mime="text/plain"
    )
