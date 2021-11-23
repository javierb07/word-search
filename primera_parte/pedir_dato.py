# Tiene como objetivo pedir un dato al usuario, validarlo y retornarlo
# Esta función debería recibir como parámetro un texto y una función de validación
# (que retorna True si el dato es válido y False en caso contrario) y retorna el dato ingresado por el usuario.
# Debe pedir al usuario que ingrese el dato mostrando el texto, 
# en caso de que el dato ingresado no pase la validación, deberá pedir el dato nuevamente.

def pedir_dato(texto, validar):
    dato = input(texto)
    while not validar(dato):
        dato = input(f"Error. {texto}") 
    return dato


#print(pedir_dato("Ingrese un número mayor a 10: ", lambda n : int(n) > 10))
