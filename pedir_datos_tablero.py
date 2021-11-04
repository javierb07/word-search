# Tiene como objetivo pedir los datos al usuario para generar un tablero. 
# No recibe parámetros y retorna en un tupla los datos ingresados por el usuario (validados). 
# Los datos a pedir son:
# ● N:  Número entero. 
#       Va a representar la cantidad de columnas y filas de la sopa de letras.
#       Tiene que ser mayor o igual a 15.
# ● Lista de palabras: Se ingresan de a una. 
#       La cantidad de palabras tiene que ser menor a N / 3. 
#       La longitud de la palabra tiene que ser menor a N / 3. 
#       Se termina el ingreso de palabras cuando se haya llegado al límite de palabras o se ingrese la palabra “fin”.
# ● Nombre de archivo: Texto.
#       Va a representar el nombre del archivo donde se guardará el tablero. 
#       El nombre del archivo no puede ser mayor a 30 caracteres.

from pedir_dato import pedir_dato


def pedir_datos_tablero():
    n = int(pedir_dato("Ingrese la cantidad de columnas y filas. Debe ser mayor o igual a 15: ", lambda n : int(n) >= 15))    
    palabras = []
    cantidad = n//3
    for i in range(cantidad):
        palabra = pedir_dato("Ingrese una palabra o escriba fin para terminar: ", lambda palabra: len(palabra) <= n)
        if palabra.lower() == "fin":
            break
        palabras.append(palabra.lower())
    nombre = input("Ingrese el nombre del archivo donde se guardará el tablero: ")
    while len(nombre) > 30:
        nombre = input("El nombre no puede tener más de 30 caracteres. Ingrese nuevamente: ")
    return (n, palabras, nombre)


#n, palabras, nombre = pedir_datos_tablero()
#print(n, palabras, nombre)
