#WEB SCRAPING

#Libreria web scraping
from bs4 import BeautifulSoup
import requests


#Libreria para imágenes
from urllib.parse import urljoin
from PIL import Image
from io import BytesIO


def seccion_noticias(imagenes,titulos,links,imagen_filenm):

    #       Obtener el HTML
    url='https://www.lanacion.com.ar/tema/dolar-blue-tid67294/'
    pedido = requests.get(url)

    #       Parsear HTML
    if pedido.status_code == 200: #Codigo de estado 200 = OK; 400= error de cliente; 500= error de servidor
        html_obtenido = pedido.text #pedimos su atributo texto
        soup = BeautifulSoup(html_obtenido, "html.parser") 


    #        NOTICIAS
        noticias = soup.find('article', class_="mod-article")      #Busco todas las coincidencias para hacer un filtro y no leer todo el html
        i=0

        for noticia in noticias:

            #------------------------Extraer imagenes--------------------
            # Extraer la URL de la imagen de la sección de noticias
            imagen_url = noticias.find_next('img')['src']

            # Descargar la imagen
            imagen_url_rel = noticia.find_next('img')['src']
            imagen_url_abs = urljoin(url, imagen_url_rel)
            imagenes.append(imagen_url_abs)

            # Descargar la imagen y mostrarla
            imagen_response = requests.get(imagen_url_abs)
            imagen = Image.open(BytesIO(imagen_response.content))
            #imagen.show()   #MUESTRO LA IMAGEN

            # Guardar la imagen
            imagen_filename = f'imagen_{i + 1}.png'
            imagen.save(f"C:\\Desktop\\CDTR\\assets\\frame0\\noticia{imagen_filename}") #CAMBIAR LA RUTA A CUALQUIERA QUE SEA DESEADA PARA GUARDAR IMAGENES
            imagen_filenm.append("noticia"+imagen_filename)
            if i==3:
                break
            i +=1



        #------------------------Extraer Titulos---------------------

        noticias=soup.find_all('h2', class_="com-title --font-primary --l --font-medium")
        i=0
        for noticia in noticias:
            texto = noticia.get_text(strip=True)
            titulos.append(texto)

            # Mostrar el título y la URL de la imagen
            #print(f'Título: {titulos[i]}')
            #print(f'URL de la imagen: {imagen_url_abs}\n')

            # Detener después de las tres primeras noticias
            if i==3:
                break
            i +=1

        #----------------------Extraer Links de noticias-----------------

        noticias=soup.find_all('div', class_="content-media")
        i=0
        for noticia in noticias:
            link=noticia.find_next('a')['href']
            link_completo = "www.lanacion.com.ar"+link
            links.append(link_completo)
            i+=1
            if i==3:
                break
        #print(links) #Muestro los links



    else:
        print(f"Error al obtener la página. Código de estado: {pedido.status_code}") #la f es para separar el string del codigo en la misma sentencia
    return imagenes,titulos,links
