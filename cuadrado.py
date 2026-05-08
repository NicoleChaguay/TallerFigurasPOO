from figura_geometrica import FiguraGeometrica




class Cuadrado(FiguraGeometrica):
    """Clase que representa un cuadrado, hereda de FiguraGeometrica."""

    def __init__(self, lado):
        # Pasa el mismo valor a alto y ancho usando el constructor base
        super().__init__(lado, lado)

    def area(self):
        return super().area()

    def perimetro(self):
        return 4 * self.alto

    def __str__(self):
        return f"Cuadrado [Lado: {self.alto}]"