"""
Usaremos Trimesh para cargar un STL de manera matematica.
"""

import trimesh
import matplotlib.pyplot as plt                             # Importamos como "PLT".
from mpl_toolkits.mplot3d.art3d import Poly3DCollection     # Importamos solo una parte.

def cargar_stl (ruta):

    try:                        # Intentamos cargar el archivo.

        model = trimesh.load_mesh(ruta)     # Cargamos el archivo.

        if model.is_empty:                  # Comprobamos que el modelo no esta vacio o dañado.

            raise ValueError (f'El archivo STL {ruta} esta vacio o dañado.')    
            # "Rise" sirve para romper el bucle en caso de fallo

        return model                        # Devolvemos el modelo en una variable.
    
    except Exception as e:      # Algo falla durante la carga el error se recoge en {e}.

        print(f'Error al cargar el archivo STL: {e} ')
        # En el mensage dejamos {e} para mostrar el mensage de error.

        return None
    
def mostrar (mesh_obj):                     # Usamos "PLT" para representar el modelo.
    figura = plt.figure()
    ax = figura.add_subplot(111, projection='3d')       # Espacio con el tipo ["3D"] y las especificaciones [(111) = Default].

    for simplex in mesh_obj.faces:
        triangle = mesh_obj.vertices[simplex]                                   # Crea los grupos de vertices.
        poligonos = Poly3DCollection([triangle], alpha=0.5, edgecolor ='k')     # Crea los poligonos.
        ax.add_collection3d(poligonos)                                          # Añade los poligonos al espacio.

    ax.set_xlabel('X')                              # Se añadan el nombre de cada eje.
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    scale = mesh_obj.vertices.flatten()             # Se extrae la escala del modelo.
    ax.auto_scale_xyz(scale, scale, scale)          # Se escala el espacio a la escala del modelo.
    plt.show(block=True)                           # Se crea la ventana. 
    
    # [(Block = False)-> permite que el codigo se continue ejecutando]

model = cargar_stl(input("Ruta del STL:"))
mostrar(model)
# Si el "Block" esta en "False" la ventana colapsa dado a que ya no hay mas codigo que ejecutar.
 