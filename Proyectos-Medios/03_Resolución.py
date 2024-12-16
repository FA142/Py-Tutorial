"""
Se pide crear un programa que cambie las monedas contennidas en un JSON. Usa el metodo ".upper()" .
"""
import json

with open ("03_Ejercício.json", 'r') as archivo:
    tasas = json.load(archivo)

def buscar_tasa(origen, destino):

    for tasa in tasas:      # Prueba cada posible respuesta.

        if tasa["origen"] == origen and tasa["destino"] == destino: 

# Prueba que el origen y el destino coinciden.
            return (tasa["tasa"])
# Devuelve el valor del numero equivalente a la tasa.

        else:
            pass    # Pasa sin hacer nada.
 
ori = str(input("Moneda a convertir:").upper())

cantidad = int(input(f'Cantidad de {ori} a convertir:'))

des = str(input(f'A que moneda desea convertir los {cantidad} {ori}:').upper())

tasa = buscar_tasa(origen=ori, destino=des)

conversion = cantidad*tasa

print (f'{cantidad} {ori} equivalen a {conversion} {des} segun el archivo JSON proporcionado.')