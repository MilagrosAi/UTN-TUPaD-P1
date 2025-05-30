'''Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.
Ejemplos:
contar_digito(12233421, 2) → 3
contar_digito(5555, 5) → 4  '''

def contar_digito(numero,digito):
    #Caso base
    if numero < 10 :
        return 1 if numero == digito else 0 
    #caso recursivo
    else:
        ultimo_digito = numero % 10 
        return (1 if ultimo_digito == digito else 0) + contar_digito(numero // 10, digito)

#Programa principal
numero= int(input("Ingrese un numero entero positivo: "))
digito = int(input("Ingrese un digito a contar(0-9): "))
print (f"El digito {digito} aparece {contar_digito(numero, digito)} veces en {numero}")