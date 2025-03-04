# Elección del representante de los estudiantes ante el Consejo Superior.
# Imprima un listado de mayor a menor, según el número de votos obtenidos por cada candidato

#Datos
# 30 candidatos identificados con un número del 1 al 30
#5000 estudiantes votaron

import numpy as np

numVotos = 5000
numCandidatos = 30


#Cada estudiante vota por un candidato
votos = np.random.randint(1, numCandidatos + 1, numVotos)

# Conteo de votos
Resultados = np.bincount(votos)[1:] # Para que omita el 0

# Array para candidatos
candidatos = np.arange(1, numCandidatos + 1)

#Mayor número de votos a menor número de votos

ordenados = np.argsort(Resultados)[::- 1]
candidatosMM = candidatos[ordenados]
votosMM = Resultados[ordenados]


print("Resultados elecciones :")
for candidato, votos in zip(candidatosMM, votosMM):
    print(f"{candidato:10} ---> {votos}")
