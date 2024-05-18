""" 
Funciones 
- Una función es un bloque de código que solo se ejecuta cuando se le llama
- Puede tener datos de entrada, conocidos como párametros
- Una función puede devolver datos como resultado
"""

# primer ejemplo que realiza la operación
def es_par(numero):
    if (numero % 2 == 0):
        print("El numero " + str(numero) + " es par");
    else:
        print("El numero " + str(numero) + " es impar");

numero = 2;
es_par(numero);

# segundo ejemplo retornando un boolean
def es_par(numero):
    if (numero % 2 == 0):
        return True;
    else:
        return False;

numero = 2;
resultado = es_par(numero);
print("¿El numero ", numero ," es par? ",  "Si" if resultado else "No");