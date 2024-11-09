"""
Definimos salida como la informacion que el programa nos entrega.
En Python, las salidas se reflejan en el terminal.
Las salidas se crean con el comando <<print("salida")>>.

Si quiero recibir un mensaje que diga "Hola. Buenos dias."
"""
print("Hola. Buenos dias.")

# Si quiero recibir un mensaje guardado en una varable.

variable_de_ejemplo = "Que aburrimiento programar."
print (variable_de_ejemplo)

"""
Las entradas se crean con el comando <<entrada=input()>> o <<entrada=input("Mensaje:")>>.
Si quiero guardar un mensaje que diga "Hola. Buenos dias."
"""

mensaje = input("Mensaje a guardar:")
print(mensaje)

"""
Esto guardara la entrada en la variable "mensaje".
Si la entrada es un numero se hace con <<entrada=int(input())>> o <<entrada=int(input("Mensaje:"))>>.
"""

edad = int(input("Edad:"))
print(edad)