"""
Recordamos que una clase es una plantilla que se encarga de definir un comportamiento y unos objetos.
Por su parte, un ojeto es una instancia de una clase.

Para trabajar en un nivel mas avanzado podemos crear nuestros propios metodos especiales o "dunder methods".

Con esto aparece la sobrecarga de operadores.
Ya sabiamos de la existencia del operador "__init__", que permitia crear una clase, ahora apareceran mas.
""
"""

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y)
    
    def __repr__(self) -> str:
        return f"El vector ({self.x}, {self.y})"
    
# La configuracion de clase se define como generar la instancia, añadir la clase anterior (si hay y se requiere)
# representar el resultado de manera leible.    


v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2            

# Se usa el operador <<+>> para tirar del metodo <<__add__>>, v2 se define como <<self>> y v1 como <<otro>>

print (v3)  
print (repr(v1) + " mas " + repr(v2) + " da como resultado " + repr(v3))    

# Se usa el operador <<repr>> para tirar del metodo <<__repr__>>
