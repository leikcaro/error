from error import DimensionError

class Foto:
    MAX = 8000  # Máximo valor permitido para dimensiones

    def __init__(self, ancho, alto):
        self.__ancho = ancho
        self.__alto = alto

    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self, valor):
        if valor < 1 or valor > Foto.MAX:
            raise DimensionError("Valor fuera de rango", 'ancho', Foto.MAX)
        self.__ancho = valor  # Asigna el valor al atributo privado

    @property
    def alto(self):
        return self.__alto  # Corrige el getter para devolver el atributo correcto

    @alto.setter9
    def alto(self, valor):
        if valor < 1 or valor > Foto.MAX:
            raise DimensionError("Valor fuera de rango", 'alto', Foto.MAX)
        self.__alto = valor  # Asigna el valor al atributo privado

# Ejemplo de uso:
if __name__ == "__main__":
    try:
        foto = Foto(1024, 768)
        f_ancho = input("Ingrese el valor de dimension: ")
        foto.ancho = int(f_ancho)  
    except DimensionError as e:
        print(e)
