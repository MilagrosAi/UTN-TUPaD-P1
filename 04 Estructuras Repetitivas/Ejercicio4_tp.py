''''4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0. '''

num_entero = int(input("Ingrese un numero entero, (0 para detenerse): "))
sumatoria = 0

while num_entero != 0:
    sumatoria = sumatoria + num_entero
    num_entero = int(input("Ingrese un numero entero, (0 para detenerse): "))
print(f"la sumatoria es: {sumatoria}")
