def dar_mejor_peor_estudiante(estudiantes):
    try:
        count = 0
        peor = 5
        mejor = 0
        notas = [i['notas'] for i in estudiantes.values()]

        for i in range(len(notas)):
            if len(notas[i]) < 5 or bool([x for x in notas[i] if x < 0]):
                return 0/0

            promedio = round(sum(notas[i])/len(notas[i]), 2)

            if promedio <= peor:
                peor = promedio
                nombre_peor = estudiantes[count]['name']
            if promedio >= mejor:
                mejor = promedio
                nombre_mejor = estudiantes[count]['name']
            count += 1

        return f'El mejor estudiante es {nombre_mejor} con {mejor}.' + \
            f' El peor estudiante es {nombre_peor} con {peor}'
    except:
        return 'El formato del diccionario no es válido'


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
    0: {'name': 'Juan', 'notas': [3, 4.2, 4, 3.9, 3.2]},
    1: {'name': 'Carlos', 'notas': [3.1, 4.2, 4, 3.9, 3.2]},
    2: {'name': 'Noemi', 'notas': [3.1, 4.2, 4, 3.9, 3.2]},
    3: {'name': 'Shoco', 'notas': [3.4, 4.2, 4, 3.9, 3.2]},
}


print(dar_mejor_peor_estudiante(entrada_1))
print(dar_mejor_peor_estudiante(entrada_2))
print(dar_mejor_peor_estudiante(entrada_3))
print(dar_mejor_peor_estudiante(entrada_4))
