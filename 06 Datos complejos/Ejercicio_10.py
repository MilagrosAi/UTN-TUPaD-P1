paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago',
    'Perú': 'Lima'
}

# Crear diccionario invertido
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}


print("Diccionario invertido:")
print(capitales_paises)
