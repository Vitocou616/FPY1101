#Promedio de asistencia guason D:

import json

lista_diccionario = []
with open("archivo.json", "r") as archivo:
    datos_leidos = json.load(archivo)
    for i in datos_leidos:
        lista_diccionario.append(i)

asistencia = []

for i in lista_diccionario:
    if i["asistencia_final"] == "asistencia_final":
        continue
    asistencia.append((int(i["asistencia_final"])))

print(f"Total de asistencias: {asistencia}")
promedio_asistencia = round(sum(asistencia)) / len(asistencia)
print(promedio_asistencia)