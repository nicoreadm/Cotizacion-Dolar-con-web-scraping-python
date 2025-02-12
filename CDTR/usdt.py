import requests
from bs4 import BeautifulSoup
# URL del sitio web a raspar
def usdt_scraping(pagina, clase):
    url = pagina

    # Realiza una solicitud HTTP para obtener el contenido de la página
    response = requests.get(url)

    # Comprueba si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Parsea el contenido HTML de la página
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encuentra elementos HTML que contengan los números (ajusta según el sitio web)
        numbers = soup.find_all(class_=clase)  # Sustituye 'clase-del-span-donde-estan-los-numeros'
        # Imprime los números

        precioc=(numbers[0].get_text(strip=True).split()[1].replace('.', '').replace(',',".").replace('$',"").replace('-',""))
        preciov=(numbers[1].get_text(strip=True).split()[1].replace('.', '').replace(',',".").replace('$',"").replace('-',""))
        precio=[precioc,preciov]
        return precio
    else:
        print('La solicitud no fue exitosa. Código de estado:', response.status_code)
