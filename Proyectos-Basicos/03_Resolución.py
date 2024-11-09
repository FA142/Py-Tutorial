"""
Se te pide crear una aplicacion que guarde los datos de una persona para un registro.

Nombre. 
Usuario. 
Fecha de nacimiento. (Numero)
DNI. (Numero)
Codigo de seguridad. 

Las variables deben de tener el formato adecuado para cada variable.
Los datos deben de guardarse en un archivo .txt.
"""

nombre = str(input("Nombre:"))
usuario = str(input("Usuario:"))


try:
    fecha_de_nacimiento = int(input("Fecha de nacimiento:"))
    dni = int(input("DNI:"))

except ValueError:
    print("Introduzca un dato valido.")

codigo_de_seguridad = input("Codigo de seguridad:")

datos = [nombre, usuario, fecha_de_nacimiento, dni, codigo_de_seguridad]

with open("Ej_03.txt", "w") as archivo:
    archivo.write (str(datos))
