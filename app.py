import streamlit as st
from PIL import Image

image = Image.open("PerritoConSombrero.jpeg")
image2 = Image.open("Perrito que mira de lado.jpg")
image3 = Image.open("Perrito feliz.jpeg")
image4 = Image.open("Perritos amigos.jpg")
st.title ("Perrito con sombrero")

st.header ("Aquí voy a poner un perrito con sombrero")
st.write("Porque me gustan mucho los perritos")

st.image(image, caption = "Perrito con sombrero")

texto = st.text_input ("Escribe algo","Este es mi texto")
st.write("El texto escrito es", texto)

st.subheader("Ahora 2 columnas")
col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Los perritos son la cosa más bacana")
  resp = st.checkbox("Estoy de acuerdo")
  if resp:
    st.write("HELL YEAH")

with col2:
  st.subheader("Esta es la segunda columna")
  modo = st.radio("¿Cuál es tu perrito favorito?", ("Perrito mirando feo", "Perrito feliz", "Perritos amigos"))
  if modo == "Perrito mirando feo" :
    st.write("Tu favorito es el perrito mirando feo")
    st.image(image2, caption = "Perrito con sombrero")
  if modo == "Perrito feliz" :
    st.write("Tu favorito es el perrito feliz")
    st.image(image3, caption = "Perrito con sombrero")
  if modo == "Perritos amigos" :
    st.write("Tu favorito son los perritos amigos")
    st.image(image4, caption = "Perrito con sombrero")
