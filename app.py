import streamlit as st
from PIL import Image
st.title ("Perrito con sombrero")

st.header ("Aquí voy a poner un perrito con sombrero")
st.write("Porque me gustan mucho los perritos")
image = Image.open("PerritoConSombrero.jpeg")
st.image(image, caption = "Perrito con sombrero")
