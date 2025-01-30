import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")

with st.expander("Upload image"):
    uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start camera"):
    # Start the camera
    camera_image = st.camera_input("Camera")

def show_image(image):
    # Create a pillow image instance
    img = Image.open(image)
    # Convert the pillow image to grayscale
    gray_img = img.convert("L")
    # Render the grayscale image on the webpage
    st.image(gray_img)

if camera_image:
    show_image(camera_image)

if uploaded_image:
    show_image(uploaded_image)