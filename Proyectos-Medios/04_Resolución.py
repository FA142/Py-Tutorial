"""
Se pide crear un sistema que lance entre uno y dos dados usando el modulo RANDOM.
"""

import random

def lanzar_dado():
    return random.randint(1, 6)

print("Simulador de dados")
print("Opciones: lanzar 1 o 2 dados.")

try:

# Intentamos que se introduzca un numero de dados entre 1 y 2.
    dados = int(input("¿Cuántos dados quieres lanzar? (1 o 2): "))

    if dados == 1:
        # Si es un solo dado se realiza un unico lanzamiento.
        resultado = lanzar_dado()
        print(f"El dado muestra: {resultado}")

    elif dados == 2:
        # Si son dos dados, se realiza el mismo codigo 2 veces.
        dado1 = lanzar_dado()
        dado2 = lanzar_dado()
        print(f"El primer dado muestra: {dado1}")
        print(f"El segundo dado muestra: {dado2}")
        print(f"El total es: {dado1 + dado2}")

    else:
        # Si no son 1 o 2 dados se indica que no se puede operar con mas.
        print("Por favor, selecciona 1 o 2 dados.")
        
except ValueError:

# Si no se introduce un numero se maneja el error.
    print("Introduce un número válido.")
