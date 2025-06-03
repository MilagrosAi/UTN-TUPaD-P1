''''Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).'''

# Conjuntos de estudiantes que aprobaron cada parcial
parcial_1 = {'Ana', 'Juan', 'Sofía', 'Pedro'}
parcial_2 = {'Juan', 'Sofía', 'Lucía', 'María'}

# 1. Estudiantes que aprobaron ambos parciales
aprobaron_ambos = parcial_1 & parcial_2

# 2. Estudiantes que aprobaron solo uno de los dos parciales 
solo_uno = parcial_1 ^ parcial_2

# 3. Lista total de estudiantes que aprobaron al menos un parcial 
al_menos_uno = parcial_1 | parcial_2

# Mostrar resultados
print("Estudiantes que aprobaron ambos parciales:", aprobaron_ambos)
print("Estudiantes que aprobaron solo un parcial:", solo_uno)
print("Estudiantes que aprobaron al menos un parcial:", al_menos_uno)