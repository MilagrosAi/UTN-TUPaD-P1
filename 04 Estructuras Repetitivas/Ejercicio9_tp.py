''' 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media 
de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder
procesar 100 números cambiando solo un valor)'''

sumatoria = 0
media = 0

for x in range(0,100):
    num = int(input("Ingrese un valor entero: "))
    sumatoria = sumatoria + num 
    media = sumatoria / (x + 1)

print(f"La media es, {media}")
