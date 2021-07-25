"""
Pseudocode

data
 ganado_heredado -> int
 hijoMayor = hijoMenor * 3
 hijoMedio = hijoMenor * 2
 hijoMenor = x % 6 

1. definir funcion calcular_herencia(ganado_heredado)
2. declarar variable hijoMenor = ganado_heredado / 6
3. declarar variable hijoMedio = hijoMenor * 2 
4. declarar variable hijoMayor = hijoMenor * 3 
5. retornar cadena = “Total: {ganado_heredado}
 Hijo mayor: {ganado_heredado_hermano_mayor}
 Hijo del medio: {ganado_heredado_hermano_medio}
 Hijo menor: {ganado_heredado_hermano_menor}.”
6. imprimir llamar funcion calcular_herencia(180)...
7.fin
 """


def calcular_herencia(ganado_heredado):
  hijoMenor = int(ganado_heredado / 6) 
  hijoMedio = hijoMenor * 2   
  hijoMayor = hijoMenor * 3

#  resultado = f"""Total: {ganado_heredado}
#Hijo mayor: {hijoMayor}
#Hijo del medio: {hijoMedio}
#Hijo menor: {hijoMenor}"""
  resultado = f"Total: {ganado_heredado} \nHijo mayor: {hijoMayor}"\
              + f"\nHijo del medio: {hijoMedio} \nHijo menor: {hijoMenor}"
  
  return resultado
  

print(calcular_herencia(180))
print(calcular_herencia(6))
print(calcular_herencia(18))

 
