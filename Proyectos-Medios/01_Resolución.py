"""
Se pide crear un programa que genere una contraseña aletoria con el modulo RANDOM.
"""

import random

def generar(longitud):
    contraseña = ''.join(str(random.randint(0,9))for _ in range (longitud))
    
# (for _ in) usa el (_) para indicar que no se necesita esa variable.

    return contraseña

longitud = int(input("Indique el largo de la contraseña:"))
print (f'La contraseña es <<{generar(longitud)}>>')