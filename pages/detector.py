#Apps de realidad virtual  
# #Haarcascade_frontalface

# apps de realidad virtual

import numpy as np
import cv2
from PIL import Image, ImageEnhance
import streamlit as st
import os

rostrocascade =cv2.CascadeClassifier("archivoxml/detectarostro.xml")

def detectar_rostro(new_image):
    nueva_imagen = np.array(new_image.convert("RGB"))
    img = cv2.cvtColor(nueva_imagen, 1)
    gris = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    rostro = rostrocascade.detectMultiScale(gris,1.1,4)
    for (ejex,ejey,ancho,alto) in rostro:
        cv2.rectangle(img,(ejex,ejey),(ejex+ancho,ejey+alto),(255,0,0),2)
    return img,rostro

def imagen_cannys(new_image):
    nueva_imagen = np.array(new_image.convert("RGB"))
    img =cv2.cvtColor(nueva_imagen,1)
    img = cv2.GaussianBlur(img,(11,11),0)
    bordes = cv2.Canny(img, 50, 70)
    return bordes


@st.cache

def cargar_imagen(img):
    imagen = Image.open(img)
    return imagen

def principal():
    st.set_page_config(page_title="Deteccion de imágenes", page_icon=":smile:", layout="wide")  # confi de la pagina
    st.title("Inteligencia Artificial")
    st.text("Machine Learning")
    actividades = ["Detectar", "Quienes Somos"]


    eleccion = st.sidebar.selectbox("Selecciona una opcion", actividades)

    if eleccion == "Detectar":
        st.subheader("Detectando Rostros")
        # Variable para cargar imagene
        archivo_img = st.file_uploader("Subir imagen", type=["jpg", "png", "jpeg", "gif"])  # 2 parametros
    if archivo_img is not None:
        new_image = Image.open(archivo_img)
        st.text("Imagen principal")
        st.image(new_image)
    tipo_formato = st.sidebar.radio("Estilos de formato",["original","Escala-Gris","Contraste","Brillante","Transparente"])
    if tipo_formato == "Escala-Gris":
        nueva_imagen = np.array(new_image.convert("RGB"))
        img = cv2.cvtColor(nueva_imagen,1)
        color_gris =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #st.write(nueva_imagen)
        st.image(color_gris)
    elif tipo_formato == "Contraste":
        radio_contraste = st.sidebar.slider("Contraste",0.5,4.5)
        formato_contraste = ImageEnhance.Contrast(new_image)
        imagen_contraste = formato_contraste.enhance(radio_contraste)
        st.image(imagen_contraste)
    elif tipo_formato == "Brillante":
        radio_brillante = st.sidebar.slider("Brillo",0.5,4.5)
        formato_brillo = ImageEnhance.Brightness(new_image)
        imagen_brillo = formato_brillo.enhance(radio_brillante)
        st.image(imagen_brillo)
    elif tipo_formato == "Transparente":
        nueva_imagen = np.array(new_image.convert("RGB"))
        radio_transparente = st.sidebar.slider("Transparente", 0.5, 10.5)
        img = cv2.cvtColor(nueva_imagen,1)
        imagen_transparente = cv2.GaussianBlur(img,(11,11),radio_transparente)
        st.image(imagen_transparente)
    animaciones = ["rostro","canny"]
    escoger_animacion = st.sidebar.selectbox("Elige una animacion",animaciones)
    if st.button("Procesar"):
        if escoger_animacion == "rostro":
            resultado_imagen,resultado_rostro = detectar_rostro(new_image)
            st.image(resultado_imagen)
            st.success("{} rostros encontrados".format(len(resultado_rostro)))
        elif escoger_animacion =="canny":
            resultado_imagen = imagen_cannys(new_image)
            st.image(resultado_imagen)


    #elif eleccion == "Quienes Somos":
    #    st.subheader("Soy ingenierio electrico")



if __name__ == "__main__":
    principal()