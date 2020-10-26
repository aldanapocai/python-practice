saldo = 500000.0
tasa  = 0.05
pago_mensual = 2684.11
total_pagado  = 0.0
mes= 1
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000 

while saldo >= 0 :
    if mes < pago_extra_mes_fin & mes > pago_extra_mes_comienzo  :
            saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra 
            total_pagado = total_pagado + pago_mensual + pago_extra
            mes= mes + 1
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual 
        total_pagado = total_pagado + pago_mensual 
        mes= mes + 1

print("Ejercicio 1.9","Meses",mes-1,'Total pagado:', round(total_pagado,0)-1,"Saldo:",round(saldo,0))