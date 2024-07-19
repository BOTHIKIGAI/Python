# importación de la libreria para trabajar con XML
import xml.etree.ElementTree as ET

# Creación de la estructura del XML (aun no es XML)
data = '''
    <person>
        <name>Chuck</name>
        <phone type="intl">+1 734 303 4456</phone>
        <email hide="yes"/>
    </person>
        '''

tree = ET.fromstring(data) # convertilo desde string a XML
print('Name: ', tree.find('name').text) # Buscar la etiqueta nombre y traer el nodo de texto
print('Attr: ', tree.find('email').get('hide')) # Buscar la etiqueta email y traer el atributo
