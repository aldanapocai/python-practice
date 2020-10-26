#rebotes_ap.py

#Una pelota de goma es arrojada desde una altura de 100 metros y cada vez que toca el piso salta 3/5 de la altura desde la que cayó. 
#Escribí un programa rebotes.py que imprima una tabla mostrando las alturas que alcanza en cada uno de sus primeros diez rebotes.

altura=100
cte_salto=3/5
salto=1

while salto<=10:
    altura=altura*cte_salto
    a=round(altura,4)
    print(salto, a)
    salto=salto+1

