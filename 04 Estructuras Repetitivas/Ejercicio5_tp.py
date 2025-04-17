'''5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, 
el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.  '''

import random
numero_aleatorio = random.randint(0,9)
#print(numero_aleatorio)
numero = int(input("Adivine el numero que la computadora creo entre el (0,9): "))

cont = 1
while numero != numero_aleatorio:
    numero = int(input("Error, intentelo de vuelta: "))
    cont = cont + 1
print(f"El usuario intento: {cont} veces adivinar el numero")