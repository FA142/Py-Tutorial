"""
Para crear una imagen desde cero, lo vamos ha hacer desde una matriz directamente.
Para ello, usaremos mnumpy.

"pip install numpy"
"""

import numpy as np
import cv2

# Creamos una matriz en formato array de caracter RGB.

im_m_rgb = np.array([
    [255, 255, 255], [255, 255, 255], [255, 255, 255],
    [255, 255, 255], [  0,   0,   0], [255, 255, 255],
    [255, 255, 255], [255, 255, 255], [255, 255, 255]
], dtype=np.uint8)

im_m_g = np.array([
    [255, 255, 255, 255, 255, 255, 255, 255, 255],
    [255, 255, 255, 255, 255, 255, 255, 255, 255],    
    [255, 255, 255, 255, 255, 255, 255, 255, 255],
    [255, 255, 255,   0,   0,   0, 255, 255, 255],
    [255, 255, 255,   0,   0,   0, 255, 255, 255],
    [255, 255, 255,   0,   0,   0, 255, 255, 255],
    [255, 255, 255, 255, 255, 255, 255, 255, 255],
    [255, 255, 255, 255, 255, 255, 255, 255, 255],
    [255, 255, 255, 255, 255, 255, 255, 255, 255]
], dtype=np.uint8)

im_m_g_2 = np.array([
    [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],
    [255, 0,   0,   0,   0,   0,   0,   0,   0,   255],
    [255, 0,   255, 255, 255, 255, 255, 255, 0,   255],
    [255, 0,   255, 0,   0,   0,   0,   255, 0,   255],
    [255, 0,   255, 0,   255, 255, 0,   255, 0,   255],
    [255, 0,   255, 0,   255, 255, 0,   255, 0,   255],
    [255, 0,   255, 0,   0,   0,   0,   255, 0,   255],
    [255, 0,   255, 255, 255, 255, 255, 255, 0,   255],
    [255, 0,   0,   0,   0,   0,   0,   0,   0,   255],
    [255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
], dtype=np.uint8)

# Aqui, cada numero corresponde a un pixel en escala de grises.



while True:

    # Cargamos la variable en una ventana con ID = 'Imagen'.
    cv2.imshow('Matriz', im_m_g_2)
              
    # Configuramos CV2 para evitar que la ventana colapse sola.
    if cv2.waitKey(1) & 0xFF == 27:
            
        # Printeamos la variable como una matriz.
        print(im_m_g_2)
        break


