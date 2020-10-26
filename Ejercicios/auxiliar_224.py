#Auxiliar 2.24

a = [{'nombre': 'Limon', 'cajones': 100, 'precio': 32.2}, 
                {'nombre': 'Naranja', 'cajones': 50, 'precio': 91.1},
                {'nombre': 'Limon', 'cajones': 150, 'precio': 83.44}
                ]
aux = []                
for n in a:
    aux.append(n['nombre'])
print(aux)