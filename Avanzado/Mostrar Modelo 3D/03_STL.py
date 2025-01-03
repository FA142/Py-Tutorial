"""
Usaremos Pyvista para cargar un STL de manera mas rapida y con menos carga de procesaiento.
Personalmente, esta manera es mas practica.
"""

import pyvista as pv    # Importamos Pyvista como "pv".

def cargar_stl_pyvista (ruta):                          # Usamos "PYVITAS".
    modelo = pv.read(ruta)                              # Se guarda el modelo.
    print(f"Número de puntos: {modelo.n_points}")       # El ".n_points" es un argumento que mide los vertices.
    print(f"Número de caras: {modelo.n_cells}")         # El ".n_cells" es un argumento que mide las caras.
    return modelo                                       # Devuelve el modelo.

def mostrar_modelo (modelo, tunel, presiones, id_ventana, datos):

# "Presiones" es el rango de valores al cual se asigna un color, es muy apropiado para simulaciones.
# "id_ventana" es el numero o nombre de la ventana.
# "Datos" es una lista con ciertos valores.

    modelo.cell_data['Presión'] = presiones

    # "Plotter" guarda los valores de una ventana. El argumento ".add_mesh" añade un modelo a la ventana.
    plotter = pv.Plotter(title=f'Simulacion {id_ventana}.')     
    plotter.add_mesh(modelo, scalars='Presión', cmap='jet', show_edges=True)

    # Aquí añadimos el contenedor (innecesario).
    plotter.add_mesh(tunel, style='wireframe', color='blue')
    
    variables = {
        'Presión': datos[0],  
        'Velocidad': datos[1],
        'Masa': datos[2],
        'Altitud': datos[3],
    }

    # Crear un string con el nombre de las variables y sus valores
    texto_simulacion = '\n'.join([f'{nombre}: {valor}' for nombre, valor in variables.items()])

    # Añadir texto en la ventana de visualización
    plotter.add_text(texto_simulacion, font_size=6, color='black', position='upper_left')

    # Se añaden los ejes.
    plotter.add_axes(line_width=5, color='black')

    # Se muestra la ventana. El parametro (auto_close) dicta si se cierra automaticamente, (interactive) permite interactuar con ella.
    plotter.show(auto_close=False, interactive=True)

def crear_tunel (largo, ancho, alto):
    tunel = pv.Box(bounds=(-largo/2, largo/2, -ancho/2, ancho/2, -alto/2, alto/2)) # Se crea una caja.
    return tunel

presiones = 1               # A modo de ejemplo usare un valor liso.
datos = [1, 2, 3, 4]        # A modo de ejemplo.

mostrar_modelo( cargar_stl_pyvista(input("Ruta")), crear_tunel(1,1,1), presiones, 1, datos)