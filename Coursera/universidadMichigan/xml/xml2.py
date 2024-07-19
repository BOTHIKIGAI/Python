# importación de la libreria para trabajar con XML
import xml.etree.ElementTree as ET

# Creación de la estructura del XML (aun no es XML)
data = '''
    <stuff>
        <users>
            <user x="2">
                <id>001</id>
                <name>Chuck</name>
            </user>
            <user x="7">
                <id>009</id>
                <name>Brent</name>
            </user>
        </users>
    </stuff>
        '''

stuff = ET.fromstring(data) # convertir el string data a XML
lst = stuff.findall('users/user') # encuentra todos los elementos que pertenecen al node padre de users, devolviendo asi una lista
print('User count:', len(lst)) # como stuf es una lista podemos saber el numero de elementos
for item in lst: # iterar en cada lista para obtener la información de cada elemento
    print('Name', item.find('name').text) # de la lista pasa al elemento y extrae el nombre o atributos
    print('Id', item.find('id').text)
    print('Attribute', item.get("x"))