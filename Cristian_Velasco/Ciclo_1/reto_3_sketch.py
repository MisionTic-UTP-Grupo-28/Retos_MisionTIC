"""
Determinar el promedio más alto y el más bajo de un grupo de estudiante 
 dadas sus calificaciones individuales 

-La solución debe permitir que se puedan evaluar múltiples entradas, lo cual
implica que el diccionario puede traer N cantidad de datos, es decir N canti
dad de estudiantes y sus notas.
 - Las notas están dadas en una lista la cual está contenida dentro
 del diccionario que ingresa por parámetro, el nombre de la lista
es "notas".
 - En caso de empate, se tomará como mejor y peor, el ultimo estudiante evaluad
o en la lista.
 - En caso de que el diccionario no tenga un formato adecuado se deberá 
 regresar un mensaje que diga: “El formato del diccionario no es válido”.

 Parámetros:
 -----------
 estudiantes (dictionary):
 Datos de los estudiantes como nombre y el registro de notas individual

 Retorna:
 --------
 str: Cadena de caracteres de la forma
 “El mejor estudiante es {nombre_mejor} con {mejor}. El últim
o estudiante es {nombre_peor} con {peor}”
"""


def dar_mejor_peor_estudiante(estudiantes):
    pass

# Entradas


entrada_1 = {0: {'name': 'Juan', 'notas': [3.1, 4.2, 4, 3.9, 3.2]},
             1: {'name': 'Ana', 'notas': [4.1, 4.7, 4.1, 4.9, 4.2]}}

entrada_2 = {0: {'name': 'Juan', 'notas': [3.1, 4.2, 4, 3.9, 3.2]},
             1: {'name': 'Ana', 'notas': [4.1, 4.1, 4.1, 4.9, 4.2]},
             2: {'name': 'Pedro', 'notas': [4, 3.7, 4, 4, 4.2]},
             3: {'name': 'Pablo', 'notas': [3, 3.3, 3.4, 3.2, 3.2]},
             4: {'name': 'Carlos', 'notas': [4.4, 4.8, 4.2, 4, 4.1]}}

entrada_3 = {0: {'name': 'Juan', 'notas': [3.1, 4.2, 4, 3.9, 3.2]},
             1: {'name': 'Ana', 'notas': [4.1, 4.7, 4.1, 4.9, 4.2]},
             2: {'name': 'Pedro', 'notas': [4, 3.7, 4, 4, 4.2]},
             3: {'name': 'Pedro', 'notas': [3, 3.3, 3.4, 3.2, 3.2]},
             4: {'name': 'Carlos', 'notas': [3.4, 3.8, 4.2, 4, 4.1]},
             5: {'name': 'Maria', 'notas': [4.4, 4.7, 4.6, 4.1, 4.2]},
             6: {'name': 'Luisa', 'notas': [4.8, 4.7, 4.5, 4.5, 4.9]}}

entrada_4 = {
    0: {'name': 'Juan', 'notas': [3.1, 4.2, 4, 3.9, 3.2]},
    1: {'name': 'Carlos', 'notas': [3.1, 4.2, 4, 3.9, 3.2]},
    2: {'name': 'Noemi', 'notas': [3.1, 4.2, 4, 3.9, 3.2]},
    3: {'name': 'Shoco', 'notas': [3.1, 4.2, 4, 3.9, 3.2]},
}


notas = [i['notas'] for i in entrada_4.values()]
# print(notas)
# print(round(sum(notas[0])/len(notas[0]), 2))

count = 0
peor = 5
mejor = 0
for i in range(len(notas)):
    promedio = round(sum(notas[i])/len(notas[i]), 2)
    if promedio <= peor:
        peor = promedio
        nombrePeor = entrada_4[count]['name']
    if promedio >= mejor:
        mejor = promedio
        nombreMejor = entrada_4[count]['name']
    # print(entrada_3[count]['name'], promedio)
    count += 1

print(mejor, nombreMejor)
print(peor, nombrePeor)


# print(promedios)

# print(dar_mejor_peor_estudiante(entrada_1))
# print(dar_mejor_peor_estudiante(entrada_2))
# print(dar_mejor_peor_estudiante(entrada_3))
