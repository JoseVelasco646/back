import numpy as np
matriz = np.array([['I',-3,2,-3,3,-2,-2,1,2,0,2,0,1],
                   [2,3,2,-1,-1,3,2,0,-3,-3,2,2,1],
                   [1,-3,-3,2,3,1,3,3,2,1,-2,-2,3],
                   [0,0,3,0,3,-3,-2,-3,0,2,2,1,1],
                   [2,-1,-1,-3,3,3,0,-3,1,-2,2,0,1],
                   [0,3,-1,1,-1,-2,2,-2,2,-1,-2,-3,0],
                    [0,3,2,0,1,1,2,3,-1,-3,0,0,-2],
                    [3,3,-3,-2,3,-3,-1,-3,3,-2,2,-2,-1],
                    [-2,-2,1,0,-1,0,3,0,0,-2,2,-3,-1],
                    [-3,3,0,-1,-3,1,2,-3,2,-3,0,2,-2],
                    [-3,-3,-3,3,-2,0,-2,-3,1,0,1,-1,-2],
                    [-1,0,1,2,1,0,'F',0,-3,3,3,-2,-1],
                    [1,-3,1,0,1,2,3,1,-2,3,3,0,3]
                   ])


for fila in range(0, len(matriz)):
    for columna in range(0, len(matriz[fila])):
        elemento = matriz[fila][columna]
        if elemento == 'F':
            print('Elemento encontrado')
            coordenadasX = columna + 1
            coordenadasY = fila + 1
            print(f"Las coordenas son: ({coordenadasX}, {coordenadasY})")

