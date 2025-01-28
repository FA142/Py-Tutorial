"""
Una vez que ya estamos listos para trabajar, vamos a comenzar por lo basico.

Comenzaremos mostrando una imagen.

Para ello, primero debemos comprender en que consiste una imagen en Python.
Una imagen se compone de pixeles, esa es la base, sin embargo, Python trabaja 
con numeros. En Python las imagenes son matrices de manera que son:

[(225), (225), (225)]

Para un pixel de una capa y tres canale, RGB. la profundidad corresponde a 
8 bits, es decir, cada valor puede ir desde 0 a 225.
Donde 0 corresponde a lo mas oscuro y 225 a lo mas claro.
"""

import cv2

try:

    while True:

        # Cragamos el archivo en una variable.
        im = cv2.imread(r'C:\Users\Pc\Documents\Curso de Python\descarga.png')
        
        # Cargamos la variable en una ventana con ID = 'Imagen'.
        cv2.imshow('Imagen', im)
                
        # Configuramos CV2 para evitar que la ventana colapse sola.
        if cv2.waitKey(1) & 0xFF == 27:
            
            # Printeamos la variable como una matriz.
            print(im)

            break

        # "if cv2.waitKey([Delay]) & 0xFF == [Codigo de tecla]:"

# Manejamos la falta del archivo.
except FileNotFoundError or FileExistsError:
    print("El archivo no existe.")

