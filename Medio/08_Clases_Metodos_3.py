"""
Ahora veremos el funcionamiento de los metodos aritmeticos (suma, resta, ...).
Estos son multiclase y operan con valores de una clase y otra.
"""

class Punto:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

# El metodo __add__ define la suma (+)

    def __add__ (self, otro):
        return self.y + otro.y
    
# El metodo __sub__ define resta (-)

    def __sub__ (self, otro):
        return self.y - otro.y
    
# El metodo __mul__ define la multiplicación (*)

    def __mul__ (self, otro):
        return self.y * otro.y
    
# El metodo __truediv__ define la division real (/)

    def __truediv__ (self, otro):
        return self.y / otro.y
    
# El metodo __floordiv__ define la division sin decimales (//)

    def __floordiv__ (self, otro):
        return self.y // otro.y
    
# El metodo __mod__ define la obtencion del resto de la division sin decimales (%)

    def __mod__ (self, otro):
        return self.y % otro.y

# El metodo __pow__ define la exponenciacion (potencias) (**)

    def __pow__ (self, otro):
        return self.y ** otro.y   

"""
Estos metodos devuelven como resultado un numero.
"""

# Crear dos puntos
p1 = Punto(3, 4)
p2 = Punto(1, 2)

# Operaciones
print(p1 + p2)          # Suma 
print(p1 - p2)          # Resta 
print(p1 * p2)          # Multiplicación 
print(p1 / p2)          # División real 
print(p1 //p2)          # División entera 
print(p1 % p2)          # Módulo (resto)
print(p1 ** p2)         # Exponenciación
