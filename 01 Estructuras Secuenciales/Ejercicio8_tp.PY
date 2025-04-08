#Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo: IMC = peso en kg / (altura en m)2

altura = float(input("Ingrese su altura por favor:"))
peso = float(input("Ingrese su peso por favor:"))
IMC = peso / (altura**2)
print(f"El indice de masa corporal es de: {IMC}")