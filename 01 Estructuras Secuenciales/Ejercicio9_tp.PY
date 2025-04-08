# Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# temp Fahrenheit= 9.5 / temp Celsius + 32
celsius= float(input("Ingrese una temperatura en Celsius:"))
fahrenheit = (9/5 * celsius) + 32
print(f"El equivalente en grados Fahrenheit es: {fahrenheit}")