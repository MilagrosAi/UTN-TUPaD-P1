''''Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva 
el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva 
el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar 
los resultados. '''

import math
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

#Programa principal
radio= float(input("Ingresa el radio: "))
area= calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)


print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")

