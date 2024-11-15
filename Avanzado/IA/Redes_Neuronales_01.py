"""
- Redes neuronales:

Las redes neuronales son agrupaciones de terminos de manera vectorial (vectores) donde cada termino es un vector.
Este sistema utiliza la suma de vactores para saber cual es la respuesta mas cercana, por ejemplo:

- Hola = (1,0,0)
- Como = (0,1,0)
- Adios = (-1,0,0)

En este ejemplo, "Hola" y "Adiós" se encuentran en posiciones opuestas, 
lo que podría interpretarse como una relación de significado opuesto. 
Los modelos utilizan la suma de vectores y otras operaciones para calcular cuál es la respuesta o 
término más cercano o adecuado según el contexto.

De esta manera, se van formando las oraciones siguiendo segun la respuesta esperada una frase que se estructura
de la forma:

Termino/s inicial + termino secuencia + termino mas cercano en significado + ... 
... + termino secuencia + termino mas cercano en significado + (...). 

(Teniendo en cuenta el registro específico.)

De esta manera en un ejemplo se veria así:

Pregunta : << ¿Qué es un agujero negro? >>

Estructura de la respuesta:

Termino/s inicial = "agujero negro"

Termino secuencia 1 = "un"
Termino secuencia 2 = "celeste"
Termino secuencia 3 = "grande"
Termino secuencia 4 = "gravedad"
Termino secuencia 5 = "masa"
Termino secuencia 6 = "cuerpo"
Termino secuencia 7 = "espacio"

- Estructura Base de Ejemplo -

Termino secuencia (cuantifica)
Termino/s inicial
Termino secuencia (define)
Termino secuencia (concreta la definición)
Termino secuencia (concreta la definición)
Termino secuencia (cracteristica del "Termino/s inicial")
Termino secuencia (concreta la caracteristica)
Termino secuencia (consecuentcia de la carcteristica)
Termino secuencia (sufridor de la consecuencia de la caracteristica)

- Aplicacion de la Estructura Base de Ejemplo -

-- Vectorizar los Terminos Secuencia con Respecto a la Estructura del Ejemplo --

Formato de vectores: (cuantifica); (define); (concreta la definición); (cracteristica del "Termino/s inicial"); ...

Termino secuencia 1 = (1.0, 0.1, 0.3, 0.0, 0.1, 0.6, 0.6)
Termino secuencia 2 = (0.0, 0.3, 1.0, 0.0, 1.0, 0.6, 0.0)
Termino secuencia 3 = (0.0, 0.6, 1.0, 1.0, 1.0, 0.0, 0.0)
Termino secuencia 4 = (0.0, 0.0, 0.0, 0.6, 0.0, 1.0, 0.4)
Termino secuencia 5 = (0.0, 0.0, 0.0, 0.8, 0.2, 0.2, 0.2)
Termino secuencia 6 = (0.0, 0.6, 0.3, 0.0, 0.0, 0.0, 1.0)
Termino secuencia 7 = (0.0, 0.2, 0.0, 0.3, 0.0, 0.0, 0.1)

-- Los Terminos van Estructurando --

---

Termino secuencia (cuantifica) -> 
Termino secuencia 1 -> 

"Un"

---

"Un" + Termino/s inicial ->

"Un agujero negro"

---

"Un agujero negro" + Termino secuencia (define) ->

"Un agujero negro" + () + "grande" -> Opcion A
"Un agujero negro" + () + "cuerpo" -> opcion B

--- Opcion B

"Un agujero negro () cuerpo" + Termino secuencia (concreta la definición) ->

"Un agujero negro () cuerpo" + () + "grande"   -> Opcion B-a
"Un agujero negro () cuerpo" + () + "celeste"  -> Opcion B-b

--- Opcion B-b

"Un agujero negro () cuerpo () celeste" + Termino secuencia (concreta la definición) ->

"Un agujero negro () cuerpo () celeste" + () + "grande"   -> Opcion B-b-a
"Un agujero negro () cuerpo () celeste" + () + "celeste"  -> Opcion B-b-b

* Se elimina la "Opcion B-b-b" por repeticion.

--- Opcion B-b-a

"Un agujero negro () cuerpo () celeste () grande" + 
Termino secuencia (cracteristica del "Termino/s inicial") ->

"Un agujero negro () cuerpo () celeste () grande" + () + "masa"    -> Opcion B-b-a-a
"Un agujero negro () cuerpo () celeste () grande" + () + "grande"  -> Opcion B-b-a-b

* Se elimina la "Opcion B-b-a-b" por repeticion.

--- Opcion B-b-a-a

"Un agujero negro () cuerpo () celeste () grande () masa" + 
Termino secuencia (concreta la caracteristica) ->

"Un agujero negro () cuerpo () celeste () grande () masa" + () + "grande"  -> Opcion B-b-a-a-a

--- Opcion B-b-a-a-a

"Un agujero negro () cuerpo () celeste () grande () masa () grande" + 
Termino secuencia (consecuentcia de la carcteristica) ->

"Un agujero negro () cuerpo () celeste () grande () masa () grande" + () + "gravedad"  -> Opcion B-b-a-a-a-a

--- Opcion B-b-a-a-a-a

"Un agujero negro () cuerpo () celeste () grande () masa () grande () gravedad" + 
Termino secuencia (sufridor de la consecuencia de la caracteristica) ->

"Un agujero negro () cuerpo () celeste () grande () masa () grande () gravedad" +
() + "cuerpo"  -> Opcion B-b-a-a-a-a-a

--- Resultado: Opcion B-b-a-a-a-a-a

"Un agujero negro () cuerpo () celeste () grande () masa () grande () gravedad () cuerpo."

Añadiendo conectores aplicando un proceso similar donde se vectoriza en funcion 
de la palabra anterior y porsterior podemos pulir obteniendo:

>> Un agujero negro (es) cuerpo () celeste (muy) grande (cuya) masa (es muy) grande (produciendo) 
gravedad (en otro) cuerpo. <<

"""
"""
Las redes neuronales son un campo complejo que se aplican en nuestro dia a dia, tal como se puede ver en el 
famoso CHAT GPT. 
Tal como puedes ver la respuesta dista mucho de la que puede dar esta IA aun aplicando la misma tecnica, 
nosotros solo hemos utilizado entre dos o tres mapas de vectores introducidos manualmente.
En cambio, las IAs mas complejas cuentan con cinetos de mapas vectoriales que se actualizan con cada operación.
Sin embargo, a modo de toma de contacto es mas que suficiente.
"""