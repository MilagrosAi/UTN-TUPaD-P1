''' 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y 
cuántos son positivos. (Nota: para probar el programa puedes
usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio)'''

cont_par = 0
cont_impar = 0
cont_positivo = 0
cont_negativo = 0

for x in range (0,100):
    num = int(input("Ingrese un numero: "))
    if num % 2 == 0:
        cont_par = cont_par + 1
    else:
        cont_impar = cont_impar + 1
    if num > 0:
        cont_positivo = cont_positivo + 1
    else: 
        cont_negativo = cont_negativo + 1

print(f"La cantidad de numero pares es:  {cont_par}")
print(f"La cantidad de numero impares es: {cont_impar}")
print(f"La cantidad de numero positivos es: {cont_positivo}")
print(f"La cantidad de numero negativos es: {cont_negativo}")



