import streamlit as st
import numpy as np
from PIL import Image
import cv2

def imagen_cannys(new_image, canny_threshold):
    img = np.array(new_image)  # ojo Ya no es necesario convertir a RGB
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # Convertir a formato BGR color rgb
    img = cv2.GaussianBlur(img, (11, 11), 0)
    bordes = cv2.Canny(img, canny_threshold, canny_threshold * 2)
    return bordes

def main():
    st.title("Aplicación de Canny")

    # Cargaremos la  imagen
    uploaded_image = st.file_uploader("Cargar imagen", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Convertimos el objeto UploadedFile a un objeto de imagen utilizando PIL
        pil_image = Image.open(uploaded_image)
   
        # Mostrar la imagen original
        st.image(pil_image, caption="Imagen Original", use_column_width=True)

        # Configurar el slider en el sidebar
        canny_threshold = st.sidebar.slider("Bordes de Canny", min_value=0, max_value=255, value=50)

        
        edges = imagen_cannys(pil_image, canny_threshold)

        # Aplicamos  el m apa de colores al resultado de Canny no se les olvide 
        edges_colored = cv2.applyColorMap(edges, cv2.COLORMAP_MAGMA) 

        # Mostramos la imagen resultante con el mapa de colores
        st.image(edges_colored, caption="Bordes detectados por Canny", use_column_width=True)

if __name__ == "__main__":
    main()
