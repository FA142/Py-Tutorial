"""
Otro tipo de archivo es el CSV. Aquí se muestra el metodo de sobreescribir.
"""

import csv

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# "@staticmethod" es similar a "@classmethod" no depende de la instancia si no ha la clase.

    @staticmethod
    def guardar_puntos_csv(puntos, archivo):

# Guarda una lista de puntos en un archivo CSV.
        with open(archivo, 'w', newline='') as f:
            escritor = csv.writer(f)
            escritor.writerow(["x", "y"])  # Encabezado
            for p in puntos:
                escritor.writerow([p.x, p.y])

    @staticmethod
    def cargar_puntos_csv(archivo):

# Carga una lista de puntos desde un archivo CSV.
        with open(archivo, 'r') as f:
            lector = csv.DictReader(f)
            return [Punto(float(fila["x"]), float(fila["y"])) for fila in lector]

p1 = Punto(5, 6)
p2 = Punto(7, 8)
Punto.guardar_puntos_csv([p1, p2], "Ejemplo_1.csv")

puntos_cargados = Punto.cargar_puntos_csv("Ejemplo_1.csv")
for p in puntos_cargados:
    print(p.x, p.y)  