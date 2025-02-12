import requests
from bs4 import BeautifulSoup
from usdt import usdt_scraping
from calculadora import fcalculadora



def precios_scraping():
    # URL del sitio web a raspar
    url = 'https://www.infodolar.com'

    # Realiza una solicitud HTTP para obtener el contenido de la página
    pagina = requests.get(url)

    # Comprueba si la solicitud fue exitosa (código de estado 200)
    if pagina.status_code == 200:
        # Parsea el contenido HTML de la página
        soup = BeautifulSoup(pagina.text, 'html.parser')

        # Encuentra elementos HTML que contengan los títulos de las noticias (ajusta según el sitio web)
        dolar = soup.find_all(class_='colCompraVenta')  # Ejemplo hipotético

        #guardo en un vector los valores de compra y venta utilizando el metodo split para seleccionar la informacion       que me interesa del string que extraigo

        #dolar blue
        blue=[dolar[0].text.split()[1].replace(',', '.') , dolar[1].text.split()[1].replace(',', '.')]

        #dolar BNA
        bna =  [dolar[36].text.split()[1].replace(',', '.') , dolar[37].text.split()[1].replace(',', '.')]

        #Dolar mep
        mep = [dolar[6].text.split()[1].replace(',', '.') , dolar[7].text.split()[1].replace(',', '.')]

        #dolar ccl
        ccl = [dolar[12].text.split()[1].replace(',', '.') , dolar[13].text.split()[1].replace(',', '.')]


        #invoca a la funcion usdt para determinar su valor
        usdt = usdt_scraping('https://www.infodolar.com/cotizacion-usdt.aspx', 'colCompraVenta')

        valores=[blue,bna,mep,ccl,usdt]
        return valores

    else:
        print('La solicitud no fue exitosa. Código de estado:', pagina.status_code)