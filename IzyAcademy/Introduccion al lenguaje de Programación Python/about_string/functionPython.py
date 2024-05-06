saludo_1 = "Hello World";
saludo_2 = "hello python";

""" Lower and Upper """
print(saludo_1.lower()); # todo a minusculas
print(saludo_1.upper()); # todo a mayousulas
print(saludo_2.capitalize()); # primera letra a mayusculas
print(saludo_2.index("a")); # busca la coincidencia y retorna el string donde inicia, si no encuentra nada no retorna nada
print(saludo_2.index("python"));

saludo_3 = saludo_2.replace("hello", "Holaa"); # remplaza la palabra indicada en el primer parametro por la segunda
print(saludo_3);

list_saludo_2 = saludo_2.split(" ");
print(list_saludo_2);

list_saludo_2 = saludo_2.split("python");
print(list_saludo_2);