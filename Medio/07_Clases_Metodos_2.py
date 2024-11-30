"""
Ahora veremos el funcionamiento de los metodos de comparacion.
Estos son multiclase y comparan valores de una clase con otra.
"""

class Punto:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

# El metodo __eq__ define la igualdad (==)

    def __eq__ (self, otro):
        return self.y == otro.y
    
# El metodo __ne__ define la no igualdad (!=)

    def __ne__ (self, otro):
        return self.y != otro.y
    
# El metodo __lt__ define la inferioridad (menor) (<)

    def __lt__ (self, otro):
        return self.y < otro.y
    
# El metodo __le__ define la igualdad o inferioridad (menor o igual) (<=)

    def __le__ (self, otro):
        return self.y <= otro.y
    
# El metodo __gt__ define la superioridad (mayor) (>)

    def __lt__ (self, otro):
        return self.y > otro.y
    
# El metodo __ge__ define la igualdad o superioridad (mayor o igual) (>=)

    def __le__ (self, otro):
        return self.y >= otro.y
    

"""
Estos metodos devuelven como resultado un boleano.
"""

# Creamos dos puntos
p1 = Punto(2, 5)  # Coordenadas: (2, 5)
p2 = Punto(3, 7)  # Coordenadas: (3, 7)

# Comparaciones específicas para la altura
print("¿P1 está a la misma altura que P2? ", p1 == p2)  
print("¿P1 está más abajo que P2? ", p1 < p2)          
print("¿P1 está más arriba que P2? ", p1 > p2)         
print("¿P1 está a la misma altura o más abajo que P2? ", p1 <= p2) 
print("¿P1 está a la misma altura o más arriba que P2? ", p1 >= p2) 
print("¿P1 no está a la misma altura que P2? ", p1 != p2)           
