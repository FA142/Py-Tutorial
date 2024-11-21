"""
Las clases ya se han visto en el bloque anterior, ahora profundizaremos en ellas.
Recordamos que una clase es una plantilla que se encarga de definir un comportamiento y unos objetos.
Por su parte, un bjeto es una instancia de una clase.
"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre            # Atributo Nombre
        self.edad = edad                # Atributo Edad

    def saludar(self):                  # Función
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

# Crear objetos (instancias)

persona1 = Persona("Juan", 30)
persona2 = Persona("María", 25)

# Usar atributos y métodos

print(persona1.saludar())  # Salida: Hola, mi nombre es Juan y tengo 30 años.
print(persona2.saludar())  # Salida: Hola, mi nombre es María y tengo 25 años.

"""
Esto es lo básico, recordamos que los atributos definen variables dento de una clase y las funciones son eso,
funciones de una clase.
El "__init__" actua como una funcion que crea o define los atributos, recordamos que se usa al principio para
poder usar esos datos dentro de las funciones siguientes.

Ahora vamos ha profundizar, las clases son un metodo para definir objetos y procesos con los atributos de estos,
sin embargo, para evitar repetir codigo de una clase en otra utilizamos un metodo llamado "herencia".

Por ejemplo, supongamos que en una clase se crea una funcion para sumar dos numeros y en otra clase 
quiero rescatar esa función, para ello no puedo llamar directamente a la función, debo de crear la segunda 
clase como "clase hija".
"""

class Coche:            
    
    def __init__ (self, modelo, marca, matricula, propietarios):    
        self.modelo = modelo
        self.marca = marca
        self.matricula = matricula
        self.propietarios = propietarios
        self.año = 2016

    def precio(self):
        if int(self.matricula) < 900:
            precio = 3000/int(self.propietarios)
        else:
            precio = 1500/int(self.propietarios)
        return str(precio)
    
class Puertas(Coche):

    def __init__(self, modelo, marca, matricula, propietarios, puertas):    

# Se vuelven a definir los atributos, en este caso "matricula" y "propietarios" no se usan y se pueden omitir.
       
        super().__init__(modelo, marca, matricula, propietarios) 

# Aquí no se pueden omitir, se deben de rescatar todos.
# Usamos a la clase padre para definir lo que ya existía. Para ello usamos "super()." .

        self.puertas = puertas

    def detalles(self):
        return f"{self.marca} {self.modelo} con {self.puertas} puertas."
    
# Creamos una función para usar estos datos, es a modo de ejemplo.




print("Vamos a comparar el precio de tus coches.")

coche1 = Puertas(modelo=input("Modelo:"), marca=input("Marca:"), matricula=input("Matricula:"), propietarios=input("Numero de propietarios:"), puertas=input("Puertas:"))
coche2 = Puertas(modelo=input("Modelo:"), marca=input("Marca:"), matricula=input("Matricula:"), propietarios=input("Numero de propietarios:"), puertas=input("Puertas:"))

print(f"El valor del coche {coche1.marca} {coche1.modelo} del {coche1.año} de: {coche1.precio()}$.")
print(f"Detalles de {coche1.marca} {coche1.modelo}: {coche1.detalles()}")
print(f"El valor del coche {coche2.marca} {coche2.modelo} del {coche2.año} de: {coche2.precio()}$.")
print(f"Detalles de {coche2.marca} {coche2.modelo}: {coche2.detalles()}")

"""
Otro metodo muy util para trabajar en proyectos de gran escale es el poliformismo, este permite redefinir una 
función en una clase hija de manera que en cada clase conserva el mismo nombre pero en funcion de la clase a 
la que se recurra se realizara una accion u otra.
"""

# Clase padre de la cual se parte como estructura base.

class Animal:

    # Se predefine la función.

    def sonido(self):
        return "Sonido Genérico No Definido Porque No Me Pagan (Es Broma)"

# Primer hijo.

class Perro(Animal):

    # Se convoca a la funcion y se redefine. 

    def sonido(self):
        return "wouf"
    
# Segundo hijo.

class Gato(Animal):

    # Se convoca a la funcion y se redefine. 

    def sonido(self):
        return "miau"

mascota1 = Animal ()
mascota2 = Perro ()
mascota3 = Gato ()

print (f"El gato hace '{mascota3.sonido()}', el perro hace '{mascota2.sonido()}', el loro hace '{mascota1.sonido()}'.")
