# hipoteca_ap_19.py

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
adelanto=1000
mes=1
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108


while saldo > 0:
    if saldo <pago_mensual:
        saldo=saldo-saldo
    else:
    
        if (mes <= pago_extra_mes_fin and mes>=pago_extra_mes_comienzo):
            saldo = saldo * (1+tasa/12) - pago_mensual - adelanto
            total_pagado = total_pagado + pago_mensual + adelanto
            
            
        else:
            saldo = saldo * (1+tasa/12) - pago_mensual
            total_pagado = total_pagado + pago_mensual
    mes=mes+1
   # print(mes-1, total_pagado, saldo) #Modificacion ej 1.10
    


#print('Total pagado', round(total_pagado, 2), "en", mes-1, "meses. Saldo", saldo)


print(f"El total pagado es {total_pagado:0.2f} en el mes {mes-1}, el saldo final es {saldo}") #Modificacion 1.20

