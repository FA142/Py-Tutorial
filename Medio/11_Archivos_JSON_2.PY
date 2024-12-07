"""
Aquí se meneja le escritura de archivos con contenido. (El contenido debe ser una lista).
"""

import json

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def a_json(self, archivo):
# Guarda el punto en un archivo JSON. Si el archivo ya existe, añade el punto a la lista.
        
        try:
            
# Si el archivo ya existe, carga los datos existentes
            with open(archivo, 'r') as f:
                contenido = f.read().strip()                        # Lee el contenido y elimina espacios en blanco
                datos = json.loads(contenido) if contenido else []  # Si está vacío, inicializa una lista vacía
        
        except FileNotFoundError:
            
# Si el archivo no existe, inicializa una lista vacía
            datos = []

# Se usa el metodo append para añadir elementos a una lista.
        datos.append({"x": self.x, "y": self.y})

        # Guarda la lista actualizada en el archivo
        with open(archivo, 'w') as f:
            json.dump(datos, f, indent=4)

    @classmethod
    def desde_json(cls, archivo):

# Carga todos los puntos desde un archivo JSON y devuelve una lista de instancias.
        with open(archivo, 'r') as f:
            datos = json.load(f)
        return [cls(dato["x"], dato["y"]) for dato in datos]

p1 = Punto(5, 10)
p2 = Punto(7, 15)

p1.a_json("Ejemplo_2.json")  # Guarda p1 en el archivo
p2.a_json("Ejemplo_2.json")  # Añade p2 al archivo

puntos_cargados = Punto.desde_json("Ejemplo_2.json")  # Carga todos los puntos desde el archivo
for punto in puntos_cargados:                         # Printea cada punto
    print(punto.x, punto.y)  

"""
Cada ejecucion añadira ambos puntos.
"""
