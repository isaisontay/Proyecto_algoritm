# Proyecto-Algoritmos
Gestor de notas academicas
El Gestor de Notas Académicas es un sistema diseñado para registrar, organizar y consultar las calificaciones de distintos cursos de manera sencilla. Su objetivo principal es ofrecer una herramienta práctica que permita almacenar la información académica sin necesidad de sistemas complejos, ni bases de datos externas utilizando únicamente un menú interactivo en consola.

Este sistema está dirigido principalmente a estudiantes y docentes que necesiten llevar un control básico de las calificaciones, ya sea para uso personal o como parte de una actividad académica. También resulta útil para quienes están aprendiendo lógica de programación y desean aplicar estructuras de control como bucles y condicionales en un contexto realista.

Con este gestor, los usuarios pueden cubrir necesidades esenciales como registrar nuevas notas, visualizar todas las calificaciones, calcular promedios y buscar información específica de un curso.

=== Requisitos ===
Funcionales

Registrar un nuevo curso y su nota para almacenarlo en la lista del sistema.
Mostrar todas las notas registradas junto con el nombre del curso correspondiente.
Calcular el promedio general de todas las notas almacenadas.
Buscar y mostrar la nota de un curso específico.
Salir del sistema de manera segura cuando el usuario lo indique.
No funcionales

Sin librerias externas
Uso de bucles
El diseño inicial estará escrito en pseudocódigo.
No depende de una red de internet
Pseudocodigo
Diseño del menu

INICIO

MIENTRAS VERDADERO HACER

    IMPRIMIR "------ MENÚ PRINCIPAL ------"
    IMPRIMIR "1. Registrar nuevo curso y nota"
    IMPRIMIR "2. Mostrar todas las notas"
    IMPRIMIR "3. Calcular promedio general"
    IMPRIMIR "4. Buscar nota por curso"
    IMPRIMIR "5. Salir"
    IMPRIMIR "Seleccione una opción:"
    LEER opcion
    SI opcion = 1 ENTONCES
        <registrar curso y nota>
    SINO SI opcion = 2 ENTONCES
        <mostrar todas las notas>
    SINO SI opcion = 3 ENTONCES
        <calcular promedio>
    SINO SI opcion = 4 ENTONCES
        <buscar nota por curso>
    SINO SI opcion = 5 ENTONCES
        IMPRIMIR "Saliendo del sistema..."
        SALIR
    SINO
        IMPRIMIR "Opción no válida. Intente de nuevo."
    FIN_SI
FIN_MIENTRAS
FIN

¿Qué aprendí con este proyecto?

Aprendí a estructurar un programa completo en Python utilizando listas, funciones y estructuras de control. También comprendí cómo aplicar algoritmos de ordenamiento (burbuja e inserción) y búsqueda (lineal y binaria) en un caso práctico. Además, mejoré mi capacidad para organizar el código y hacerlo más modular y legible.

¿Qué fue lo más desafiante de resolver?

Lo más desafiante fue implementar las funciones de ordenamiento y búsqueda de manera correcta, ya que requerían entender bien la lógica de comparación y el manejo de índices en las listas. También resultó un reto lograr que el programa validara correctamente los datos ingresados por el usuario sin causar errores.

¿Qué mejoraría si tuviera más tiempo?

Si tuviera más tiempo, mejoraría la interfaz del programa para que fuera más interactiva y amigable, quizás usando una interfaz gráfica. También agregaría la posibilidad de guardar y cargar los cursos desde un archivo externo, de modo que la información no se pierda al cerrar el programa.


