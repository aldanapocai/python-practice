#geringoso.py

cadena='aldana'
capadepenapa=' '

for c in cadena:
    if c=='a':
        s=cadena.split('a',1) #divide el string en dos por la a
        capadepenapa= s[0] + 'apa' +s[1]
        print(capadepenapa)
        
    elif c=='e':
        s=capadepenapa.split('e',1) #divide el string en dos por la a
        capadepenapa= s[0] + 'epe' +s[1]
        print(capadepenapa)

    elif c=='i':
        s=capadepenapa.split('i',1) #divide el string en dos por la a
        capadepenapa= s[0] + 'ipi' +s[1]
        print(capadepenapa)
    
    elif c=='o':
        s=capadepenapa.split('o',1) #divide el string en dos por la a
        capadepenapa= s[0] + 'opo' +s[1]
        print(capadepenapa)    

    elif c=='u':
        s=capadepenapa.split('u',1) #divide el string en dos por la a
        capadepenapa= s[0] + 'upu' +s[1]
        print(capadepenapa)        
       
print(capadepenapa)