'''' Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius 
y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.'''

def celcius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32


#Programa principal
celcius= float(input("Ingrese una temperatura en Celcius: "))
fahrenheit= celcius_a_fahrenheit(celcius)
print(f"{celcius} c equivalen a {fahrenheit} F")