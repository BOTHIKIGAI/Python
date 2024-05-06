""" String """
""" 
String o cadena de carcateres, es un tipo de datos que se utilizar para representar texto, este puede contener
espacios y números. Son útiles cuando se almacenan pequeñas o grandes cadeas de texto, desde palabras sueltas hasta
oraciones completas. Las cadenas se asignan las variables usando un solo igual y rodeando la cedena por comillas
simples o dobles.
"""
saludo = "Hello python";
saludo_1 = "Hello world";
print(saludo);
print(saludo_1);
print("Primer saludo ", saludo);
print("Segundo saludo ", saludo_1);

""" Indexing a String """
""" 
- nombre_variable[posición]
- nombre_variable[posici+on_inicial:posición_final]
"""
print(saludo[0]);
print(saludo[-1]);
print(saludo[-2]);
print(saludo[0:5]);
print(saludo[0:3]);