class FiguraGeometrica:
    """Clase base que representa una figura con dimensiones."""

    def __init__(self, alto, ancho):
        # El uso de los nombres de las propiedades (sin guion) en el init
        # dispara automáticamente las validaciones de los setters.
        self.alto = alto
        self.ancho = ancho

    @property
    
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, valor):
        if valor > 0:
            self._alto = valor
        else:
            raise ValueError("El alto debe ser mayor que 0.")

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, valor):
        if valor > 0:
            self._ancho = valor
        else:
            raise ValueError("El ancho debe ser mayor que 0.")

    def area(self):
        """Calcula el área de la figura."""
        return self._alto * self._ancho

    def perimetro(self):
        """Método base (sin implementación según requerimiento)."""
        pass

    def __str__(self):
        return f"FiguraGeometrica [Alto: {self._alto}, Ancho: {self._ancho}]"