"""Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
lower() y title() de Python para convertir entre mayúsculas y minúsculas. """

nombre = input("Escriba su nombre por favor:")

opcion = input("Elija una opción (1 para mayúsculas, 2 para minúsculas, 3 para primera letra mayúscula): ")

if opcion == "1":
    resultado = nombre.upper()  
    print(resultado)
elif opcion == "2":
    resultado = nombre.lower()  
    print(resultado)
elif opcion == "3":
    resultado = nombre.title()  
    print(resultado)
else:
    print("Opción no válida. Por favor, ingrese 1, 2 o 3.")

