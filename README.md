# Crear un programa que dibuje una matriz con las siguientes condiciones:
## - La cantidad de filas y columnas debe ser definida por el usuario.
## - Que se logre dibujar filas y columnas indicadas por el usuario.
***
## A continuacion dejare algunos fragmentos del codigo donde se explica el funccionamiento ya que los commentarios complica mucho la lectura del codigo:
***
- 1) Mediante la estructura condicional 'if', compararemos los valores ingresados por el usuario. Si son menores a 1, le indicaremos que ha ocurrido un error y se ejecutará nuevamente el ciclo 'while'.
```
    if columnas < 1 or lineas < 1:
        print("\nError: ingresa un valor valido para número de columnas y/o líneas")
```
***
- 2) Si no se cumple la condición del 'if', significa que los valores ingresados son superiores a 0, y procedemos con la ejecución de la matriz. Crearemos una variable llamada 'columnas_valor_usuario' donde guardaremos el valor inicial de las columnas a dibujar, el cual fue indicado por el usuario, ya que lo necesitaremos más adelante. Si el número ingresado para las columnas es 1, se imprimirá en pantalla lo siguiente: (+---+). De lo contrario, se imprimirán los mismos caracteres, con la diferencia de que llevarán la instrucción 'end=""', lo que significa que el siguiente valor se imprimirá en la misma fila sin salto de línea. En las comillas no indicaremos nada, ya que necesitamos que los elementos se impriman uno al lado del otro.
```
    else:
        columnas_valor_usuario = columnas
        if columnas == 1:
            print ("+---+")
        else:
            print ("+---+", end="")
```
***
- 3) El ciclo 'while' nos ayudará a completar la parte superior de la matriz con los elementos restantes si el usuario solicita un número de columnas mayor o igual a 2. Con la estructura 'if', controlaremos la impresión de los elementos intermedios, donde la variable 'columnas' servirá como contador para la ejecución del 'while'. La estructura 'else' se utilizará para la impresión del elemento final en la línea superior de la matriz.
```
            while columnas >= 2:
                if columnas > 2:
                    print ("---+", end="")
                    columnas -= 1
                else:        
                    print ("---+")
                    columnas -= 1
```
***
- 4) El siguiente ciclo 'while' se encargará de la impresión de las partes laterales y los elementos de abajo que cerrarán la matriz. En esta parte, la variable 'líneas' será el contador del siguiente ciclo, que se decrementará de uno en uno en cada pasada por el ciclo hasta completar las líneas de la matriz solicitadas por el usuario. En la siguiente instrucción, podemos ver cómo se reutiliza el valor de la variable 'columnas' que guardamos al inicio en la variable 'columnas_valor_usuario'. Utilizaremos la misma lógica que empleamos para la impresión de los elementos superiores de la matriz: si es una línea, completaremos la celda con los elementos faltantes. De lo contrario, trabajaremos la matriz por elementos separados, imprimiremos la parte lateral.
```
        while lineas > 0:
            lineas -= 1
            columnas = columnas_valor_usuario
            if columnas == 1:
                print ("|   |")
                print ("+---+")
            else:    
                print ("|   |", end="")
                columnas = columnas_valor_usuario
```