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
            nombre_real = cursos[i][0]
            cursos.pop(i)
            historial.append(f"Eliminado {nombre_real}")
            print(f"Curso '{nombre_real}' eliminado\n")
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
        for j in range(0, n - i - 1):
            if cursos[j][1] > cursos[j + 1][1]:
                cursos[j], cursos[j + 1] = cursos[j + 1], cursos[j]
    print("Cursos ordenados por nota (burbuja):")
    ver_cursos()

def ordenar_insercion_por_nombre():
    for i in range(1, len(cursos)):
        key = cursos[i]
        j = i - 1
        while j >= 0 and key[0].lower() < cursos[j][0].lower():
            cursos[j + 1] = cursos[j]
            j -= 1
        cursos[j + 1] = key
    print("Cursos ordenados por nombre (inserción):")
    ver_cursos()

def contar_aprobados_reprobados():
    if len(cursos) == 0:
        print("No tienes cursos registrados\n")
        return
    aprobados = sum(1 for c in cursos if c[1] >= 60)
    reprobados = len(cursos) - aprobados
    print(f"Aprobados: {aprobados}")
    print(f"Reprobados: {reprobados}\n")

def actualizar_nota():
    if len(cursos) == 0:
        print("No hay cursos para actualizar\n")
        return
    nombre = input("Nombre del curso a actualizar: ")
    for i in range(len(cursos)):
        if cursos[i][0].lower() == nombre.lower():
            try:
                nueva_nota = float(input(f"Nueva nota para '{cursos[i][0]}' (0 a 100): "))
                if nueva_nota < 0 or nueva_nota > 100:
                    print("¡La nota debe estar entre 0 y 100!\n")
                    return
            except:
                print("¡Eso no es un número!\n")
                return
            nota_antigua = cursos[i][1]
            cursos[i][1] = nueva_nota
            historial.append(f"Actualizado {cursos[i][0]} de {nota_antigua} a {nueva_nota}")
            print(f"Nota actualizada: {cursos[i][0]} de {nota_antigua} a {nueva_nota}\n")
            return
    print("No se encontró ese curso\n")

def busqueda_binaria_nombre():
    if len(cursos) == 0:
        print("No tienes cursos para buscar\n")
        return
    ordenar_insercion_por_nombre()
    objetivo = input("Nombre del curso a buscar (búsqueda binaria): ").lower()
    low = 0
    high = len(cursos) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_name = cursos[mid][0].lower()
        if mid_name == objetivo:
            print(f"Encontrado: {cursos[mid][0]} - Nota: {cursos[mid][1]}\n")
            return
        elif mid_name < objetivo:
            low = mid + 1
        else:
            high = mid - 1
    print("No se encontró ese curso\n")

while True:
    print("================================")
    print("===== Gestor de notas académicas =====")
    print("1. Registrar nuevo curso")
    print("2. Mostrar todos los cursos y notas")
    print("3. Calcular promedio general")
    print("4. Contar cursos aprobados y reprobados")
    print("5. Buscar curso por nombre (búsqueda lineal)")
    print("6. Actualizar nota de un curso")
    print("7. Eliminar un curso")
    print("8. Ordenar cursos por nota (burbuja)")
    print("9. Ordenar cursos por nombre (inserción)")
    print("10. Buscar curso por nombre (búsqueda binaria)")
    print("11. Simular cola de revisión")
    print("12. Mostrar historial de cambios")
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
        contar_aprobados_reprobados()
    elif opcion == "5":
        buscar_curso()
    elif opcion == "6":
        actualizar_nota()
    elif opcion == "7":
        eliminar_curso()
    elif opcion == "8":
        ordenar_burbuja()
    elif opcion == "9":
        ordenar_insercion_por_nombre()
    elif opcion == "10":
        busqueda_binaria_nombre()
    elif opcion == "11":
        revisar_cola()
    elif opcion == "12":
        ver_historial()
    elif opcion == "13":
        print("Adiós\n")
        break
    else:
        print("Opción no válida\n")
