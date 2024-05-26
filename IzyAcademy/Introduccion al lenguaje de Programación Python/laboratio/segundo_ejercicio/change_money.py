import math


def change_money(monto):
    change = [0, 0, 0];
    """ 
    Si retorna un valor de 0.n representara que no se puede
    devolver un cambio con monedas de 25 centavos.
    """

    # 1. Saber cuantas monedas de 25 centavos se necesita
    a = monto / 25;

    # 1.2 Saber si el monto no es suficiente para dar cambio con monedas de 25 centavos
    if (math.floor(a) == 0):

        # 1.2.1 Saber cuantas monedas 10 centavos se necesita
        b = monto / 10;

        # 1.2.2 Saber si el monto no es suficiente para dar cambio con monedas de 10 centavos
        if (math.floor(b) == 0):

            # 1.2.2.1 Agregar al array el valor del monto al primer indice porque son monedas de 1 centavo
            change[0] = monto;
            # 1.2.2.2 Retornar el array
            return change;

        # 1.2.3 Si el monto es suficiente para dar cambio con monedas de 10 centavos
        else:

            # 1.2.3.1 Se agrega la cantidad de monedas de 10 centavos al indice 1
            change[1] = math.floor(b);
            # 1.2.3.2 Se resta la cantidad de monedas de 10 centavos al monto
            monto = monto - (10 * math.floor(b));
            # 1.2.3.3 Se agrega al array el valor de monto ya que su valor sera menor a 10
            change[0] = monto;

            return change;

    # 1.3 El monto es suficiente para dar cambio con 25 cetnavo
    else:

        # 1.3.1 Se agrega la cantidad de monedas de 25 centavos al indice 2
        change[2] = math.floor(a);
        # 1.3.2 Se le resta al monto la cantidad de monedas de 25 centavos
        monto = monto - (25 * (math.floor(a)));
        # 1.3.3 Se divide por 10 para saber la cantidad de monedas de 10 centavos
        c = monto / 10;

        # 1.3.4 Saber si el monto no es suficiente para dar cambio con monedas de de 10 centavos
        if (math.floor(c) == 0):

            # 1.3.1.1 Agregar al array el valor del monto al primer indice porque son monedas de 1 centavo
            change[0] = monto;
            return change;

        # 1.3.5 Si el monto es suficiente para dar cambio de 10 centavos
        else:

            # 1.3.5.1 Se agrega la cantidad de monedas de 10 centavos al indice 1
            change[1] = math.floor(c);
            # 1.3.5.2 Se le resta al monto la cantidad de monedas de 10 centavos
            monto = monto - (10 * math.floor(c));
            # 1.3.5.2 Se agrega al array el valor de monto ya que su valor sera menor a 10
            change[0] = monto;
            return change;


change = change_money(40);
print(change);