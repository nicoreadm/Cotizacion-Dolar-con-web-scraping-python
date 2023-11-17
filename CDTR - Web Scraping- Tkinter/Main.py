from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, StringVar,PhotoImage
from tipo_dolar import precios_scraping
from calculadora import fcalculadora
from noticias import seccion_noticias
import webbrowser

###############ICONO





imagenes=[]
titulos=[]
links=[]
imagen_filenm=[]

tipos = precios_scraping()
calculos = [0, 0, 0, 0, 0]
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\\RUTA_DE_ASSETS\\assets\\frame0") #COLOCAR LA RUTA DE ASSETS DETERMINADA
seccion_noticias(imagenes,titulos,links,imagen_filenm)
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
window = Tk()
window.geometry("1402x817")
window.configure(bg = "#0B0B0F")

canvas = Canvas(
    window,
    bg = "#0B0B0F",
    height = 817,
    width = 1402,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets('image_1.png'))
image_1 = canvas.create_image(
    1062.0,
    423.0,
    image=image_image_1
)
image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    1063.0,
    455.0,
    image=image_image_2
)
image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    441.0,
    321.0,
    image=image_image_3
)
image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    492.0,
    379.0,
    image=image_image_4
)
image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    442.0,
    110.0,
    image=image_image_5
)
canvas.create_text(
    418.0,
    657.0,
    anchor="nw",
    text="\n",
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)
image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    441.0,
    681.0,
    image=image_image_6
)
image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    444.0,
    624.0,
    image=image_image_7
)
image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    625.0,
    625.0,
    image=image_image_8
)
canvas.create_text(
    88.0,
    613.0,
    anchor="nw",
    text="Calculadora",
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)
canvas.create_text(
    80.0,
    666.5645141601562,
    anchor="nw",
    text="Dolar Oficial:",
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)
canvas.create_text(
    331.9902038574219,
    665.4172058105469,
    anchor="nw",
    text="Dolar Ccl:",
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)
canvas.create_text(
    169.0,
    90.0,
    anchor="nw",
    text="Moneda",
    fill="#FFFFFF",
    font=("Inter SemiBold", 30 * -1)
)
canvas.create_text(
    406.0,
    90.0,
    anchor="nw",
    text="Compra",
    fill="#FFFFFF",
    font=("Inter SemiBold", 30 * -1)
)
canvas.create_text(
    635.0,
    90.0,
    anchor="nw",
    text="Venta",
    fill="#FFFFFF",
    font=("Inter SemiBold", 30 * -1)
)
image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    106.0,
    229.0,
    image=image_image_9
)
image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    104.0,
    301.0,
    image=image_image_10
)
canvas.create_rectangle(
    169.0,
    278.0,
    817.0031127929688,
    279.0,
    fill="#000000",
    outline="")
canvas.create_rectangle(
    169.0,
    343.0,
    817.0,
    345.0,
    fill="#000000",
    outline="")
canvas.create_rectangle(
    169.0,
    407.0,
    816.0,
    408.0,
    fill="#000000",
    outline="")
canvas.create_rectangle(
    169.0,
    469.0,
    817.0,
    471.0,
    fill="#000000",
    outline="")
image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    104.0,
    372.0,
    image=image_image_11
)
canvas.create_text(
    351.0,
    616.0,
    anchor="nw",
    text="Ingresar un monto: ",
    fill="#FFFFFF",
    font=("Inter Medium", 16 * -1)
)
canvas.create_text(
    184.0,
    232.0,
    anchor="nw",
    text="Dolar Oficial",
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)
canvas.create_text(
    184.0,
    300.0,
    anchor="nw",
    text="Dolar Blue",
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)
canvas.create_text(
    184.0,
    368.0,
    anchor="nw",
    text="Dolar Mep",
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)
canvas.create_text(
    184.0,
    440.0,
    anchor="nw",
    text="Dolar Ccl",
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)
canvas.create_text(
    184.0,
    498.0,
    anchor="nw",
    text="Dolar Usdt",
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)
image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    104.0,
    510.0,
    image=image_image_12
)
canvas.create_text(
    114.0,
    28.0,
    anchor="nw",
    text="Cdtr",
    fill="#FFFFFF",
    font=("Inter SemiBold", 30 * -1)
)
canvas.create_text(
    80.0,
    727.0,
    anchor="nw",
    text="Dolar Blue:",
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)
canvas.create_text(
    332.0,
    727.0,
    anchor="nw",
    text="Dolar Mep:",
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)
canvas.create_text(
    584.175048828125,
    667.5704345703125,
    anchor="nw",
    text="Dolar Usdt:",
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    62.0,
    38.0,
    image=image_image_14
)

