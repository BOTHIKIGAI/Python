""" ¿Que es la identación? """
""" 
En un lenguaje de programación, la identación es lo que la sangria
es el lenguaje humano escrito (a nivel fomral).
No todos los lenguajes de programación necesitan de una identación,
pero para el caso de python, la identación es obligatoria, ya que
de ella, dependera su estructura.
"""

""" Estructuras de control de flujo condicionales """
""" 
Una instrucción es aquella que permite realizar una acción u otra base a
una condición previa.
En la vida diaria, actuamos con la evaluación de condiciones:
1. Una condición: Si el semaforo está en verde, cruzar calle. Si no, esperar a 
   que cambie a verde.
2. Mas de una condición: Si llega la factura de la luz y tengo dinero, pago la factura.

| Operador | Descripción         | Ejemplo                           |
|----------|---------------------|-----------------------------------|
| ==       | Igual a             | 5 == 3 devuelve False             |
| !=       | No igual a          | 5 != 3 devuelve True              |
| <        | Menor que           | 5 < 3 devuelve False              |
| >        | Mayor que           | 5 > 3 devuelve True               |
| <=       | Menor o igual que   | 5 <= 5 devuelve True              |
| >=       | Mayor o igual que   | 5 >= 3 devuelve True              |
| and      | Operador lógico AND | (5 > 3) and (6 > 3) devuelve True |
| or       | Operador lógico OR  | (5 < 3) or (6 > 3) devuelve True  |
| not      | Operador lógico NOT | not(5 < 3) devuelve True          |

Las estructuras de control de flujo condicionales son:
1. if
2. elif
3. else

"""

semaforo = "verde";

# Estructura de control de flujo condicional if

# ejemplo 1
if (semaforo == "verde"):
   print("Cruzar la calle");
else:
   print("Esperar a que cambie a verde");

# ejemplo 2
compra = 200;

if (compra <= 100):
   print("pago en efectivo");
elif (compra >= 100):
   print("pago en tarjeta");
else:
   print("pago no es posible");