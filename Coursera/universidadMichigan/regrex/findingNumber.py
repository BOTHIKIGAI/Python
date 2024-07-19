import re

fhand = open(r'..\assets\plaintxt\regex_sum_2055738.txt') # ruta del archivo
values = list();

# Funcion para tener una lista plana sin listas dentro de esta
def flatten_list(list):
    flat_list = []
    for sublist in list:
        for item in sublist:
            flat_list.append(int(item))
    return flat_list


# recorrer cada linea y recuperar los valors numericos
for line in fhand:
    
    if re.findall('[0-9]+', line):
        values.append(re.findall('[0-9]+', line))
    

values = sum(flatten_list(values))
    
print(values)