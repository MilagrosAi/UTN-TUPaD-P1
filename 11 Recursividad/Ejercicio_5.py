'''Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.
Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reverse
palindromo= Palabra o frase cuyas letras están dispuestas de tal manera que resulta la misma leída de izquierda a 
derecha que de derecha a izquierda '''

def es_palindromo(palabra):
    #caso base
    if len(palabra) <= 1:
        return True
    #caso recursivo
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

#Programa principal
palabra= input("Ingrese una palabra: ")
Resultado= es_palindromo(palabra)
print(f"{palabra} es palidromo?: {Resultado}")