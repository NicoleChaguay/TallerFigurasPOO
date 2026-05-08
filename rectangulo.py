from figura_geometrica import FiguraGeometrica


class Rectangulo(FiguraGeometrica):
    """Clase que representa un rectángulo, hereda de FiguraGeometrica."""

    def __init__(self, alto, ancho):
        super().__init__(alto, ancho)

    def perimetro(self):
        return (2 * self.alto) + (2 * self.ancho)

    def __str__(self):
        return f"Rectangulo [Alto: {self.alto}, Ancho: {self.ancho}]"