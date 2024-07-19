from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Configuracion del CTX
ctx = ssl.create_default_context() # 
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
countIteration = 0;
i = 0

# Definición de variables

url = input('Enter - ') # pedir la url
count = int(input('Enter count: ')) # ingresar las veces que se repetira
position = int(input('Enter position: ')) # ingresar la posición a la que se ingresara

# Creación de funciones

# Funcion para abrir la URL, recuperar los elementos
def openUrl(url, ctx, element): # función para abrir la url
    html = urlopen(url, context=ctx).read() # leer la url
    soup = BeautifulSoup(html, "html.parser") # parsear a html la pagina
    elements = soup(element) # buscar todos los elementos anchor
    return elements

# Función para buscar la información que se requiere
def findURLByDeep(elements):
    
    data = re.findall('href="(.+)"', str(elements[position-1])) # extraer elemento
    return data[0]


while i < count:
    i = i + 1;
    elementsURL = openUrl(url, ctx, 'a')
    url = findURLByDeep(elementsURL)
    

print((re.findall('by_(.+)\.', url))[0]);
    