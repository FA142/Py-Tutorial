"""
Cuando trabajamos con una gran cantidad de funciones para conseguir una unica cosa, hace falta algo mas.
Es necesario, ha veces, usar clases. 
Las clases son conjuntos concretos de funciones que cumplen el proposito de definir una entidad.
"""

class Coche:            
    
# Se definen los valores de la clase.

    def __init__ (self, modelo, marca, matricula, propietarios):    

# Aqui se especifican los valores especificos de cada clase.
# Cada vez que se defina la clase va ha tener un valor propio para estas variables.

        self.modelo = modelo
        self.marca = marca
        self.matricula = matricula
        self.propietarios = propietarios

# Aqui se especifican los parametros valores de cada clase.
# Cada vez que se defina la clase va ha tener el mismo valor para esta variables.

        self.año = 2016

# Se definen las funciones de la clase.

    def precio(self):

        if int(self.matricula) < 900:
            precio = 3000/int(self.propietarios)

        else:
            precio = 1500/int(self.propietarios)
        
        return str(precio)

# Self nos permite llamar las variables de dentro de la misma clase.
# Aquí, por ejemplo, se define el precio en función de la matricula y el numero de propietarios.

"""
Ahora vamos a crear una clase a partir de la que ya tenemos definida.
"""

print("Vamos a comparar el precio de tus coches.")

coche1 = Coche(modelo=input("Modelo:"), marca=input("Marca:"), matricula=input("Matricula:"), propietarios=input("Numero de propietarios:"))
coche2 = Coche(modelo=input("Modelo:"), marca=input("Marca:"), matricula=input("Matricula:"), propietarios=input("Numero de propietarios:"))

print(f"El valor del coche {coche1.marca} {coche1.modelo} del {coche1.año} de: {coche1.precio()}$.")
print(f"El valor del coche {coche2.marca} {coche2.modelo} del {coche2.año} de: {coche2.precio()}$.")