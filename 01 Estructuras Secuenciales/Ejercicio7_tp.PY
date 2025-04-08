#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero = int(input("Ingrese un numero entero distinto de cero:"))
num = int(input("Ingrese el segundo numero entero distinto de cero:"))

print(f"La multiplicacion de los numeros enteros es: {numero* num}" )
print(f"La suma de los numero enteros es: {numero + num}")
print(f"La resta de {numero} menos {num} es: {numero - num}")
print(f"La resta de {num} menos {numero} es: {num - numero}")
print(f"La division de {numero} / {num} es: {numero/ num}")
print (f"La division de {num} / {numero} es: {num / numero}")