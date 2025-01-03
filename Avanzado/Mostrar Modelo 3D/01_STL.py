"""
Existen principalmente 2 librerias que se pueden usar par amostrar modelos 3D dentro de Python.
Una de ellas es Pyvista: "pip install pyvista"
La otra es Trimesh + PLT: "pip install trimesh"; "pip install matplotlib"
Aqui aprenderamos a usar ambas. Para ello es necesario conocer el funcionamiento de un STL.

Estructura de un STL:

facet normal 0.123715 -0.028784 0.991900
outer loop
vertex 0.057592 -1.198736 0.021406
vertex 0.092639 -1.158202 0.018211
vertex 0.078866 -1.066394 0.022593
endloop
endfacet

Eso es una cara de un modleo STL.

Esto indica la direccion de una cara, lo que se conoce como NORMAL:

"facet normal 0.123715 -0.028784 0.991900"

Esto indica los VERTICES de una cara:

"vertex 0.057592 -1.198736 0.021406"
"vertex 0.092639 -1.158202 0.018211"
"vertex 0.078866 -1.066394 0.022593"

Con esto es posible cargar un modelo 3D y mostrarlo dentro de Python.
Hay que recordar que un modelo 3D se compone de caras trianguladas, al menos en el formato STL.
El formato OBJ usa caras cudradas.
"""