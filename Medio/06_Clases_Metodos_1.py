"""

Ahora que ya conocemos el funcionamiento base de una clase, de un metodo y sabemos 
que ya existen metodso predefinidos, vamod a conocer los mas usados, su funcionamiento interno, 
y su aplicación practica.

En este caso veremos los metodos de formato o de retro-alimentacion del ususario.
Estos nos permiten dar una forma concreta a la resuesta de la extraccion de los valores de una clase.
"""

class Punto:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

# Metodo __str__:

    def __str__(self) -> str:
        return f"Punto ({self.x}, {self.y})."
    
# Metodo __repr__:

    def __repr__(self) -> str:
        return f"Punto(x={self.x}). Punto(y={self.y})."
    
"""
El metodo __str__:

Permite devolver valores de manera mas legible en formato "str" y se suele utilizar de 
manera que convierte la salida en una cadena para ser impresa directamente al llamar al metodo.

El metodo __repr__:

Permite devolver valores de manera mas legible pero se suele utilizar en el proceso de depuracion de 
manera que convierte la salida en una cadena para ser impresa directamente al llamar al metodo.
Tambien devuelve un "str".

Ambos metodos se pueden intercambiar de manera indistinguida.
"""

punto1 = Punto(1,2)

punto_str = str(punto1)
punto_repr = repr(punto1)
print (punto_str)
print (punto_repr)
