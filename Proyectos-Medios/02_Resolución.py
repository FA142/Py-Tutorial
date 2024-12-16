"""
Se pide crear una calculadora de masa corporal que clasifique el resultado.
"""
peso = 0
altura = 0
IMC = 0

def calcualar (peso, altura):
    IMC = peso / (altura ** 2)
    return IMC

def clasificar (IMC):
    if IMC < 18.5:
        print ("Peso bajo.")

    elif IMC < 25:
        print ("Peso normal.")
    
    elif IMC < 29.9:
        print ("Peso alto.")
    
    else:
        print ("Peso demasiado alto.")

print ("Calculadora de IMC.")

peso = float(input ("Peso:"))
altura = float(input ("Altura:"))

if altura == 0 or peso == 0:            # Nos anticipamos al error de dividir por 0.
    print ("Datos introducidos no viables.")
print (f'Tu IMC es de {calcualar(peso, altura)}')

clasificar(calcualar(peso, altura))