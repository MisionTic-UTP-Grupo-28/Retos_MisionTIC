"""Descripción:
-----------
 Retorna la cantidad de personas cuyo nombre es igual o similar a uno dad
o por parámetro
 Parámetros:
 -----------
 pname (str):
 Nombre buscado con el cual se espera encontrar coincidencias.

 Retorna:
 --------
 int: 0... N
"""

import pandas as pd

# def get_users_with_name(pname:str, url):
#     try:
#         pname = str(pname.lower().strip().capitalize())
#         url = str(url)
#         df = pd.read_json(url)
#         persons_list = list(df['results'])
#         # names_list = [ f"{i['name']['first']} {i['name']['last']}" for i in persons_list]
#         # print(names_list)
#         names_list = [i['name']['first'] for i in persons_list]
#         count = 0
#         for name in names_list:
#             if pname != '' and pname in name:
#                 count += 1

#         return count 
#     except:
#         return 0

def get_users_with_name(pname:str, url):
    try:
        pname = str(pname)
        url = str(url)
    except:
        return 0
        
    df = pd.read_json(url)
    persons_list = list(df['results'])
    names_list = [i['name']['first'] for i in persons_list 
                  if pname != '' and pname in i['name']['first']]
    return len(names_list)


print(get_users_with_name('Alan', 'users.json'))
print(get_users_with_name('Alban', 'users.json'))
print(get_users_with_name('', 'users.json'))
# print(get_users_with_name('1', 'users.json'))
# print(get_users_with_name(1 , 'users.json'))
# print(get_users_with_name('william' , 'https://magicsolutions.co/users.json'))




