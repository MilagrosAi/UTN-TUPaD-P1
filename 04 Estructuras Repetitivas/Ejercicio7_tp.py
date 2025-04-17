'''7) Crea un programa que calcule la suma de todos los números
comprendidos entre 0 y un número entero positivo indicado por el usuario.  '''

num = int(input("Ingrese un numero entero positivo: "))
sumatoria = 0

for x in range(1,num):
    sumatoria = sumatoria + x
print(f"la suma de los numero es: {sumatoria}")
