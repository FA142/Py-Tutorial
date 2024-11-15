"""
Se conoce como red neuronal al sistema que se encarga de genrar texto de manera procedural usando 
datos y su relación interna.

Para generar texto se pueden usar tres metodos:

- Red neuronal.
- Reglas gramaticales.
- Red interna preentrenada.


- Reglas gramaticales:

El metodo de reglas gramaticales permite escribir textos tal como lo haria una persona real, sin embargo,
solo puede escribir textos gramaticamente correctos y con terminos registrados en la RAE o el diccionario
lexico-gramatical correspondiente. Este metodo puede ser increible para textos muy cultos o de hambito
empresarial. No obstante, el sistema no es optimo para un hambito mas coloquial o común dado que no puede 
utilizar terminos mas comunes o estructuras lexicas coloquiales.

Este metodo podria generar: "Fue en ese preciso instante que el jefe irrumpio en la habitación."
Sin embargo, no podria generar: "Y entonces el jefe entro en la habitación."

Este metodo tambien cuenta con una correción gramatical insuperable.


- Red interna preentrenada:

El metodo de red interna preentrenada permite escribir textos de manera completamente computacional, sin embargo,
no puede escribir textos gramaticamente correctos. Funciona mediante terminos anteriormente registrados en el 
sistema y usando el sistema de red neuronal ya guardaddo en el equipo con anterioridad. 
El sistema es optimo para un hambito mas coloquial o común dado que puede utilizar terminos mas comunes 
o estructuras lexicas coloquiales, además, permite una adición mas rapida de terminos nuevos o especializados. 

Este metodo no podria generar: "Fue en ese preciso instante que el jefe irrumpio en la habitación."
Sin embargo, podria generar: "pues sabes que el jefe viene y entra en el cuarto como si na"

Este metodo tambien cuenta con una correción gramatical baja y que debe ser muy revisada durante el preentreno.
Suele ser el metodo mas común para trabajo local.


- Red neuronal:

El metodo de red neuronal permite escribir textos de manera completamente computacional, sin embargo,
no puede escribir textos gramaticamente correctos. Funciona mediante terminos registrados en el 
sistema y usando el sistema de red neuronal procesado demanera continua durante la generación del termino. 
El sistema es optimo para un hambito mas coloquial o común dado que puede utilizar terminos mas comunes 
o estructuras lexicas coloquiales, además, permite una adición muchisimo rapida de terminos nuevos o especializados
sin la necesidad de reentrenar el sistema. 

Este metodo no podria generar: "Fue en ese preciso instante que el jefe irrumpio en la habitación."
Sin embargo, podria generar: "pues sabes que el jefe viene y entra en el cuarto como si na"

Este metodo tambien cuenta con una correción gramatical baja pero muy facil de regular.
Suele ser el metodo mas común para trabajo en host u online.

"""

"""
El ejemplo mas comun de cada uno son:

- Sitema de traducción de Google o Deepl.
- Modulos GPT para trabajo local.
- Chat GPT, Gemini, Copilot...
"""

"""
En este curso nos centraremos en los dos ultimos, dando mas prioridad a los modulos preentrenados.
"""