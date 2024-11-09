"""
Las operaciones son una forma de trabajar y modificar las variables.
"""

a = 15
b = 7.9

suma = a+b
print ("Suma:", suma)                                    # Suma de "a" y "b".

resta = a-b
print ("Resta:", resta)                                  # Resta de "a" y "b".

multiplicación = a*b
print ("Multiplicacción:", multiplicación)               # Multiplica "a" por "b".

división = a/b
print ("División:", división)            # Divide "a" entre "b" y devuelve el numero con los decimales.

división_entera = a//b
print ("División:", división_entera)     # Divide "a" entre "b" y devuelve el numero entero. (No redondeado)

resto = a%b
print ("Resto:", resto)                  # Divide "a" entre "b" y devuelve el resto.

elevación = a**2
print ("Cuadrado:", elevación)           # Eleva "a" al cuadrado.

"""
Ademas, se puede operar con texto u otras variables.
Se pueden juntar cadenas y numeros.
Sin embargo, se necesita convertir la cadena a numeros.
"""

c = "56"

suma_str_num = a + int(c)           # Se convierte la cadna a numero. (La cadena debe de ser un numero.)
print ("Suma de cadena y numero: ", suma_str_num)

d = "Dia"

suma_str_num = d + " " + str(a)                       # Se convierte el numero a cadena.
print ("Suma de cadena y numero: " + suma_str_num)    # Sumamos un espacio para que quede bien.