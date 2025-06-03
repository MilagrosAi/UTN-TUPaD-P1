agenda = {
    ('Lunes', '10:00'): 'Reunión con equipo',
    ('Martes', '14:00'): 'Clase de Python',
    ('Miércoles', '09:00'): 'Cita médica'
}

# Consultar actividad
dia = input("Ingrese el día (ej. Lunes): ")
hora = input("Ingrese la hora (ej. 10:00): ")

# Verificar si la tupla (día, hora) existe en la agenda
actividad = agenda.get((dia, hora), 'No hay eventos programados')
print(f"En {dia} a las {hora}: {actividad}")

# Mostrar agenda completa
print("Agenda completa:")
for (dia, hora), evento in agenda.items():
    print(f"{dia} {hora}: {evento}")