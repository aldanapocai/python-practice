#inclusive.py

frase = "Todos somos programadores"

palabras = frase.split()

palabras_t =[]

for palabra in palabras:
    if palabra[-1]=='o':
        palabra= palabra[:-1]+'e'
        palabras_t.append(palabra)
    
    elif palabra[-2]=='o':
        palabra= palabra[:-2] + 'e' + palabra[-1]
        palabras_t.append(palabra)
    else:
        palabras_t.append(palabra)
       


frase_t = ' '.join(palabras_t)

print(frase_t)