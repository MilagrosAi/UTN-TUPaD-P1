""""escribir un programa que tome la lista
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
Definir la lista numeros_aleatorios de la siguiente forma:
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
forma aleatoria """

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median (numeros_aleatorios)
media = mean (numeros_aleatorios)

if media > mediana and mediana > moda:
    print("hay sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("sesgo negativo o a la izquierda")
elif media == mediana and media == moda:
    print("sin sesgo")
else:
    print("no se cumple ninguna de las tres")