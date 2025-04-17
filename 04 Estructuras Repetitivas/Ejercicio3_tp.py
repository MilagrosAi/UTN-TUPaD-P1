''''3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores '''


num_1 = int(input("ingrese el primer valor: "))
num_2 = int(input("Ingrese el segundo valor: "))
sumatoria = 0

for cont in range(num_1, num_2):
    sumatoria = sumatoria + cont

print(f"La suma de los dos valores es: {sumatoria}")
