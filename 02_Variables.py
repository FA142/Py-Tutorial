"""
Existen varios tipos de "Variable".

Cuando una variable contiene mas de un dato, para recuperar un dato en una posicion especifiaca
debemos saber que siempre el darto en la posicion 1 tendra como indicador de posicion el valor 0.

Cadenas: almacena una cantidad de numero o letras pero no se puede combiar sus elementos.
Las cadenas se definen <<Variable="">>
Aqui, no se guarda el valor 23, sino un valor 2 y un valor 3 independientes. 
Cada elemento viene con una posicion determinada.
"""

cadena = "23"
print(cadena)

"""
Variable convencional: almacena un valor para poder trabajar con el.
Se definen sin <<"">>
Aqui, si se guarda el valor 23 como un numero.
"""

variable_comun = 23
print(variable_comun)

"""
Listas: almacena una cantidad de numero, letras o variable y se puede trabajar sobre ellos.
Las cadenas se definen <<lista=[]>>.
En el ejemplo vemos como una lista contiene valores, cadenas, e incluso, otra lista. 
"""

lista_1 = [23, "Hola", 45, [23, 45, 67]]
print(lista_1)

"""
Set: son iguales a las listas, pero no pueden presentar elementos dobles.
No pueden almacenar listas ni diccionarios.
No conservan el orden.
Se definen con <<set={}>>.
"""

set_1 = {1, 6, 7, 9, "Hola"}
print(set_1)

"""
Tuplas: almacena una cantidad de numero, letras o variable pero, no se pude trabajar sobre ellos.
Las cadenas se definen <<tupla=( , , ,)>> o <<tupla= , , , , >>.
"""

tupla_1 = (23, 45, 67, 78)
print(tupla_1)

tupla_2 = 23, 45, 67, 78
print(tupla_2)

"""
Diccionarios: almacena una cantidad de numero, letras o variable.
Presenta una estructura <<llave: valor>>.
Aqui se muestran los tres ejemplos mas comunes y usados en cunato a forma.
"""

diccionario_1 = { "Nombre": "Sara", "Edad": 23, "DNI": 1003882}
print(diccionario_1)

diccionario_2 = {
    "Nombre": "Sara", 
    "Edad": 23, 
    "DNI": 1003882
    }
print(diccionario_2)

diccionario_3 = dict["Nombre": "Sara", "Edad": 23, "DNI": 1003882]
print(diccionario_3)

"""
Sin embargo, a la hora de trabajar con gran cantidad datos, se suelen utilizar archivos ".json".

Qudan dos terminos mas por aclarar, bolenaos y numeros.

Boleanos: definen si una condicion es verdadera o no.
Se  escriben como <<condicion=True>> si es verdadera y <<condicion=False>> si es falsa.
"""

condicion = True
condicion = False

"""
Numeros: numeros.
Numeros enteros se escriben <<n>>.
Numeros decimales se escriben <<n.d>>.
Numeros complejos se escriben <<n.d + n.dj>> donde jota representa el numero i.

"""

a = 45
b = 45.67
c = 45.6 + 67j

print(a)
print(b)
print(c)

# Sin embargo, los numeros complejos son mas avanzados y requieren operaciones diferentes.
