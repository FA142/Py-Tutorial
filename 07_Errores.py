"""
Cuando se trabaja en proyectos grandes, con funciones complejas, es necesario manejar los posibles errores.
Para ello, utilizamos "try" y "except"
"""

try:
    num = int(input("Introduce un número: "))
    division = 10 / num

# Se intenta ver si el numero sirve como divisor.

except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")

# Si el divisor es 0, no sirve como divisor y se da este mensaje.

except ValueError:
    print("Error: Debes introducir un número.")

# Si el divisor no es un numero, no sirve como divisor y se da este mensaje.

else:
    print("Resultado:", division)

# Si no ocurre ningun error de los anteriores, se da este mensaje.

finally:
    print("Se ha acabado.")

# Esto indica que la comprobacion ha acabado, para bien o para mal.