import streamlit as st
import numpy as np
from PIL import Image
import cv2

def imagen_cannys(new_image, canny_threshold):
    img = np.array(new_image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    img = cv2.GaussianBlur(img, (11, 11), 0)
    bordes = cv2.Canny(img, canny_threshold, canny_threshold * 2)
    return bordes

def main():
    st.title("Aplicación de Canny")
    st.sidebar.header("Configuración")

    # Cargamos  la imagen con manejo de errores
    uploaded_image = st.file_uploader("Cargar imagen", type=["jpg", "jpeg", "png","gif"])
    if uploaded_image is None:
        st.sidebar.warning("Por favor, carga una imagen.")
        return

    # Convertimos  el objeto UploadedFile a un objeto de imagen utilizando PIL
    with Image.open(uploaded_image) as pil_image:
        # Mostramos  la imagen original
        st.image(pil_image, caption="Imagen Original", use_column_width=True, channels="RGB")

        # Configuraramos  el slider en el sidebar
        canny_threshold = st.sidebar.slider("Algoritmo  de Canny", min_value=0, max_value=255, value=50)

        # Aplicamos  el algoritmo de Canny
        edges = imagen_cannys(pil_image, canny_threshold)

        # Aplicamos  el mapa de colores al resultado de Canny
        color_bordes = cv2.applyColorMap(edges, cv2.COLORMAP_MAGMA)

        # Mostramos la imagen resultante con el mapa de colores
        st.image(color_bordes, caption="Bordes detectados por Canny", use_column_width=True)

if __name__ == "__main__":
    main()
