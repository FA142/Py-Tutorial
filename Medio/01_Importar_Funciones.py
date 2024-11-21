"""

Cuando trabajamos con proyectos un poco mas complejos, puede ser estresante tener 
cientos de funciones definidas en un mismo documento de manera que si nuestro proyecto requiere una 
funcion para saber la hora y otra para calcular el precio de un coche, resulta poco util tenerlas definidas en el 
mismo archivo.

Ademas, al tenerlas en archivos distintos pueden ser integradas en cualquier archivo, no solo en el 
proyecto donde se han definido.

Para esto, utilizamos el modulo impot()

Sin embargo, el archivo debe de estar en la misma carpeta.

"""

mensaje1 = ""
mensaje2 = ""

from Funciones import saludar  # El modulo no debe de empezar por un numero, se importa solo la funcion saludar.

print ("Saludar importado con exito.")

mensaje1 = saludar("Ana")       # Ya se puede usar la funcion como si estuviera dentro del archivo.
print(mensaje1)

from Funciones import *        # El modulo no debe de empezar por un numero, se importan todas las funciones.

print ("Todas las funciones importadas con exito.")

mensaje2 = despedir("Ana")       # Ya se puede usar la funcion como si estuviera dentro del archivo.
print(mensaje2)

# El archivo donde se guardan las funciones solo deberia contener funciones.