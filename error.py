class DimensionError(Exception):
    def __init__(self, mensaje, dimension=None, maximo=None):
        super().__init__(mensaje)
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self):
        if self.dimension is None or self.maximo is None:
            return super().__str__()
        else:
            return f"{self.mensaje} La dimensión '{self.dimension}' debe estar entre 1 y {self.maximo}."
