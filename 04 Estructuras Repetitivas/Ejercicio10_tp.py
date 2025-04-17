'''10) Escribe un programa que invierta el orden de los dígitos de un número ingresado 
por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.  '''

num = int(input("Ingrese un numero: "))
num_abs = abs(num)
num_invertido = 0 

while num_abs > 0:
    digito = num_abs % 10
    num_invertido = num_invertido * 10 + digito
    num_abs = num_abs // 10
if num < 0:
    num_invertido = - num_invertido

print(f"El numero invertido es: {num_invertido}")