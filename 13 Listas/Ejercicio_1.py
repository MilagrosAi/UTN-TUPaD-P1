''' 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
range'''

lista = list (range(1,101))
for i in lista:
    if i % 4 == 0:
        print(i)