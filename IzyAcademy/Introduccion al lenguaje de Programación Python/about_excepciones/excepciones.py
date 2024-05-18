"""
Excepciones
Es indispensable capturar las excepciones y/o errores que se
generan en nuestro código y decidir que hacer en caso de que
suceda.
"""

# ejemplo 1
def cubo(numero): # se define una función que retornara un el cubo de un numero
    numero = numero ** 3;
    return numero;

numero = "Hola"; # se instancia una variable con un dato no numerico

# try except permite caputarar errores y que el codigo continue trabajando
try:
    cubo(numero);
except:
    print("hubo un error en la función cubo");

print('holaaa aun continuo');