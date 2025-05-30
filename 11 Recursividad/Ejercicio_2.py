'''Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique. '''

def fib(n):
    if n <= 1:
        return n
    else:
        return fib (n - 1) + fib(n - 2)

num= int (input("Posicion: "))
for i in range (1, num + 1):
    print(f"F({i}) = {fib(i)}")