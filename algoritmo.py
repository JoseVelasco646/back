m = ([[-1,2,3],
       ['I',1,-3],
       [-1,-2,'F']
                   ])

matriz = m.copy()
filas = len(matriz)
columnas = len(matriz)
caminoCorto = None
caminoLargo = None
coordenadaLarga = []
coordenadaCOrta = []


def encontrar_coordenadas(valor):
    for y in range(filas):
         for x in range(columnas):
              if matriz[y][x] == valor:
                   return (y,x)

inicio = encontrar_coordenadas('I')
fin = encontrar_coordenadas('F')

def buscar_camino(y,x):
     if (y,x) == fin:
          