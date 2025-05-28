''''Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y 
devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar 
los resultados de forma clara. '''

def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    division = a // b
    multiplicacion = a * b
    return (suma, resta, division, multiplicacion)

#Programa principal
a= int(input("Ingrese el primer numero: "))
b= int(input("Ingrese el segundo numero: "))

resultado = operaciones_basicas(a,b)
print(f"La suma es: {resultado[0]}")
print(f"La resta es: {resultado[1]}")
print(f"La division es: {resultado[2]}")
print(f"La multiplicacion es: {resultado[3]}")