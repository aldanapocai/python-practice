# hipoteca.py

# inicial
if False:
    saldo = 500000.0
    tasa  = 0.05
    pago_mensual = 2684.11
    total_pagado  = 0.0

    while saldo > 0:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual

    print('Total pagado', round(total_pagado, 2))

# primera ampliacion
if False:
    saldo = 500000.0
    tasa  = 0.05
    pago_mensual = 2684.11
    total_pagado  = 0.0
    mes = 1

    while saldo > 0:
        pago_actual = pago_mensual + (1000 if mes <= 12 else 0)
        saldo = saldo * (1+tasa/12) - pago_actual
        total_pagado = total_pagado + pago_actual
        mes += 1

    print('Total pagado', round(total_pagado, 2))


# segunda ampliacion

saldo = 500000.0
tasa  = 0.05
pago_mensual = 2684.11
total_pagado  = 0.0
mes = 1
pago_extra_mes_comienzo = 73
pago_extra_mes_fin = 121
pago_extra = 1000
cont_pago_extra = 0

while saldo > 0:
    hay_pago_extra = pago_extra_mes_comienzo <= mes and mes < pago_extra_mes_fin
    pago_actual = pago_mensual + (pago_extra if hay_pago_extra else 0)
    saldo = saldo * (1+tasa/12) - pago_actual
    total_pagado = total_pagado + pago_actual
    if mes < 6 or mes > 308:
        print(mes, round(total_pagado, 2), round(saldo, 2))
    elif hay_pago_extra:
        cont_pago_extra +=1
        if cont_pago_extra in [1,2,47,48]:
            print(mes, round(total_pagado, 2), round(saldo, 2), "{} ({})".format(pago_extra,cont_pago_extra))
        elif cont_pago_extra in [3]:
            print("...")
    if mes in [6, 122]:
        print("...")
    mes += 1

print('Total pagado', round(total_pagado, 2))
print("Meses {}".format(mes-1))

# tercera ampliacion
if False:
    saldo = 500000.0
    tasa  = 0.05
    pago_mensual = 2684.11
    total_pagado  = 0.0
    mes = 1
    pago_extra_mes_comienzo = 73
    pago_extra_mes_fin = 121
    pago_extra = 1000
    cont_pago_extra = 0

    while saldo > 0:
        hay_pago_extra = pago_extra_mes_comienzo <= mes and mes < pago_extra_mes_fin
        pago_actual = pago_mensual + (pago_extra if hay_pago_extra else 0)
        if saldo * (1+tasa/12) < pago_actual:
            pago_actual = saldo * (1+tasa/12)
        saldo = saldo * (1+tasa/12) - pago_actual
        total_pagado = total_pagado + pago_actual
        if mes < 6 or mes > 308:
            print(mes, round(total_pagado, 2), round(saldo, 2))
        elif hay_pago_extra:
            cont_pago_extra +=1
            if cont_pago_extra in [1,2,47,48]:
                print(mes, round(total_pagado, 2), round(saldo, 2), "{} ({})".format(pago_extra,cont_pago_extra))
            elif cont_pago_extra in [3]:
                print("...")
        if mes in [6, 122]:
            print("...")
        mes += 1

    print('Total pagado', round(total_pagado, 2))
    print("Meses {}".format(mes-1))


