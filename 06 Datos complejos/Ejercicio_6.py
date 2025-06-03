''''6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno '''


alumnos = {
    'Milagros': (8, 7, 9),
    'Gabriel': (6, 5, 7),
    'Marta': (9, 8, 10)
}

# Mostrar promedios
print("Promedios de los alumnos:")
for nombre, notas in alumnos.items():
    print(f"{nombre}: {sum(notas)/len(notas):.2f}")