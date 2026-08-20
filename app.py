import streamlit as st
from PIL import Image
st.title ("Perrito con sombrero")

st.header ("Aquí voy a poner un perrito con sombrero")
st.write("Porque me gustan mucho los perritos")
image = Image.open("PerritoConSombrero.jpeg")
st.image(image, caption = "Perrito con sombrero")

texto = st.text_input ("Escribe algo","Este es mi texto")
st.write("El texto escrito es", texto)

st.subheader("Ahora 2 columnas")
col1, col2 = st.columns(2)
