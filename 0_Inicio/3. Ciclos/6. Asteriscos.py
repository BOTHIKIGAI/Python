"""
07 / 02 / 2023

6. Escriba un programa para mostrar el patron como triangulo con un asterisco. El patron como:

*
**
***
****
*****
****
***
**
*

"""

con1 = 0
obj = ["*"]
obj_rem = 4

print ("")

while con1 != 5:
    print (*obj)
    obj.append("*")
    con1 = con1 + 1

obj.pop(obj_rem)

while con1 != 0:
    con1 = con1 - 1
    obj.pop(obj_rem)
    obj_rem = obj_rem - 1
    print (*obj)

