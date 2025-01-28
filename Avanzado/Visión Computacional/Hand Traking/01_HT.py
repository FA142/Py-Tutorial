"""
Se denomina Hand Traking al sistema completo encargado de detectar he interpretar el movimiento de las manos. 

En este apartado veremos como:
    Importar imagenes. 
    Tarbajar con imagenes.
    Editar imagenes.
    Captura video.
    Utilizar modelos pre-entrenados de reconocimiento.
    Detectar el movimiento de las manos.
    Controlar cosas por medio del Hand Traking.

Python esta especialmente diseñado para interpretar y procesar gran cantidad de datos de manera eficiente y sin una gran
complicación, convirtiendolo en un lenguage ideal para estos proyectos.

Para comenzar, necesitaremos la libreria CV2.

La instalaremos:
"pip install opencv-python"
"""

try:
    import cv2
    
except ImportError:
    print("Importacion no lograda.")
