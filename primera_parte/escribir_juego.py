# El objetivo de esta función es la de escribir en archivos el juego (el tablero y la solución).
# Esta función recibe una matriz de NxN, un diccionario de palabras con sus ubicaciones y el nombre del archivo. 
# Tiene que escribir dos archivos:
# ● nombre_del_archivo.csv: Escribe el tablero (la matriz) en un formato que luego pueda leerse y convertirse nuevamente
#   en matriz de forma sencilla. Se recomienda guardarlo como CSV (sin columnas), donde cada línea es una fila de la matriz
#   y las letras están separadas con coma. Recomendación: Revisar la liberia csv, en especial el método writerow.
# ● nombre_del_archivo_solucion.csv: Escribe las palabras a partir del diccionario de solución. 
#   Se espera que el diccionario de palabras tenga la siguiente forma:
# { "casa": { "x_inicial": 0, "y_inicial": 0, "x_final": 3, "y_final": 0 } ... }
# Se entiende que la fila 0 de la matriz es la primera contando desde arriba y la columna 0 es la primera contando de izquierda a derecha. 
# El formato del archivo debe ser un CSV con las siguientes columnas: palabra, , y_inicial, y_final, x_final.

import csv
from generar_tablero import generar_tablero
from pedir_datos_tablero import pedir_datos_tablero


def escribir_juego(tablero, palabras_sol, nombre):
    with open(f"{nombre}.csv", "w", newline='\n', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        for fila in tablero:
            escritor.writerow(fila)
    with open(f"{nombre}_solucion.csv", "w", newline='\n', encoding='utf-8') as archivo:
        titulos = ["palabra", "x_inicial", "y_inicial", "x_final", "y_final"]
        escritor = csv.DictWriter(archivo, fieldnames=titulos)
        escritor.writeheader()
        for palabra, posiciones in palabras_sol.items():
            escritor.writerow({
                "palabra": palabra, 
                "x_inicial": posiciones["x_inicial"], 
                "y_inicial": posiciones["y_inicial"],
                "x_final": posiciones["x_final"], 
                "y_final": posiciones["y_final"],  
            })


n, palabras, nombre = pedir_datos_tablero()
tablero, palabras_sol = generar_tablero(n, palabras)
escribir_juego(tablero, palabras_sol, nombre)
