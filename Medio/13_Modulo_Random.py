"""
El módulo "random" proporciona funciones para generar valores aleatorios, como números, 
selecciones de listas o secuencias. 
Se usa para juegos, simulaciones y pruebas de software.
"""

import random

print ("Metodos random basicos:")
print (random.random())         # Aleatorio decimal entre 0 y 1, incluidos.
print (random.randint(1, 7))     # Alestorio entero entre 1 y 7, incluidos.
print (random.uniform(1, 7))    # Aleatorio decimal entre 1 y 7, incluidos.

print ("Metodo Choice:")
colores = ['rojo', 'azul', 'verde']
print (random.choice(colores))  # Selecciona el elemento en una posion aleatoria entre las de la lista.

print ("Metodo Choice (amañado):")
print (random.choices(colores, weights=[10, 1, 1], k=3))  

# Selecciona varios elementos aleatorios de una lista con una tendencia previa para cada elemento.
# En el ejemplo la tendecia es: Rojo -> 10, Azul -> 1, Verde -> 1.
# K indica el numero de elementos que se extraen.

print ("Metodo Sample:")
numeros = [1, 2, 3, 4, 5, 6]
print (random.sample(numeros, k=3))

# Selecciona varios elementos aleatorios de una lista pero estos no se repiten.
# K indica el numero de elementos que se extraen.

print ("Metodo Shuffle:")
numeros_2 = [1, 2, 3, 4, 5, 6]
random.shuffle(numeros_2)
print(numeros)
print(numeros_2)  

# Desordena una lista redefiniendola.

random.seed(42)             

# Sirve para establecer una semilla de aleatoriedad y obtener los mismos valores.

print(0.6394267984578837)
print(random.random())

