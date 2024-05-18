""" 
Bucles 
Es una estructura de control que permite repetir un bloque
de codigo varias veces, siempre que se cumpla una condición
especifica.
"""

# primer ejemplo (mientra el valor de year sea menor a 2012)
year = 2000;
# mientras el año sea menor a 2012
while (year < 2012):
    year += 1;
    print ("año", year);

# segundo ejemplo (ingresar nombre hasta que sea diferente de Jose)
nombre = input("Ingrese su nombre: ");
while (nombre != "Jose"):
    nombre = input("Indique su nombre: ");

print(nombre);

# tercer ejemplo (recorrer una lista)
mi_lista = ['Milan', 'Tara', 'Samanta', 'Tabata'];
for gatos in mi_lista:
    print(gatos);

"""
cuarto ejemplo (usar range)

La función range() devuelve una secuencia de números, comenzando desde 0
de forma predeterminada e incrementada en 1 (de forma predeterminada) y
se detiene antes de un número especifico.
"""

# primer ejemplo
for l in range (5): # se imprimira 5 veces
    print(l); # el valor de l iniciara en 5 y aumentara de uno a uno

print("------------------------------------")

# segundo ejemplo
for l in range(5,10): # se imprimira 5 veces
    print(l) # el valor de l iniciara en 5, se detendra antes de llegar a 10

# tecer ejemplo
for l in range(2001, 2020, 2): # se imprimira 10 veces
    print(l);
    """ 
    el valor de l inicia en 2000, se detendra antes de llegar a 
    2020 y aumentara de dos a dos, no de uno a uno.
    """

# cuarto ejemplo
