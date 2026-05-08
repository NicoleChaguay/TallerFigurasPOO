from rectangulo import Rectangulo
from cuadrado import Cuadrado
from datetime import datetime


def sumar_areas(figuras):
    """Suma las áreas de una lista de figuras geométricas."""
    total = 0
    for figura in figuras:
        total += figura.area()
    return total


def sumar_perimetros(figuras):
    """Suma los perímetros de una lista de figuras geométricas."""
    total = 0
    for figura in figuras:
        total += figura.perimetro()
    return total


if __name__ == "__main__":
    # 1. Crear objetos
    c1 = Cuadrado(5)
    c2 = Cuadrado(10)
    r1 = Rectangulo(4, 8)
    r2 = Rectangulo(2, 6)

    figuras = [c1, c2, r1, r2]

    print("--- LISTA DE FIGURAS ---")
    for f in figuras:
        print(f"{f} | Área: {f.area()} | Perímetro: {f.perimetro()}")

    # 2. Cálculos totales
    print(f"\nSuma total de áreas: {sumar_areas(figuras)}")
    print(f"Suma total de perímetros: {sumar_perimetros(figuras)}")

    # 3. Demostración de modificación y encapsulamiento
    print("\n--- MODIFICACIÓN DE VALORES ---")
    print(f"Rectángulo inicial: {r1}")
    r1.alto = 10
    r1.ancho = 20
    print(f"Rectángulo modificado: {r1}")

    # 4. Demostración de validación de errores
    print("\n--- PRUEBA DE VALIDACIÓN (ERROR) ---")
    try:
        print("Intentando asignar ancho = 0 a un cuadrado...")
        c1.ancho = 0
    except ValueError as e:
        print(f"ERROR CAPTURADO: {e}")

    try:
        print("Intentando crear rectángulo con alto negativo (-5)...")
        r_error = Rectangulo(-5, 10)
    except ValueError as e:
        print(f"ERROR CAPTURADO: {e}")

    # Fecha y hora de ejecución
    print("\n" + "="*40)
    print("Fecha y hora de ejecución:", datetime.now())
    print("="*40)