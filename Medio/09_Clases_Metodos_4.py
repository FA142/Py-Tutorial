"""
Ahora analizaremos los metodos de varibles, de conversion y de Context Manager.
"""

class Sets:

# Iniciamos la calse.

    def __init__ (self, elementos):
        self.elementos = elementos

# Devuelve el valor de la longitud de la lista.

    def __len__ (self):
        return len(self.elementos)
    
# Devuelve el valor de un dato en una posición específica.

    def __getitem__ (self, indice):
        return self.elementos[indice]
    
# Cambia un valor en una posion x por otro.

    def __setitem__ (self, indice, valor):
        self.elementos[indice] = valor

# Elimina el valor en una posicion x de la lista.

    def __delitem__ (self, indice):
        del self.elementos[indice]

# Devuelve un boleano que indica si un valor se encuentar en la lista.

    def __contains__ (self, valor):
        return valor in self.elementos

contenedor = Sets([3435, 3332, 5657, 5652, 6766])   # Definimos los sets de nuestro contenedor.

print(len(contenedor))                              # Averiguamos cunatos sets diferentes tenemos.
print(contenedor[2])                                # Averiguamos cual es el tercero que mas hay.
contenedor[1] = 1978                                # Camviamos el numero del 2º set mas abundante.
print(contenedor[1])                                # Averiguamos cual es el tercero que mas hay ahora.
del contenedor[0]                                   # Eliminamos el mas abundante de la lista.
print(contenedor.elementos)                         # Imprimimos la lista final.
print(5652 in contenedor)               # Comprobamos si el set 5652 continua en nuestras existencias.