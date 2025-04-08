#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.
radio = float(input("Ingrese el radio del circulo:"))
pi = 3.14159
perimetro = 2 * pi * radio
area = pi * radio * radio

print(f"El area del circulo es: {area}")
print(f"El perimetro del circulo es: {perimetro}")