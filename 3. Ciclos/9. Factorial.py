"""
08 / 02 / 2022

9. Escriba un programa para calcular el factorial de un número dado.

"""

"""
La primera solucion que cree, tenia el defecto de terminar en cero y repetir el resultado del factorial dos veces, por eso mismo, en esta solucion
investigue un poco mas y encontre que era mas sencillo utilizar un bucle while el cual se detuviera al momento que este sea falso o 0.

Lo que esta dentro del ciclo me permite ir restando el numero del factorial para luego ir multiplicando




"""

factorial = 1
num = float(input("Numero: "))
while num:
    factorial = factorial * num
    num -= 1                   
print (factorial)               


"""
Anterior codigo

fac = int(input("Ingrese un numero: "))
list_re = []
list_re.append(fac)

for x in range (fac):
    num_r = fac - 1
    fac = num_r
    res1 = list_re[0] * num_r
    list_re[0] = res1
    print (res1)

"""