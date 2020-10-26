# hipoteca.py
# Archivo de ejemplo
# Ejercicio 1.7

saldo = 500000.0
tasa  = 0.05
pago_mensual = 2684.11
total_pagado  = 0.0

while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual

print("Ejercicio 1.7",'Total pagado:', round(total_pagado,2))

#%%
# Ejercicio 1.8
#pagos extra de $1000/mes durante los primeros 12 meses de la hipoteca.

saldo = 500000.0
tasa  = 0.05
pago_mensual = 2684.11
total_pagado  = 0.0
mes = 1
adelanto= 1000


while saldo > 0 :
    if mes < 13 :   
        saldo = saldo * (1+tasa/12) - pago_mensual - adelanto
        total_pagado = total_pagado + pago_mensual + adelanto
        mes= mes + 1
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
        mes= mes + 1

#%%
    
print("Ejercicio 1.8","Meses:", mes - 1, "Total pagado:", round(total_pagado,1)-1)

# Ejercicio 1.9

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

#%%

# Ejercicio 1.10

saldo = 500000.0
tasa  = 0.05
pago_mensual = 2684.11
total_pagado  = 0.0
mes= 1
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000 

print("Ejercicio 1.10")
while saldo >= 0 :
        print("Meses",mes-1,'Total pagado:', round(total_pagado,0)-1,"Saldo:",round(saldo,0))
        if mes < pago_extra_mes_fin and mes > pago_extra_mes_comienzo  :
            saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra 
            total_pagado = total_pagado + pago_mensual + pago_extra
            mes= mes + 1
        else:
            saldo = saldo * (1+tasa/12) - pago_mensual 
            total_pagado = total_pagado + pago_mensual 
            mes= mes + 1

#%%


# Ejercicio 1.11

saldo = 500000.0
tasa  = 0.05
pago_mensual = 2684.11
total_pagado  = 0.0
mes = 1
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000 

while saldo > pago_mensual :
    saldo *= (1+tasa/12)
    
    if mes <= pago_extra_mes_fin and mes >= pago_extra_mes_comienzo:
        saldo -= (pago_mensual + pago_extra)
        total_pagado = total_pagado + pago_mensual + pago_extra
    else:
        saldo -= pago_mensual 
        total_pagado = total_pagado + pago_mensual 
    
    mes += 1
    
    
total_pagado += saldo * (1+tasa/12)
mes += 1

print("Ejercicio 1.11","Meses",mes-1,'Total pagado:', round(total_pagado,0),"Saldo:",round(saldo,0))


#%%


880074.1 -1871.53


