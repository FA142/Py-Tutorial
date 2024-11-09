"""
La mejor forma de trabajar con informacion es a partir de variables.
Sin embargo, si se necesita guardar información se necesitan archivos permanentes.
Estos archivos se guardan en la memoria interna mientras que las variables se guardan en la memoria RAM.
Para abrir se usa "open()".
Se distinguen dos modos.
"w" para escribir o crear.
"r" para leer.
"""

with open ("Ej_01.txt", "r") as archivo:       # Se carga el archivo en RAM como "archivo".
    contenido = archivo.read()                 # Se lee el archivo como una cadena.
    print (contenido)

with open ("Ej_02.txt", "w") as archivo:       # Se carga o crea el archivo en RAM como "archivo".
    archivo.write ("Hola, este es un archivo de texto.")  # Se escribe una linea.
    archivo.write ("Escrito desde Python.")

try:                                           # Se intenta abrir el archivo.
    with open ("Ej_02.txt", "r") as archivo:   # Si existe se abre.
        contenido = archivo.read()
        print (contenido)

except FileNotFoundError:                      # Si se hubiera borrado, salta el error.
    print ("El archivo no existe.")

"""
Los archivos deben de estar en la carpetra raiz del proyecto.
"""