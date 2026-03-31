import streamlit as st
from PIL import Image, ImageDraw

st.title("✅ Connection Test")

# Create a blank image
img = Image.new("RGB", (200, 200), "white")
draw = ImageDraw.Draw(img)

# Draw a black square
draw.rectangle([50, 50, 150, 150], fill="black")

# Show the image
st.image(img, caption="Black square = success ✅")
