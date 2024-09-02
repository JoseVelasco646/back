# back

## Crear algoritmo de busquedad
Este programa encuentra la el camino mas corto y el camino mas largo.
-1 -2 3
'I' -1 -3
-1 -2 'F'
Por ejemplo, el programa debe de imprimir el camino mas corto y el camino mas largo de la matriz anterior.
Usamos un for que recorre la matriz y guardamos el valor.
Para lograr esto el programa recorre las filas y columnas y las almacena en un valor 'Y' y 'X'
EL valor y lo toma las filas y el valor x las columnas, cuando el programa encuentre el valor los retorna en y,x.
y si no encuentra los valores retorna un None, None representa que no esta el valor.
Para poder moverse de direccion se crea un arraya para poder moverse hacia arriba, abajo, izquierda y derecha.
EL programa valida si la fila esta dentro de los limites de la matriz al igual que las columnas.