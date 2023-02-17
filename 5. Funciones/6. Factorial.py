'''
15 / 02 / 2023

6. Escriba una función de Python para calcular el factorial de un número (un entero no negativo). La función acepta el número como argumento.

'''

def factorial(num):
    factorial = 1
    while num:
        factorial = factorial * num
        num -= 1                   
    print (factorial) 

num = float(input("Numero: "))
factorial(num)