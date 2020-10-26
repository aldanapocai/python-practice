# def tiene_a(expresion):
#     n = len(expresion)
#     i = 0
#     while i<n :
#         if expresion[i] == 'a' or expresion[i] == 'A':
#             return True
#             break
#         else:
#             return False
#         i += 1

 
# a = tiene_a('UNSAM 2020')
# b = tiene_a('abracadabra')
# c = tiene_a('La novela 1984 de George Orwell')

#%%

# def tiene_a(expresion):
#     n = len(expresion)
#     i = 0
#     while i<n:
#         if expresion[i] == 'a' or expresion[i] == 'A':
#             return True
#         i += 1
#     return False

# a = tiene_a('UNSAM 2020')
# b = tiene_a('La novela 1984 de George Orwell')


#%%
# def tiene_uno(expresion):
#     exp = str(expresion)
#     n = len(exp)
#     i = 0
#     tiene = False
#     while (i<n) and not tiene:
#         if exp[i] == '1':
#             tiene = True
#         i += 1
#     return tiene


# a = tiene_uno('UNSAM 2020')
# b = tiene_uno('La novela 1984 de George Orwell')
# c = tiene_uno(1984)

#%%Ejercicio 3.4: Alcances
def suma(a,b):
    c = a + b
    return c 
a = 10
b = 15
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")