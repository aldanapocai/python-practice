#geringoso_v2.py

cadena='murcielago'
capadepenapa=' '


for c in cadena:

    capadepenapa+=c
    
    if c=='a':
       capadepenapa+='pa'
    
    if c=='e':
       capadepenapa+='pe'

    if c=='i':
       capadepenapa+='pi'
       
    if c=='o':
       capadepenapa+='po'

    if c=='u':
       capadepenapa+='pu'       

print(capadepenapa)