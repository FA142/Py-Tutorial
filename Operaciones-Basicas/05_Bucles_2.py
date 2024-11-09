"""
Los bucles sencillos son la manera mas frecuente de crear acciones que se ejecutan por "X" veces.
Sin embargo, cuando queremos meter un bucle dentro de otro debemos de hacerlo de manera concreta.
"""

for i in range(3):

    print ("Bucle 1 ejecutado:", i)

    for j in range(2):
        
        print ("Bucle 2 ejecutado:", j)

        for k in range(2):

            print ("Bucle 3 ejecutado:", k)
            
"""
La forma de entender el codigo seria:

- Se ejecuta lo que hay en el bucle 1.
    - Se ejecuta lo que hay en el bucle 2.
        - Se ejecuta lo que hay en el bucle 3. 

- Se ejecuta lo que hay en el bucle 1.
    - Se ejecuta lo que hay en el bucle 2.
        - Se ejecuta lo que hay en el bucle 3. 

- Se ejecuta lo que hay en el bucle 1.
    - Se ejecuta lo que hay en el bucle 2.
        - Se ejecuta lo que hay en el bucle 3. 

- Se detiene el bucle.
"""