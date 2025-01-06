import pytesseract
import streamlit as st
from PIL import Image
import os

port = int(os.environ.get("PORT", 8501))

# Title of the app
st.title("OCR Image to Text Extractor")

# File uploader for images
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Load the image
    image = Image.open(uploaded_file)

    # Display the uploaded image
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Perform OCR using pytesseract
    with st.spinner("Extracting text..."):
        extracted_text = pytesseract.image_to_string(image)

    # Display the extracted text
    st.subheader("Extracted Text:")
    st.text_area("Extracted Text:", extracted_text, height=200)

# Add instructions
st.info("Upload an image containing text, and the app will extract the text for you.")

# Footer
st.write("Powered by [Streamlit](https://streamlit.io) and [Tesseract OCR](https://github.com/tesseract-ocr)")
