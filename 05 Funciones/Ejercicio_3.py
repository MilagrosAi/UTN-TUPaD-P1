''''Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba 
cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
Pedir los datos al usuario y llamar a esta función con los valores ingresados. '''

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido} , tengo {edad} años y vivo en {residencia}")

#Programa principal
nombre= input("Ingrese su nombre por favor: ")
apellido= input("Ingrese su apellido por favor: ")
edad= input("Ingrese su edad por favor: ")
residencia = input("Ingrese el lugar donde vive por favor: ")

informacion_personal(nombre, apellido, edad, residencia)