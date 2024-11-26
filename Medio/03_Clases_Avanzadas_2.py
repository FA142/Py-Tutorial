"""
Recordamos que una clase es una plantilla que se encarga de definir un comportamiento y unos objetos.
Por su parte, un ojeto es una instancia de una clase.

Cuando trabajamos a nivel publico es dificil asegurar la integridad de nuestro codigo y es facil que alguien 
con una mala intención pueda colar una parte de codigo que altere el correcto funcionamiento de la aplicación que 
estemos desarrollando. 

Para ello usamos la privacidad de las clases.
De esta manera solo dentro de una clase o subclase se podra acceder al atributo.

"self.atributo" -> Crea un atributo publico.
"self._atributo" -> Crea un atributo portegido.
"self.__atributo" -> Crea un atributo privado.

A un atributo publico se puede acceder siempre.
A un atributo protegido solo se puede acceder en las clases o clsases hijas (subclases).
A un atributo privado solo se puede acceder en la propia clase.

"""

class Persona:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre        # Atributo público
        self._edad = edad           # Atributo protegido
        self.__salario = salario    # Atributo privado

# Método público, usa un atributo publico.
    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self._edad}"

# Método protegido, puede usar el atributo protegido porque es la clase padre.
    def _incrementar_edad(self, años):
        self._edad += años

# Método privado, solo se puede definir aquie por ser la clase pedre.
    def __actualizar_salario(self, nuevo_salario):
        self.__salario = nuevo_salario

# Acceso controlado al salario por ser estar en la clase padre.
    def obtener_salario(self):
        return self.__salario

    def actualizar_salario_publico(self, nuevo_salario):
        self.__actualizar_salario(nuevo_salario)


# Subclase
class Empleado(Persona):
    def __init__(self, nombre, edad, salario, puesto):
        super().__init__(nombre, edad, salario)
        self.puesto = puesto                        # Atributo público

# Método para usar atributos protegidos, al ser una clase hija se puede acceder a estos.
    def promocion(self, nuevo_puesto, incremento_edad):
        self.puesto = nuevo_puesto
        self._incrementar_edad(incremento_edad)     # Accede al método protegido

# Intento de acceso al atributo privado (producirá un error al estar fuera de la funcion padre).
    def intentar_modificar_salario(self, nuevo_salario):
        try:
            self.__salario = nuevo_salario          # Esto no funciona porque __salario es privado
        except AttributeError:
            print("Error: No se puede modificar un atributo privado directamente.")


# Uso de las clases
empleado1 = Empleado("Juan", 30, 50000, "Analista")

# Acceso a atributos y métodos públicos
print(empleado1.mostrar_informacion())      # Nombre: Juan, Edad: 30
print("Puesto actual:", empleado1.puesto)   # Puesto actual: Analista

# Acceso a métodos protegidos desde la subclase
empleado1.promocion("Gerente", 2)
print(empleado1.mostrar_informacion())      # Nombre: Juan, Edad: 32
print("Nuevo puesto:", empleado1.puesto)    # Nuevo puesto: Gerente

# Acceso a atributos privados controlado (clase padre)
print("Salario actual:", empleado1.obtener_salario())   # Salario actual: 50000
empleado1.actualizar_salario_publico(60000)
print("Nuevo salario:", empleado1.obtener_salario())    # Nuevo salario: 60000

# Intento de acceso directo al atributo privado (va ha fallar)
try:
    print (empleado1.salario)                           # Esto debe fallar
except AttributeError:
    print("No se puede acceder directamente al atributo privado 'salario'.")

# Verificar que el atributo privado no fue modificado
print("Salario después del intento de modificación:", empleado1.obtener_salario())      # 60000
