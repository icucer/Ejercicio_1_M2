# Encabezado y nombre del programa.
print ("\n+------------------------------------+")
print ("|  Crearemos una tabla de n celdas.  |")
print ("+------------------------------------+")

# Crearemos dos variables "columnas" y "líneas" y le asignamos el valor de 0
# para inicializar el ciclo while.
columnas = 0
lineas = 0

# Crearemos un ciclo while para controlar el ingreso de datos por el usuario.
while columnas < 1 or lineas < 1:
    columnas = int(input("\nIngrese número de columnas que tendrá la tabla\n"))
    lineas = int(input("\nIngrese número de líneas que tendrá la tabla\n"))

    # 1) para el funcionamiento revisar README.md
    if columnas < 1 or lineas < 1:
        print("\nError: ingresa un valor valido para número de columnas y/o líneas")
    
    # 2) para el funcionamiento revisar README.md
    else:
        columnas_valor_usuario = columnas
        if columnas == 1:
            print ("+---+")
        else:
            print ("+---+", end="")

            # 3) para el funcionamiento revisar README.md
            while columnas >= 2:
                if columnas > 2:
                    print ("---+", end="")
                    columnas -= 1
                else:        
                    print ("---+")
                    columnas -= 1

        # 4) para el funcionamiento revisar README.md
        while lineas > 0:
            lineas -= 1
            columnas = columnas_valor_usuario

            if columnas == 1:
                print ("|   |")
                print ("+---+")
            else:    
                print ("|   |", end="")
                columnas = columnas_valor_usuario
                
                # Con 1-er while, trabajaremos la parte lateral de las celdas tomando en consideracion el numero de las columnas.
                while columnas >= 2:

                    # Si tenemos mas de dos columnas se ejecutara el if que nos imprimirá los elementos intermedios.
                    if columnas > 2:
                        print ("   |", end="")
                        columnas -= 1
                    
                    # En caso si es igual a 2 se ejecutaran los siguientes instrucciones.
                    else:
                        print ("   |")
                        print ("+---+", end="")
                        columnas = columnas_valor_usuario # Nuevamente vamos a reiniciar el valor de las columnas con el valor inicial.

                        # Y finalmente el ultimo ciclo while que se encargara de los elementos inferiores intermedios,
                        # con la misma lógica de funcionamiento.
                        while columnas >= 2:
                            if columnas > 2:
                                print ("---+", end="")
                                columnas -= 1
                            else:
                                print ("---+")
                                columnas -= 1
    
    # Punto donde termina el programa. Ya que en caso contrario se ejecutara infinitas veces.
    break