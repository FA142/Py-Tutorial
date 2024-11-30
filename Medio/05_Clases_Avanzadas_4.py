"""
Ahora que ya conocemos los metodos especiales de las clases, vamos a conocer los mas usuales.
Tan usuales que ya vienen predefinidos en el propio lenguage.

"""

from types import UnionType
from typing import Any


class Coche:

    def __init__ (self, kilometros, precio):
        self.kilometros = kilometros
        self.precio = precio

# Comprueba si dos terminos son iguales. Se llama con "==". Devuelve un boleano.

    def __eq__(self, otros_kilometros: object) -> bool: 
        return self.kilometros == otros_kilometros
    
# Divide dos terminos. Se llama con "|". Devuelve una Union de datos.

    def __or__(self, value: Any) -> UnionType:
        return self.precio/value

# Divide dos terminos a la inverse (de derecha a izquierda). Se llama con "|". Devuelve una Union de datos.   
    def __ror__(self, value: Any) -> UnionType:
        return value/self.kilometros


coche1 = Coche(210000, 3000)
coche2 = Coche(210000, 6700)

if coche1 == coche2:
    print("Misma cantidad de kilometros.")

# Si el valor esta a la derecha del dato se usa "__or__", si esta a la izquierda se usa "__ror__".
met_or = (coche1 | 2)
met_ror = (2 | coche1)
print (met_or)
print (met_ror)