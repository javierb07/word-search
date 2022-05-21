def main():
    datos = Obetener_Datos()
    usuario, tablero = datos.obtener_datos_del_usuario()
    juego = Juego(usuario, tablero)
    juego.agregar_jugador()   
    juego.tablero.visualizar_tablero()
    juego.jugar()


class Obetener_Datos():
    def validar_datos(self, texto, validar):
        dato = input(texto)
        while not validar(dato):
            dato = input(f"Error. {texto}") 
        return dato 
    
    def verificar_tablero(self, nombre):
        from csv import reader
        try:
            with open(nombre, 'r') as f:
                lector = reader(f)
            return True
        except IOError:
            return False
    
    def obtener_datos_del_usuario(self):
        usuario = self.validar_datos("Ingrese su nombre. Longitud máxima de caracteres 40: ", lambda n : len(n) <= 40) 
        tablero = self.validar_datos("Ingrese el nombre del tablero a utilizar: ", self.verificar_tablero)
        return usuario, tablero


class Juego():
    def __init__(self, nombre_usuario, nombre_tablero):
        self.nombre_usuario = nombre_usuario
        self.nombre_tablero = nombre_tablero
        self.tablero = Tablero(nombre_tablero)
        self.terminado = False
        self.palabra = ""

    def agregar_jugador(self):
        self.jugador = Jugador(self.nombre_usuario)
    
    def encontrar_palabra(self):
        if not self.tablero.solucion:
            self.terminado = True
        else:
            self.palabra = input("Ingrese una palabra o escriba fin para terminar: ")
            if self.palabra.lower() == "fin":
                self.terminado = True
            elif self.tablero.encontrar_palabra(self.palabra):
                self.jugador.sumar_punto()
    
    def jugar(self):
        while not self.terminado:
            self.encontrar_palabra()
            self.tablero.visualizar_tablero()
        self.jugador.imprimir_puntaje()
        self.tablero.imprimir_palabras()


class Tablero():
    def __init__(self, nombre):
        self.tablero = self.cargar_tablero(nombre)
        self.solucion = self.cargar_solucion(nombre)
        self.palabras = []

    def cargar_tablero(self, nombre):
        from csv import reader
        tablero = []
        with open(nombre, 'r') as f:
            lector = reader(f)
            for fila in lector:
                tablero.append(fila) 
        return tablero

    def cargar_solucion(self, nombre):
        from csv import DictReader
        solucion = nombre.replace(".csv", "_solucion.csv")
        file = open(solucion, "r")
        lector = DictReader(file)
        solucion = {}
        for fila in lector:
            solucion[fila["palabra"]] =  {             
                "x_inicial": fila["x_inicial"], 
                "y_inicial": fila["y_inicial"],
                "x_final": fila["x_final"], 
                "y_final": fila["y_final"],
                }     
        return solucion

    def visualizar_tablero(self):
        separador = " | "
        for fila in self.tablero:
            print(separador.join(map(str,fila)))

    def encontrar_palabra(self, palabra):
        if palabra not in self.solucion:
            print(f"{palabra} no está en la sopa de letras.")
            return False
        else:
            datos_palabra = self.solucion[palabra]
            x_inicial = int(datos_palabra["x_inicial"])
            x_final = int(datos_palabra["x_final"])
            y_inicial = int(datos_palabra["y_inicial"])
            y_final = int(datos_palabra["y_final"])
            self.solucion.pop(palabra, None)
            # Palabra horizontal
            if y_inicial == y_final:
                for i in range(min(x_inicial, x_final), max(x_inicial, x_final)+1):
                    self.tablero[y_inicial][i] = self.tablero[y_inicial][i].upper()
            # Palabra vertical
            else:
                for j in range(min(y_inicial, y_final), max(y_inicial, y_final)+1):
                    self.tablero[j][x_inicial] =  self.tablero[j][x_inicial].upper()
            self.palabras.append(palabra)
            return True

    def imprimir_palabras(self):
        no_encontradas = sorted(list(self.solucion.keys()))
        print("Encontró las siguientes palabras: ")
        for i, palabra in enumerate(self.palabras):
            print(f"{i+1}: {palabra}")
        if len(no_encontradas) > 0:
            print("No encontró las siguientes palabras: ")
            for i, palabra in enumerate(no_encontradas):
                print(f"{i+1}: {palabra}")


class Jugador():
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntaje = 0

    def sumar_punto(self):
        self.puntaje += 1

    def imprimir_puntaje(self):
        print(f"El jugador {self.nombre} tiene {self.puntaje} puntos.")
        

if __name__ == "__main__":
    main()