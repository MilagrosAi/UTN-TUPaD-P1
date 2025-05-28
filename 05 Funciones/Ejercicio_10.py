''''Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y 
devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta
función. '''

def calcular_promedio(a,b,c):
    return (a + b + c) // 3

#Programa principal
a= int(input("Ingresa el primer numero: "))
b= int(input("Ingresa el segundo numero: "))
c= int(input("Ingresa el tercer numero: "))
promedio = calcular_promedio(a,b,c)
print(f"El promedio es: {promedio}")