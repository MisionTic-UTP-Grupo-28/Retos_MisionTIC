def buscar_estudiantes(nota):
    """
    Conocer los estudiantes cuyo promedio este por debajo
    de una nota dada como parametro

    Parámetros:
    -----------
    nota (float):
    Nota minima con la cual se calcula cuantos alumnos suben.

    Retorna:
    --------
    list: "[{student}...]"
    -En caso de que el dato ingresado no sea un float:
    "Error en el dato ingresado"
    """
    
    students = {'a': {'name': 'Juan', 'notas': [3.1, 2.2, 2.5, 3.9, 3.2]},
                'j': {'name': 'Jenny', 'notas': [2, 3.7, 2, 2, 2.2]},
                'c': {'name': 'Ana', 'notas': [2.6, 2.7, 2.1, 2.9, 2.2]},
                'y': {'name': 'Pedro', 'notas': [2, 3.5, 2, 2, 2.2]},
                'x': {'name': 'Pablo', 'notas': [2, 3.3, 3.9, 3.2, 3.2]},
                'l': {'name': 'Carlos', 'notas': [3.2, 3.8, 2.2, 2, 2.1]},
                'v': {'name': 'Maria', 'notas': [2.8, 2.7, 2.8, 2.9, 2.8]},
                'r': {'name': 'Luisa', 'notas': [2.8, 2.7, 3.5, 2.5, 2.9]},
                'b': {'name': 'Mario', 'notas': [2.2, 3.2, 3, 3.2, 2.2]},
                'g': {'name': 'Fabio', 'notas': [2.4, 3.2, 3.1, 3.2, 2.2]}}

    try:
        nota = float(nota)
        result = []
        average = [round(sum(i['notas'])/len(i['notas']), 2)
                   for i in students.values()]
        students_list = list(students.values())

        filter_average = list(filter(lambda x: x < nota, average))

        for i in filter_average:
            result.append(students_list[average.index(i)])

        return result
    except:
        return 'Error en el dato ingresado'



print(buscar_estudiantes(2.8))
print(buscar_estudiantes(1))
print(buscar_estudiantes('a'))
