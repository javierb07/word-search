def main():
    datos = Obetener_Datos()
    n, palabras, nombre = datos.obtener_datos_tablero()
    tablero = Generador_Tablero(n, palabras)
    tablero, solucion = tablero.generar(n, palabras)
    escritor = Escritor(nombre, tablero, solucion)
    escritor.escribir_tablero()
    escritor.escribir_solucion()
    print(f"Archivos {nombre}.csv y {nombre}_solucion.csv generados exitosamente.")


class Obetener_Datos():
    def obtener_datos_usuario(self, texto, validar):
        dato = input(texto)
        while not validar(dato):
            dato = input(f"Error. {texto}") 
        return dato 
    
    def obtener_datos_tablero(self):
        n = int(self.obtener_datos_usuario("Ingrese la cantidad de columnas y filas. Debe ser mayor o igual a 15: ", lambda n : int(n) >= 15))    
        palabras = []
        cantidad = n//3
        for i in range(cantidad):
            palabra = self.obtener_datos_usuario("Ingrese una palabra o escriba fin para terminar: ", lambda palabra: len(palabra) <= n)
            if palabra.lower() == "fin":
                break
            palabras.append(palabra.lower())
        nombre = input("Ingrese el nombre del archivo donde se guardará el tablero: ")
        while len(nombre) > 30:
            nombre = input("El nombre no puede tener más de 30 caracteres. Ingrese nuevamente: ")
        return (n, palabras, nombre)


class Escritor:
    def __init__(self, nombre, tablero, solucion):
        self.nombre = nombre
        self.tablero = tablero
        self.solucion = solucion

    def escribir_tablero(self):
        from csv import writer
        with open(f"{self.nombre}.csv", "w", newline='\n', encoding='utf-8') as archivo:
                escritor = writer(archivo)
                for fila in self.tablero:
                    escritor.writerow(fila)

    def escribir_solucion(self):
        from csv import DictWriter
        with open(f"{self.nombre}_solucion.csv", "w", newline='\n', encoding='utf-8') as archivo:
            titulos = ["palabra", "x_inicial", "y_inicial", "x_final", "y_final"]
            escritor = DictWriter(archivo, fieldnames=titulos)
            escritor.writeheader()
            for palabra, posiciones in self.solucion.items():
                escritor.writerow({
                    "palabra": palabra, 
                    "x_inicial": posiciones["x_inicial"], 
                    "y_inicial": posiciones["y_inicial"],
                    "x_final": posiciones["x_final"], 
                    "y_final": posiciones["y_final"],  
                })


class Generador_Tablero():
    def __init__(self, n, palabras):
        self.n = n
        self.palabras = palabras
    def validar_posicion(self, palabra, seccion):
        for i, letra in enumerate(seccion):
            if (letra == "" or letra == palabra[i]):
                continue
            else:
                return False
        return True

    def insertar_palabra(self, direccion, sentido, palabra, tablero):
        from random import randint
        if direccion == 0: # horizontal
            fila = randint(0,len(tablero)-1)
            posicion = randint(0, len(tablero)-len(palabra))
            seccion = tablero[fila][posicion:len(palabra)+posicion]
            if sentido == 0: # izq -> der
                while not self.validar_posicion(palabra, seccion):
                    fila = randint(0,len(tablero)-1)
                    posicion = randint(0, len(tablero)-len(palabra))
                    seccion = tablero[fila][posicion:len(palabra)+posicion]
                tablero[fila][posicion:len(palabra)+posicion] = list(palabra)
                palabra_sol = [palabra,posicion,fila,len(palabra)+posicion-1,fila]
            else: # der -> izq
                while not self.validar_posicion(palabra[::-1], seccion):
                    fila = randint(0,len(tablero)-1)
                    posicion = randint(0, len(tablero)-len(palabra))
                    seccion = tablero[fila][posicion:len(palabra)+posicion]
                tablero[fila][posicion:len(palabra)+posicion] = list(palabra)[::-1]
                palabra_sol = [palabra,len(palabra)+posicion-1,fila,posicion,fila]
        else: # vertical
            columna = randint(0,len(tablero)-1)
            posicion = randint(0, len(tablero)-len(palabra))
            seccion =  [fila[columna] for fila in tablero][posicion:len(palabra)+posicion]
            if sentido == 0: # arriba -> abajo
                while not self.validar_posicion(palabra, seccion):
                    columna = randint(0,len(tablero)-1)
                    posicion = randint(0, len(tablero)-len(palabra))
                    seccion =  [col[columna] for col in tablero][posicion:len(palabra)+posicion]
                for j in range(posicion, posicion+len(palabra)):
                    tablero[j][columna] = palabra[j-posicion]
                palabra_sol = [palabra,columna,posicion,columna,posicion+len(palabra)-1]
            else: # abajo -> arriba
                while not self.validar_posicion(palabra[::-1], seccion):
                    columna = randint(0,len(tablero)-1)
                    posicion = randint(0, len(tablero)-len(palabra))
                    seccion =  [col[columna] for col in tablero][posicion:len(palabra)+posicion]
                for j in range(posicion, posicion + len(palabra)):
                    tablero[j][columna] = palabra[::-1][j-posicion]
                palabra_sol = [palabra,columna,posicion+len(palabra)-1,columna,posicion]   
        return [tablero, palabra_sol]

    def generar(self, n, palabras):
        from random import randint, choice
        tablero = [["" for x in range(n)] for y in range(n)]
        solucion = {} 
        palabras.sort(key = len, reverse = True)
        for palabra in palabras:
            direccion = randint(0,1) # 0 horizontal 1 vertical
            sentido = randint(0,1) # 0 izq -> der 1 der -> izq o 0 arriba -> abajo 1 abajo -> arriba
            try:
                tablero, palabra_sol = self.insertar_palabra(direccion, sentido, palabra, tablero)
            except Exception:
                main()
            solucion[palabra_sol[0]] = {"x_inicial": palabra_sol[1], "y_inicial": palabra_sol[2], "x_final": palabra_sol[3], "y_final": palabra_sol[4]}
        for i in range(n):
            for j in range(n):
                if tablero[i][j] == "":
                    tablero[i][j] = choice("abcdefghijklmnopqrstuvwxyz")
        return [tablero, solucion]


if __name__ == "__main__":
    main()