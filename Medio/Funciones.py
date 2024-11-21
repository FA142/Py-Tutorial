"""
Las funciones permiten encapsular un bloque de código reutilizable.
Pueden utilizarse cada vez que se quiera sin tener que escribirla.

Se deben de difinir y luego deben de llamarse.
Entre parentesis se escriben los nombres de las variables que va a usar la funcion.
"""

# Definir la función 1.

def saludar(nombre):
    return "Hola, " + nombre + "!"   
# Definir la función 2.

def despedir(nombre):
    return f"Adios, {nombre}!"   # Se utiliza la estructura f"" para poder introducir el dato en la cadena.
    