#=======================caja de calculo==================================
entry_var = StringVar()
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    625.0,
    625.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D4DADD",
    fg="#000716",
    highlightthickness=0,
    textvariable=entry_var,
)
entry_1.place(
    x=566.0,
    y=611.0,
    width=118.0,
    height=26.0
)
#el nombre del valor es "valor ingresado"
#=============================================Codigo de conversion ==========================================================
#print dolar oficial Compra
canvas.create_text(
    438.0,
    232.18194580078125,
    anchor="nw",
    text="$"+tipos[1][0],
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)
#dolar blue compra
canvas.create_text(
    438.0,
    299.0,
    anchor="nw",
    text="$"+tipos[0][0],
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)
#print dolar mep compra
canvas.create_text(
    438.0,
    365.0,
    anchor="nw",
    text="$"+tipos[2][0],
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)
#print dolar ccl compra
canvas.create_text(
    438.0,
    429.0,
    anchor="nw",
    text="$"+tipos[3][0],
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)
#print dolar USDT compra
canvas.create_text(
    438.0,
    493.0,
    anchor="nw",
    text="$"+tipos[4][0],
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)
#print dolar oficial venta
canvas.create_text(
    668.0,
    232.0,
    anchor="nw",
    text="$"+tipos[1][1],
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)
#print dolar blue venta
canvas.create_text(
    668.0,
    299.0,
    anchor="nw",
    text="$"+tipos[0][1],
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)
#print dolar mep venta
canvas.create_text(
    668.0,
    365.0,
    anchor="nw",
    text="$"+tipos[2][1],
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)
#print dolar ccl venta
canvas.create_text(
    668.0,
    429.0,
    anchor="nw",
    text="$"+tipos[3][1],
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)
#print dolar USDT venta
canvas.create_text(
    668.0,
    493.0,
    anchor="nw",
    text="$"+tipos[4][1],
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)
image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    768.0,
    625.0,
    image=image_image_13
)
#####################################################
#resultado calculadora
text_dolar_oficial = canvas.create_text(
    212.0,
    665.9999694824219,
    anchor="nw",
    text="$" + str(calculos[1]),  # Initial placeholder value
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)
text_dolar_blue = canvas.create_text(
    212.0,
    724.9999694824219,
    anchor="nw",
    text="$" + str(calculos[0]),  # Initial placeholder value
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)
text_dolar_mep = canvas.create_text(
    449.0,
    724.8743286132812,
    anchor="nw",
    text="$" + str(calculos[2]),  # Initial placeholder value
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)
text_dolar_ccl = canvas.create_text(
    449.0,
    665.9999694824219,
    anchor="nw",
    text="$" + str(calculos[3]),  # Initial placeholder value
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)
text_dolar_usdt = canvas.create_text(
    706.0,
    665.8282470703125,
    anchor="nw",
    text="$" + str(calculos[4]),  # Initial placeholder value
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
    )
canvas.create_text(
    949.0,
    67.0,
    anchor="nw",
    text="Noticias",
    fill="#D9D9D9",
    font=("Katibeh Regular", 64 * -1)
)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    102.0,
    445.0,
    image=image_image_15
)
valorcalc=1
## cambia los valores de la etiqueta utilizando la funcion calculadora 
def actualizar(pesos):
        fcalculadora(tipos[0],tipos[1],tipos[2],tipos[3],tipos[4],pesos,calculos)
        canvas.itemconfig(text_dolar_oficial,text="$" + calculos[1])
        canvas.itemconfig(text_dolar_blue ,text="$" +calculos[0])
        canvas.itemconfig(text_dolar_mep,text="$" +calculos[2])
        canvas.itemconfig(text_dolar_ccl,text="$" +calculos[3])
        canvas.itemconfig(text_dolar_usdt,text="$" +calculos[4])
        
def on_entry_change(*args):

    global pesos
    value = entry_var.get()
    pesos=value
    #se guarda en la variable pesos lo que esta escrito en la caja
    print(value)
value= on_entry_change()
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: actualizar(pesos),
    relief="flat"
    #cuando se hace click en el boton se llama a la funcion actualizar precion con el parametro pesos que tiene el valor que esta en la caja de texto
)
button_1.place(
    x=725.0,
    y=614.0,
    width=86.0,
    height=21.0
)

################################### Noticias-----------------------------------------
#boton noticias 1:
url_noticias_1=links[1]
button_image_2 = PhotoImage(
    file=relative_to_assets(imagen_filenm[1]))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:  webbrowser.open(url_noticias_1),
    relief="flat"
)
button_2.place(
    x=908.0,
    y=486.0,
    width=300.0,
    height=139.0
)
#boton 2 noticias
url_noticias_2=links[0]
button_image_3 = PhotoImage(
    file=relative_to_assets(imagen_filenm[0]))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: webbrowser.open(url_noticias_2),
    relief="flat"
)
button_3.place(
    x=908.0,
    y=186.0,
    width=300.0,
    height=139.0
)
###############TITULO_---------------------
x2 = titulos[0]
palabras2 = x2.split()
max_palabras = 4
renglones2 = [palabras2[i:i + max_palabras] for i in range(0, len(palabras2), max_palabras)]
mostrar2 = [""] * 4
# Asignar elementos directamente a mostrar
for i, renglon in enumerate(renglones2):
    mostrar2[i] = renglon
canvas.create_text(
    901.0,
    355,
    anchor="nw",
    text=mostrar2[0],
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)
canvas.create_text(
    901.0,
    375,
    anchor="nw",
    text=mostrar2[1],
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)
canvas.create_text(
    901.0,
    395,
    anchor="nw",
    text=mostrar2[2],
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)
canvas.create_text(
    901.0,
    415,
    anchor="nw",
    text=mostrar2[3],
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)
#Noticia 2
x = titulos[1]
palabras = x.split()
max_palabras = 6
renglones = [palabras[i:i + max_palabras] for i in range(0, len(palabras), max_palabras)]
mostrar = [""] * 4
# Asignar elementos directamente a mostrar
for i, renglon in enumerate(renglones):
    mostrar[i] = renglon
canvas.create_text(
    901.0,
    655,
    anchor="nw",
    text=mostrar[0],
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)
canvas.create_text(
    901.0,
    675,
    anchor="nw",
    text=mostrar[1],
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)
canvas.create_text(
    901.0,
    695,
    anchor="nw",
    text=mostrar[2],
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)
canvas.create_text(
    901.0,
    715,
    anchor="nw",
    text=mostrar[3],
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)
canvas.tag_raise("CDTR")
entry_var.trace_add("write", on_entry_change)
window.resizable(False, False)
icon=PhotoImage(file="C:\\Users\\nicol\\Desktop\\proyecto\\CDTR\\assets\\frame0\\miku2.png")
window.iconphoto(False,icon)
window.mainloop()