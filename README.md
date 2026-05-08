**Estudiante:** Nicole Samara Chaguay Alejandro.
**Curso:** GIG-S-NO-3-4
**Materia:** Programación Orientada a Objetos. 
**Docente:** Jose Cordova Aragundi.

# Taller POO

# Taller de Polimorfismo: Figuras Geométricas

Este proyecto implementa un sistema para gestionar figuras geométricas (Cuadrados y Rectángulos) aplicando los pilares de la Programación Orientada a Objetos en Python. Se enfoca en el control estricto de datos mediante propiedades y la reutilización de código a través de la herencia.

## Clases Implementadas.
- **FiguraGeometrica**: Clase base que encapsula "alto" y "ancho". Incluye validaciones para asegurar que las dimensiones sean siempre positivas.
- **Cuadrado**: Especialización de la base que obliga a que ambos lados sean iguales desde el constructor. Sobrescribe el cálculo de perímetro.
- **Rectangulo**: Extensión de la base para figuras con lados potencialmente desiguales. Sobrescribe el cálculo de perímetro.

## Conceptos de POO Aplicados
1. **Encapsulamiento**: Uso de "_atributo" privado y decoradores "@property".
2. **Herencia**: Las subclases heredan la lógica de validación y el cálculo de área.
3. **Polimorfismo**: Las funciones "sumar_areas" y "sumar_perimetros" procesan cualquier objeto derivado de la base sin importar su tipo específico.

## Evidencia de Ejecución
*(Aquí deberás adjuntar la captura de pantalla de tu terminal ejecutando main.py)*

**Puntos clave visibles en la consola:**
- Cálculo correcto de áreas y perímetros.
- Mensajes de error cuando se ingresan valores inválidos (<= 0).
- Fecha y hora del sistema al momento de la ejecución.



