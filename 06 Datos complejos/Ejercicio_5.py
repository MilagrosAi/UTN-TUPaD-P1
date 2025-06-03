'''Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra. '''

from collections import Counter
frase = input("Ingrese una frase: ")

# Convertir la frase a minúsculas y dividirla en palabras
palabras = frase.lower().split()

# Obtener palabras únicas usando un set
palabras_unicas = set(palabras)

# Contar palabras usando Counter
conteo_palabras = Counter(palabras)

# Imprimir resultados
print("Palabras únicas:", palabras_unicas)
print("Conteo de palabras:", dict(conteo_palabras))