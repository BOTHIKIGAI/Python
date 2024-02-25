"""
08 / 02 / 2023

10. Escriba un programa para mostrar un patrón como Z con asteriscos. 

*******
     *
    *
   *
  *
 *
*******

"""

list_a = [" ", " ", " ", " ", " ", "*" ]
num_lim1 = 5
num_lim2 = 4
list_c = ["*"]

for x in range(5):
    list_c.append("*")

print (*list_c)

for x in range (6):
    print(*list_a)
    list_a[num_lim1] = " "
    num_lim1 = num_lim1 - 1
    list_a[num_lim2] = "*"
    num_lim2 = num_lim2 - 1

print (*list_c)