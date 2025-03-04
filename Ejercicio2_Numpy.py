# Imprima el código y el nombre de los estudiantes de la carrera X (debe leerse el código de la carrera a listar) 
# Con promedio acumulado igual o mayor a 4 y decir cuántos fueron.

# Imprima el código y el nombre de los estudiantes que ingresaron antes de 1990 y están condicionales.

# Datos:
# 6500 estudiantes
# Nombre, codigo y promedio acumulado por cada estudiante

import numpy as np

estudiantes = 6500

np.random.seed(0)  
codigos = np.arange(1, estudiantes + 1)
nombres = np.array([f"Estudiante_{i}" for i in range(1, estudiantes + 1)])
promedios = np.random.uniform(2.0, 5.0, estudiantes)  
añoIngreso = np.random.randint(1980, 2025, estudiantes)
carreras = np.random.randint(1, 11, estudiantes)  


codigoCarrera = int(input("Ingrese el código de la carrera: "))
# Estudiantes con promedio igual o mayor a 4.0

Acumulado = (carreras == codigoCarrera) & (promedios >= 4.0)
estAcumulado = np.column_stack((codigos[Acumulado], nombres[Acumulado], promedios[Acumulado]))

# Estudiantes condicionales ingresados antes de 1990

Condicional = (añoIngreso < 1990) & (promedios >= 2.7) & (promedios < 3.2)
estCondicionales = np.column_stack((codigos[Condicional], nombres[Condicional], promedios[Condicional]))


print(f"\nEstudiantes de la carrera {codigoCarrera} con promedio igual o mayor a 4.0 :")
if estAcumulado.size > 0:
    for codigo, nombre, promedio in estAcumulado:
        print(f"Código: {int(codigo)}, Nombre: {nombre}, Promedio: {float(promedio):.2f}")
    print(f"\nTotal de estudiantes con promedio igual o mayor a 4.0:  {len(estAcumulado)}\n")
else:
    print("No hay estudiantes con promedio mayor o igual a 4.0 en esta carrera.\n")


print(f"\n Estudiantes que ingresaron antes de 1990 y están condicionales: ")
num_mostrar = min(20, len(estCondicionales))  
if num_mostrar > 0:
    for codigo, nombre, promedio in estCondicionales[:num_mostrar]:
        print(f"Código: {int(codigo)}, Nombre: {nombre}, Promedio: {float(promedio):.2f}")
    print(f"\nTotal de estudiantes condicionales: {len(estCondicionales)}\n")
else:
    print("No hay estudiantes condicionales que ingresaron antes de 1990.\n")
