def calcular_descuento(precio, tipo_cliente, cantidad, region, dia_semana, festivo):
    if tipo_cliente == "premium":
        if cantidad > 100:
            descuento = 0.3
        elif cantidad > 50:
            descuento = 0.2
        else:
            descuento = 0.1
    else:
        if tipo_cliente == "normal":
            if cantidad > 50:
                descuento = 0.15
            elif cantidad > 20:
                descuento = 0.1
            else:
                descuento = 0.05
        else:
            descuento = 0
    if region == "norte":
        if dia_semana == "lunes" or dia_semana == "martes":
            descuento *= 0.9
    elif region == "sur":
        if dia_semana == "miercoles" or dia_semana == "jueves":
            descuento *= 0.8
    else:
        if region == "este":
            if dia_semana == "viernes" or festivo:
                descuento *= 0.85
        else:
            if region == "oeste":
                if dia_semana == "sabado" or dia_semana == "domingo":
                    descuento *= 0.75
    
    precio_final = precio - (precio * descuento)
    return precio_final
