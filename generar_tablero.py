# Tiene como objetivo el de generar el tablero de una sopa de letras. 
# Recibe un número N y una lista de palabras. 
# Retorna una matriz (lista de listas) de dimensiones NxN donde en cada posición hay una letra. 
# La matriz representa el tablero de sopa de letras y en cada posición tiene que haber una letra. 
# El tablero devuelto tiene que contener las palabras entre
# todas las letras de forma horizontal o de forma vertical. Los casilleros que no contengan una letra de las palabras a ubicar,
# deben tener una letra generada de forma aleatoria. Todas las letras tienen que estar en minúscula
# Consejo: Intentar de insertar las palabras de a una en lugares aleatorios. 
# En el caso de no ser posible re intentarlo hasta que se logre.

from random import randint, choice


def validar_posicion(palabra, seccion):
    for i, letra in enumerate(seccion):
        if (letra == "" or letra == palabra[i]):
            continue
        else:
            return False
    return True

def insertar_palabra(direccion, sentido, palabra, tablero):
    maxIntentos = 100
    contador = 0
    if direccion == 0: # horizontal
        fila = randint(0,len(tablero)-1)
        posicion = randint(0, len(tablero)-len(palabra))
        seccion = tablero[fila][posicion:len(palabra)+posicion]
        if sentido == 0: # izq -> der
            while not validar_posicion(palabra, seccion):
                fila = randint(0,len(tablero)-1)
                posicion = randint(0, len(tablero)-len(palabra))
                seccion = tablero[fila][posicion:len(palabra)+posicion]
                contador += 1
                if contador >= maxIntentos:
                    return "error"
            tablero[fila][posicion:len(palabra)+posicion] = list(palabra)
            palabra_sol = [palabra,posicion,fila,len(palabra)+posicion-1,fila]
        else: # der -> izq
            while not validar_posicion(palabra[::-1], seccion):
                fila = randint(0,len(tablero)-1)
                posicion = randint(0, len(tablero)-len(palabra))
                seccion = tablero[fila][posicion:len(palabra)+posicion]
                contador += 1
                if contador >= maxIntentos:
                    return "error"
            tablero[fila][posicion:len(palabra)+posicion] = list(palabra)[::-1]
            palabra_sol = [palabra,len(palabra)+posicion-1,fila,posicion,fila]
    else: # vertical
        columna = randint(0,len(tablero)-1)
        posicion = randint(0, len(tablero)-len(palabra))
        seccion =  [fila[columna] for fila in tablero][posicion:len(palabra)+posicion]
        if sentido == 0: # arriba -> abajo
            while not validar_posicion(palabra, seccion):
                columna = randint(0,len(tablero)-1)
                posicion = randint(0, len(tablero)-len(palabra))
                seccion =  [col[columna] for col in tablero][posicion:len(palabra)+posicion]
                contador += 1
                if contador >= maxIntentos:
                    return "error"
            for j in range(posicion, posicion+len(palabra)):
                tablero[j][columna] = palabra[j-posicion]
            palabra_sol = [palabra,columna,posicion,columna,posicion+len(palabra)-1]
        else: # abajo -> arriba
            while not validar_posicion(palabra[::-1], seccion):
                columna = randint(0,len(tablero)-1)
                posicion = randint(0, len(tablero)-len(palabra))
                seccion =  [col[columna] for col in tablero][posicion:len(palabra)+posicion]
                contador += 1
                if contador >= maxIntentos:
                    return "error"
            for j in range(posicion, posicion + len(palabra)):
                tablero[j][columna] = palabra[::-1][j-posicion]
            palabra_sol = [palabra,columna,posicion+len(palabra)-1,columna,posicion]   
    return [tablero, palabra_sol]

def generar_tablero(n, palabras):
    tablero = [["" for x in range(n)] for y in range(n)]
    solucion = {} 
    palabras.sort(key = len, reverse = True)
    for palabra in palabras:
        direccion = randint(0,1) # 0 horizontal 1 vertical
        sentido = randint(0,1) # 0 izq -> der 1 der -> izq o 0 arriba -> abajo 1 abajo -> arriba
        tablero, palabra_sol = insertar_palabra(direccion, sentido, palabra, tablero)
        solucion[palabra_sol[0]] = {"x_inicial": palabra_sol[1], "y_inicial": palabra_sol[2], "x_final": palabra_sol[3], "y_final": palabra_sol[4]}
        if tablero == "error":
            tablero = generar_tablero(n, palabras)
    for i in range(n):
        for j in range(n):
            if tablero[i][j] == "":
                tablero[i][j] = choice("abcdefghijklmnopqrstuvwxyz")
    return [tablero, solucion]


def visualizar_tablero(tablero):
    separador = " | "
    for fila in tablero:
        print(separador.join(map(str,fila)))


#n = 4
#palabras = ['inu', 'te', 'amo'] 
#[tablero, solucion] = generar_tablero(n, palabras)
#visualizar_tablero(tablero)
