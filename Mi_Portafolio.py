import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
import base64
from PIL import Image
import io
import os
import folium
from streamlit_folium import folium_static




st.set_page_config(page_title='Mi Portafolio', page_icon=':wave:', layout='wide')


# Obtener la ubicación del usuario (opcional)
# location = st.location()




background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://cdn.pixabay.com/photo/2020/04/02/07/38/hot-air-balloon-4993835_1280.jpg");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)

def load_lottie(url):
    response= requests.get(url)
    if response.status_code !=200:
        return None
    return response.json()

# Temas
themes = ["Claro", "Oscuro", "Fondo_imagen"]
selected_theme = st.sidebar.radio("Selecciona un tema", themes)
# Cambiar el tema de la aplicación
if selected_theme == "Oscuro":
    st.write("""
    <style>
    [data-testid="stAppViewContainer"] > .main{
        background: #1E1E1E;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)
elif selected_theme == "Claro":
    st.write("""
    <style>
    [data-testid="stAppViewContainer"] > .main {
        background: #FFFFFF;
        color: black;
    }
    </style>
    """, unsafe_allow_html=True)
else:
    st.write(""" 
    <style>
          [data-testid="stAppViewContainer"] > .main {
    background-image: url("https://cdn.pixabay.com/photo/2020/04/02/07/38/hot-air-balloon-4993835_1280.jpg");
    background-size: cover;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    color: white;
}   
    </style>


""", unsafe_allow_html=True)





# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("estilos/estilos.css")


# codigo lottie hamster   https://lottie.host/f6b9cd22-dde0-4035-9644-e2f47aff0432/hUS0bTQwi3.json


codigo_lottie= load_lottie("https://lottie.host/48dc3c5d-e8d8-4329-9cae-79a61543c913/c3PXUBwg6b.json")
codigo_lottie_proyectos= load_lottie("https://lottie.host/695aeef8-d4b0-415d-a016-00c3d9c5b0a8/hKURFkbXbT.json")
python_lottie = load_lottie("https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json")
js_lottie = load_lottie("https://lottie.host/fc1ad1cd-012a-4da2-8a11-0f00da670fb9/GqPujskDlr.json")
streamlit_lottie = load_lottie("https://lottie.host/9eb4ee92-fcfe-4424-bd87-03b298060b51/HDGKKekqEW.json")
my_sql_lottie = load_lottie("https://assets4.lottiefiles.com/private_files/lf30_w11f2rwn.json")
git_lottie = load_lottie("https://assets9.lottiefiles.com/private_files/lf30_03cuemhb.json")
github_lottie = load_lottie("https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json")
docker_lottie = load_lottie("https://assets4.lottiefiles.com/private_files/lf30_35uv2spq.json")

st.write('##')
st.subheader('Bienvenidos a mi PORTAFOLIO :smile:')

st.write('''Mi  nombre  es  Jeyfrey, soy un apasionado por la tecnología, 
         la programación y el desarrollo WEB, actualmente llevo un año
         desarrollando aplicaciones con Python, Javascript y Streamlit con Django Frameworks         
         ''')

st.write('----')




#animacion 1 Cargar imágenes desde el sistema de archivos
image1 = Image.open("img/img1.jpg")
image2 = Image.open("img/img2.jpg")
image3 = Image.open("img/img3.jpg")
image4 = Image.open("img/img4.jpg")

# Lista de imágenes
images = [image1, image2, image3, image4]

# Título del slider carousel
st.title("Slider Carousel con Streamlit")

# Seleccionar la imagen actual mediante un slider
image_index = st.slider("Selecciona una imagen", 0, len(images)-1, 0)

# Mostrar la imagen actual
st.image(images[image_index], use_column_width=True)

#animacion 2 Cargar imágenes desde el sistema de archivos

uploaded_files = st.file_uploader("Cargar imágenes", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

# Verificar si se han cargado archivos
if uploaded_files:
    # Lista de imágenes
    images = [Image.open(file) for file in uploaded_files]

    # Título del slider carousel
    st.title("Slider Carousel con Streamlit")

    # Seleccionar la imagen actual mediante un slider
    image_index = st.slider("Selecciona una imagen", 0, len(images)-1, 0)

    # Mostrar la imagen actual
    st.image(images[image_index], use_column_width=True)


with st.container():
    selected = option_menu(
        menu_title= None,
        options= ['Acerca de mi',  'Contáctame!..', 'Curriculum', 'Skills'],
        icons=['person-check', 'code-slash', 'chat'],
        orientation = 'horizontal',
    )
#ACERCA DE MI...
if selected == 'Acerca de mi':
    with st.container():
        col1,col2= st.columns(2)
        with col1:
            st.write("##")
            st.subheader("Hola Mi nombre es Jeyfrey Calero!")
            st.title("""
                     Es un placer conocerlos! 
                     Soy un apasionado por la programación, la tecnologia, la inteligencia artificial 
                     el analisis de datos y desarrollo web Fullstack. Me atrae participar en los proyectos que permiten
                     formar parte de la comunidad de programadores, aprender y fortalecer mis habilidades! 
                     """)
        with col2:
            st_lottie(codigo_lottie)


#CONTÁCTAME...
if selected == 'Contáctame!..':
    with st.container():
        st.write("---")
        st.header("Envíame un Mensaje!")
        st.write("##")

        contact_form = """
        <form action="https://formsubmit.co/jeyfrey1980@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Tu Nombre" required>
            <input type="text" name="email" placeholder="Tu email" required>
            <textarea name="message" placeholder="Ingresa Tu Mensaje" required></textarea>
            <button type="submit">Enviar</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st_lottie(codigo_lottie)
        
        st.header("Mi Ubicación")
        
       # Crear un mapa centrado en la ubicación del usuario
        m = folium.Map(location=[4.08466, -76.19536], zoom_start=10)

        # Añadir un marcador en la ubicación del usuario
        folium.Marker([4.08466, -76.19536], tooltip=" Aqui estoy").add_to(m)

        # Mostrar el mapa en la aplicación de Streamlit
        folium_static(m)

#MUESTRA MI CV y la OPCION DE DESCARGA
if selected == 'Curriculum':
    with open("img/CV_JEYFREY_CALERO.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
      pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000mm" height="1000mm" type="application/pdf"></iframe>'
      st.markdown(pdf_display, unsafe_allow_html=True)
      
    def load_pdf(file_path):
            with open(file_path, "rb") as f:  # Abre el archivo en modo binario "rb"
                base64_pdf = base64.b64encode(f.read())  # Lee el archivo y lo codifica en base64
            return base64_pdf

        # Cargar el archivo PDF
    pdf_data = load_pdf("img/CV_JEYFREY_CALERO.pdf")

        # Mostrar el PDF
    pdf_display = f'<iframe src="data:application/pdf;base64,{pdf_data.decode()}" width="1000mm" height="1000mm" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

        # Agregar el botón de descarga

        # Función para crear el enlace de descarga
    def get_binary_file_downloader_html(bin_file, file_label='File', file_name='filename'):
            href = f'<a href="data:application/octet-stream;base64,{bin_file.decode()}" download="{file_name}">{file_label}</a>'
            return href

    st.markdown(get_binary_file_downloader_html(pdf_data, file_label='Descargar PDF', file_name='doc_aplicaciones.pdf'), unsafe_allow_html=True)

#MIS SKILLS
if selected == 'Skills':
       with st.container():
        col1,col2= st.columns(2)
        with col1:
            st.write("##")
            st.subheader("Python")
            st.write(""" Mis conocimientos con este lenguaje son de intermedio a avanzados,
            dado que he logrado implementar aplicaciones web utilizando django,
            al mismo tiempo aplicaciones de analisis de datos e inteligencia 
            artificial usando Streamlit""")
        with col2:
            st_lottie(python_lottie)
        
        st.markdown("---")

        with st.container():
            col1,col2= st.columns(2)
            with col1:
                st.write("##")
                st.subheader("Javascript")
                st.write(""" Mis conocimientos con este lenguaje son de un nivel 
                          básico a intermedio, dado que he logrado implementar aplicaciones web
                          sencillas como la APP-Agencia juegos y animaciones de tipo SWAL""")
            with col2:
                st_lottie(js_lottie)
        st.markdown("---")

        with st.container():
            col1,col2= st.columns(2)
            with col1:
                st.write("##")
                st.subheader("Streamlit")
                st.write(""" Mis conocimientos con este lenguaje son de un nivel 
                          Básico a intermedio, he desarrollado aplicaciones WEB scikit-learn,
                          pandas, numpy entre otros paquetes de Python para el análisis de datos
                        """)
            with col2:
                st_lottie(streamlit_lottie)
        
        with st.container():
            col1,col2= st.columns(2)
            with col1:
                st.write("##")
                st.subheader("Mysql")
                st.write(""" Mis conocimientos con esta Base de datos  son de un nivel 
                           bàsico a intermedio y he logrado implementar aplicaciones web
                           utilizando Mysql como base de datos""")
            with col2:
                st_lottie(my_sql_lottie)

            with st.container():
                col1,col2= st.columns(2)
                with col1:
                    st.write("##")
                    st.subheader("Git")
                    st.write(""" Mis conocimientos con Git son de un nivel 
                            intermedio a avanzado, he realizado clonación y
                            migración de distintas aplicaciones utilizando commit
                            y master""")
                with col2:
                    st_lottie(git_lottie)

            with st.container():
                col1,col2= st.columns(2)
                with col1:
                    st.write("##")
                    st.subheader("Github")
                    st.write(""" Mis conocimientos con Github  son de un nivel 
                            intermedio a avanzado, he creado mi propio repositorio
                            donde he cargado mas de 32 proyectos desarrollados con
                            los diferentes lenguajes PYTHON, JAVASCRIPT, STREAMLIT,
                            y framework Django.
                            Visita mi repositorio >>> https://github.com/Jeyjocar""")
                with col2:
                    st_lottie(github_lottie)





        
