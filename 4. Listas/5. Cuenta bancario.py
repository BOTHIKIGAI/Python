"""
10 / 07 / 2023

Problema

5.  Elabore un programa que simule el movimiento de una cuenta de ahorro. Se tiene un saldo inicial y 
    dependiendo de la opción que escoja D- Deposito o R-Retiro, y el monto de esa opción aumente o 
    disminuya el saldo de la cuenta. Valide y de mensajes de error cuando considere.

Requisitos

1. Variable cuenta de ahorro
2. Opción de retirar o depositar
3. Validación de la información
4. Mensajes de error

Analisis

1. Crear una sola cuenta de ahorra, no solicitan mas
2. Mediante un ciclo while podria crear las opciones de retirar o depositar
3. Mediante print podria mostrar el dinero que tiene la cuenta
4. Mediante condicionales podria verificar si la operación es valida o no, ejemplo, realizar un retiro mayor a
   la cantidad de dinero de la cuenta.


"""

def transaccionBancaria():
    
    numeroCuentaBancaria = int(input("Ingrese el numero de su cuenta: "))
    cuentaBancariaDinero  = 10000
        # cuantaBancaria es una variable que simula el dinero almacena en una cuenta
    respuesta = 0
        # respuesta1 es la variable control para definir como se comportara el ciclo while

    while respuesta == 0:

        # Impresión Información "cuenta bancaria" :P
        
        print ("----------------------------------------------------------")
        print ("Bienvenido a BanColombia")
        print ("----------------------------------------------------------")
        print ("Cuenta:", numeroCuentaBancaria)
        print ("$", cuentaBancariaDinero)
        print ("----------------------------------------------------------")
        
        # Menu

        print ("Retiro = digite  1")
        print ("Deposito = digite 2")
        print ("Salir/Cancelar = digite 3")
        print ("----------------------------------------------------------")
        respuesta2 = int(input("¿Que desea realizar?: "))
        
        # Inicio de los condicionales

        if respuesta2 == 3:
            respuesta = 1
            print ("----------------------------------------------------------")
            print ("Hasta Luego :D")
            print ("----------------------------------------------------------")
            
        elif respuesta2 == 1:
            print ("----------------------------------------------------------")
            print ("Retiro")
            print ("----------------------------------------------------------")

            estadoOperacion = False
            while estadoOperacion != True:
                
                montoRetirar = int(input("¿Cuanto dinero desea retirar? "))

                if montoRetirar <= 0: 
                    print ("El monto ingresado es negativo o igual a cero, ingrese un monto mayor o igual a 1")
                    estadoOperacion = False

                elif montoRetirar < cuentaBancariaDinero:
                    cuentaBancariaDinero = cuentaBancariaDinero - montoRetirar
                    print ("La operación fue exitosa")
                    print ("----------------------------------------------------------")
                    print ("El estado de su cuenta", numeroCuentaBancaria)
                    print ("$", cuentaBancariaDinero)
                    print ("----------------------------------------------------------")
                    estadoOperacion = True

                elif montoRetirar == cuentaBancariaDinero:
                    cuentaBancariaDinero = cuentaBancariaDinero - montoRetirar
                    print ("La operación fue exitosa")
                    print ("----------------------------------------------------------")
                    estadoOperacion = True
                
                elif montoRetirar > cuentaBancariaDinero:
                    print ("----------------------------------------------------------")
                    print ("No cuenta con los fondos suficientes")
                    estadoOperacion = True

                else:
                    print("Error en el sistema")
                    estadoOperacion = True
            
        elif respuesta2 == 2:
            print ("----------------------------------------------------------")
            print ("Deposito")
            print ("----------------------------------------------------------")
        
            estadoOperacion = False
            while estadoOperacion != True:

                montoDepositar = int(input("¿Cuanto dinero desea depositar?"))
                cuentaBancariaDinero = cuentaBancariaDinero + montoDepositar
                print ("----------------------------------------------------------")
                print ("Cuenta", numeroCuentaBancaria)
                print ("$", cuentaBancariaDinero )
                print ("----------------------------------------------------------")
                print ("Digite 1 para SI o digite 2 para NO")
                respuesta2 = int(input( ))
                print ("----------------------------------------------------------")

                if respuesta2 != 1 or respuesta2 != 2:
                    print ("----------------------------------------------------------")
                    print ("Respuesta incorrecta")
                    print ("----------------------------------------------------------")
                    print ("¿Desea realizar otro deposito?")
                    print ("Digite 1 para SI o digite 2 para NO")
                    respuesta2 = int(input( ))
                    print ("----------------------------------------------------------")

                elif respuesta2 == 2:
                    estadoOperacion = True
                
                else:
                    print ("Error")
                    break
                    


        else:
            print("Fin")


transaccionBancaria()