"""
17 / 02 / 2023

10.Escriba una función de Python que tome un número como parámetro y verifique que el número sea primo o no. 
Un número primo (o primo) es un número natural mayor que 1 y que no tiene divisores positivos aparte de 1 y sí mismo.

"""
''''
El numero primo es un numero entero con exactamente dos divisores integrales, 1 y el numero mismo. El numero
mismo. El numero 1 no es un primo, ya que solo tiene un divisor. Asi los numeros primos mas pequeños son: 2, 3, 5, 7

Para clasificar si un numero es primo o no, se puede tener en cuenta las siguientes condiciones: 

1. Si la division del numero es exacta -> No es primo
2. Si la division del numero no es exacta & ademas 
''' 

def primo_o_no_primo(n):
  for x in range(2,n):
    if (n%x) == 0:
      return print ("No es numero primo")
  return print ("Es numero primo")

  # Dentro de la iteracion del ciclo forge busco saber si n puede ser dividido entre x, ademas de eso busco saber si el resto de la division
  # n%i es igual a cero


primo_o_no_primo(15)
