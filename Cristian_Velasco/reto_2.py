""" Determina el estudiante con el mejor promedio dada una lista
(Diccionario) con los datos de 4 estudiantes

 -En caso de que dos o mas alumnos tengan el mismo promedio, el
 mejor promedio sera el del primer alumno evaluado dentro del empate
 Parámetros:
 -----------
 estudiantes (dictionary):
 Lista de estudiantes con nombre y promedio.

 Retorna:
 --------
 str: Cadena de caracteres de la forma
 “Con {promedio}, el mejor estudiante es {nombre}”
"""

def determinar_mejor_promedio(estudiantes):
    if estudiantes['prom1'] >= estudiantes['prom2'] >= \
    estudiantes['prom3'] >= estudiantes['prom4']:
        return f"Con {estudiantes['prom1']}, el mejor estudiante es {estudiantes['est1']}"
    elif estudiantes['prom2'] >= estudiantes['prom3'] >= estudiantes['prom4']:
        return f"Con {estudiantes['prom2']}, el mejor estudiante es {estudiantes['est2']}"
    elif estudiantes['prom3'] >= estudiantes['prom4']:
        return f"Con {estudiantes['prom3']}, el mejor estudiante es {estudiantes['est3']}"
    else:
        return f"Con {estudiantes['prom4']}, el mejor estudiante es {estudiantes['est4']}"



 

        
# entradas:

estudiantes_1 = {'est1': 'Ana', 'prom1': 4.1, 'est2': 'Juan', 'prom2':
4.2, 'est3': 'Pedro', 'prom3': 4.3, 'est4': 'Carla',
'prom4': 4.4}

estudiantes_2 = {'est1': 'Ana', 'prom1': 4.1, 'est2': 'Juan', 'prom2':
4.5, 'est3': 'Pedro', 'prom3': 4.4, 'est4': 'Carla',
'prom4': 4.3}

estudiantes_3 = {'est1': 'Ana', 'prom1': 4, 'est2': 'Juan', 'prom2':
4, 'est3': 'Pedro', 'prom3': 4, 'est4': 'Carla',
'prom4': 4}

print(determinar_mejor_promedio(estudiantes_1))
print(determinar_mejor_promedio(estudiantes_2))
print(determinar_mejor_promedio(estudiantes_3))
