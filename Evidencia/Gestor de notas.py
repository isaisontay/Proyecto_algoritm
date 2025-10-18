cursos = []
historial = []
cola = []

def agregar_curso():
    nombre = input("Nombre del curso: ")
    if nombre == "":
        print("¡Debes escribir un nombre!\n")
        return
    try:
        nota = float(input("Nota (0 a 100): "))
        if nota < 0 or nota > 100:
            print("¡La nota debe estar entre 0 y 100!\n")
            return
    except:
        print("¡Eso no es un número!\n")
        return
    cursos.append([nombre, nota])
    historial.append(f"Agregado {nombre}")
    cola.append(nombre)
    print(f"Curso '{nombre}' guardado con nota {nota}\n")

def ver_cursos():
    if len(cursos) == 0:
        print("No tienes cursos todavía\n")
    else:
        for i in range(len(cursos)):
            print(f"{i+1}. {cursos[i][0]}: {cursos[i][1]}")
    print()

def calcular_promedio():
    if len(cursos) == 0:
        print("No tienes cursos para calcular promedio\n")
    else:
        total = 0
        for curso in cursos:
            total += curso[1]
        promedio = total / len(cursos)
        print(f"Tu promedio es: {promedio:.1f}\n")

def buscar_curso():
    if len(cursos) == 0:
        print("No tienes cursos para buscar\n")
        return
    buscar = input("Nombre del curso a buscar: ")
    for curso in cursos:
        if curso[0].lower() == buscar.lower():
            print(f"Encontrado: {curso[0]} - Nota: {curso[1]}\n")
            return
    print("No se encontró ese curso\n")

def eliminar_curso():
    if len(cursos) == 0:
        print("No hay cursos para eliminar\n")
        return
    eliminar = input("Nombre del curso a eliminar: ")
    for i in range(len(cursos)):
        if cursos[i][0].lower() == eliminar.lower():
            cursos.pop(i)
            historial.append(f"Eliminado {eliminar}")
            print(f"Curso '{eliminar}' eliminado\n")
            return
    print("No se encontró ese curso\n")

def ver_historial():
    if len(historial) == 0:
        print("No hay historial\n")
    else:
        for h in reversed(historial):
            print(h)
    print()

def revisar_cola():
    if len(cola) == 0:
        print("No hay cursos en revisión\n")
    else:
        print(f"Revisando: {cola.pop(0)}\n")

def ordenar_burbuja():
    n = len(cursos)
    for i in range(n):
        for j in range(0, n-i-1):
            if cursos[j][1] > cursos[j+1][1]:
                cursos[j], cursos[j+1] = cursos[j+1], cursos[j]
    print("Cursos ordenados por nota (burbuja)\n")

def ordenar_insercion():
    for i in range(1, len(cursos)):
        key = cursos[i]
        j = i-1
        while j >= 0 and key[1] < cursos[j][1]:
            cursos[j+1] = cursos[j]
            j -= 1
        cursos[j+1] = key
    print("Cursos ordenados por nota (inserción)\n")

# === MENÚ PRINCIPAL ===
while True:
    print("================================")
    print("===== Gestor de notas academicas =====")
    print("1. Registrar nuevo curso")
    print("2. Mostrar todos los cursos y notas")
    print("3. Calcular promedio general")
    print("4. Contar cursos aprobados y reprobados")
    print("5. Buscar curso por nombre (búsqueda lineal)")
    print("6. Actualizar nota de un curso")
    print("7. Eliminar un curso")
    print("8. Ordenar cursos por nota (ordenamiento burbuja)")
    print("9. Ordenar cursos por nombre (ordenamiento inserción)")
    print("10. Buscar curso por nombre (búsqueda binaria)")
    print("11. Simular cola de solicitudes de revisión")
    print("12. Mostrar historial de cambios (pila)")
    print("13. Salir")
    opcion = input("Seleccione una opción: ")
    print()

    if opcion == "1":
        agregar_curso()
    elif opcion == "2":
        ver_cursos()
    elif opcion == "3":
        calcular_promedio()
    elif opcion == "4":
        print("Función aún no implementada.\n")
    elif opcion == "5":
        buscar_curso()
    elif opcion == "6":
        print("Función aún no implementada.\n")
    elif opcion == "7":
        eliminar_curso()
    elif opcion == "8":
        ordenar_burbuja()
    elif opcion == "9":
        ordenar_insercion()
    elif opcion == "10":
        print("Función aún no implementada.\n")
    elif opcion == "11":
        revisar_cola()
    elif opcion == "12":
        ver_historial()
    elif opcion == "13":
        print("Adios\n")
        break
    else:
        print("Opción no válida\n")