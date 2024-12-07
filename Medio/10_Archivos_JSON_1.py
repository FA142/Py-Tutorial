"""
Para guardar los datos de manera ordenada se utilizan archivos de manera que se guarden por un tiempo ilimitado.
En este caso veremos el JSON que se había mencionado anteriormente.
Aqui se puede ver el metodo de sobreescritura.
"""

import json

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def a_json(self, archivo):
# Guarda el punto en un archivo JSON.
        with open(archivo, 'w') as f:                   # "w" abre el archivo en modo escritura y borra todo.
            json.dump({"x": self.x, "y": self.y}, f)

# "@classmethod" se conoce como decorador e indica que se puede llamar a una funcion sin declarar una clase.

    @classmethod
    def desde_json(cls, archivo):
# Crea un punto cargando datos desde un archivo JSON.
        with open(archivo, 'r') as f:
            datos = json.load(f)
        return cls(datos["x"], datos["y"])

# Ejemplo de uso
p1 = Punto(5, 10)
p1.a_json("Ejemplo_1.json")                      # Guarda en un archivo JSON
p2 = Punto(7, 10)
p2.a_json("Ejemplo_1.json")                      # Guarda en un archivo JSON

p1_cargado = Punto.desde_json("Ejemplo_1.json")  # Carga desde un archivo JSON
print(p1_cargado.x, p1_cargado.y)  
