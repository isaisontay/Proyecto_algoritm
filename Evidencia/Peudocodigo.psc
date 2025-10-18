Proceso Gestor_de_Notas

    Definir opcion Como Entero
	
    Mientras Verdadero Hacer

        Escribir "====== Gestor de Notas Academicas ======"
        Escribir "1. Registrar nuevo curso"
        Escribir "2. Mostrar todos los cursos y notas"
        Escribir "3. Calcular promedio general"
        Escribir "4. Contar cursos aprobados y reprobados"
        Escribir "5. Buscar curso por nombre (busqueda lineal)"
        Escribir "6. Actualizar nota de un curso"
        Escribir "7. Eliminar un curso"
        Escribir "8. Ordenar cursos por nota (burbuja)"
        Escribir "9. Ordenar cursos por nombre (insercion)"
        Escribir "10. Buscar curso por nombre (busqueda binaria)"
        Escribir "11. Simular cola de solicitudes de revision"
        Escribir "12. Mostrar historial de cambios (pila)"
        Escribir "13. Salir"
        Escribir ""
        Escribir "Seleccione una opcion:"
        Leer opcion
		
        Segun opcion Hacer
            1:
                Escribir "Registrando nuevo curso..."
            2:
                Escribir "Mostrando todos los cursos..."
            3:
                Escribir "Calculando promedio general..."
            4:
                Escribir "Contando cursos aprobados y reprobados..."
            5:
                Escribir "Buscando curso por nombre..."
            6:
                Escribir "Actualizando nota de un curso..."
            7:
                Escribir "Eliminando curso..."
            8:
                Escribir "Ordenando cursos por nota..."
            9:
                Escribir "Ordenando cursos por nombre..."
            10:
                Escribir "Buscando curso por nombre (busqueda binaria)..."
            11:
                Escribir "Simulando cola de revision..."
            12:
                Escribir "Mostrando historial de cambios..."
            13:
                Escribir "Gracias por usar el Gestor de Notas Academicas."
                
            DeOtroModo:
                Escribir "Opcion no valida, intente de nuevo."
        FinSegun
		
        Escribir ""
    FinMientras
FinProceso

