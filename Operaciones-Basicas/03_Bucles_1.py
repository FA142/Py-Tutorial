"""
La logica nos permite establecer operaciones y flujos de trabajo.
En Python es esencial debido a que es un lenguaje de lectura lineal.
Cada orden se ejecuta desde la linea 1 hasta la ultima a menos que se indique lo contrario.

Condicionales.
Permiten realizar una accion sin se cumple una condición.
Permiten realizar una accion si no se cumple una condición.
"""
edad = int(input("Edad:"))

if edad >= 18:                  
    print("Eres mayor de edad.")        # Si "edad" es > o = que 18 se cumple la condición y se hace esto.
else:
    print("Eres menor de edad.")        # Si no se cumple la condición se hace esto.

"""
Bucles.
Permiten realizar una accion hsta que se incumple una condición.
Permiten realizar una accion por una cantidad determinada de ciclos.
"""
# Bucle "MIENTRAS" (While).

a = 0                       # Una variable.
while a < 5:                # El bucle comprueba que se cumple la condición. i < 5
    print(a)
    a += 1                  # Se realiza una acción.

print("Bucle finalizado.")  # Se ejecuta cuando el bucle ya ha terminado.

# Bucle "POR" (For).

for i in range(5):  # Se define una variable temporal donde se guardan las veces que se ha completado.
    print(i)        # Se realiza una acción.

print("Bucle finalizado.")  # Se ejecuta cuando el bucle ya ha terminado.