"""
05 / 02 / 2023

13. Un reporte de salud muestra una tabla diferente del índice de masa corporal IMC de una persona que se calcula con la fórmula IMC=P/T en donde P 
es el peso en Kg. y T es la talla en metros. Lea un valor de P y de T, calcule el IMC y muestre su estado según la siguiente tabla:

/--------------//--------------/
/    IMC       /     Estado    /
/--------------//--------------/
/              //              /
/ Menor a 18.5 //  Desnutrido  /
/              //              /
/--------------//--------------/
/              //              /
/  18.5 , 25   //    Normal    /
/              //              /
/--------------//--------------/
/              //              /
/   25,30      //  Sobrepeso   /
/              //              /
/--------------//--------------/
/              //              /
/   30,35      //  Sobrepeso   /
/              //  Grado 1     /
/--------------//--------------/
/              //              /
/   35,40      //  Sobrepeso   /
/              //  Grado 2     /
/--------------//--------------/
/              //              /
/  Mayor a 40  //  Sobrepeso   /
/              //  Grado 3     /
/--------------//--------------/


"""

print ("")
print ("Pizza y precio")
print("")

print ("""

/--------------//--------------/
/    IMC       /     Estado    /
/--------------//--------------/
/              //              /
/ Menor a 18.5 //  Desnutrido  /
/              //              /
/--------------//--------------/
/              //              /
/  18.5 , 25   //    Normal    /
/              //              /
/--------------//--------------/
/              //              /
/   25,30      //  Sobrepeso   /
/              //              /
/--------------//--------------/
/              //              /
/   30,35      //  Sobrepeso   /
/              //  Grado 1     /
/--------------//--------------/
/              //              /
/   35,40      //  Sobrepeso   /
/              //  Grado 2     /
/--------------//--------------/
/              //              /
/  Mayor a 40  //  Sobrepeso   /
/              //  Grado 3     /
/--------------//--------------/

""")

p = float(input("Ingrese el peso en kg: "))
t = float(input("Ingrese la estatura en metros: "))

IMC = p / (t * t)

if IMC < 18.5:
    print ("Desnutrido")
elif IMC >= 18.5 and IMC <= 25:
    print ("Normal")
elif IMC > 25.30 and IMC < 30.55:
    print ("Sobrepeso")
elif IMC > 30.55 and IMC < 35.40:
    print ("Obesidad grado I")
elif IMC > 35.40 and IMC <= 40:
    print ("Obesidad grado II")
elif IMC > 40:
    print ("Obesidad grado II")
else:
    print ("Ingresaste un dato erroneo")