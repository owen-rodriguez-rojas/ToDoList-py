from functions import cargar_datos, guardar_datos, crear_tarea, mostrar_tarea, marcar_completada, editar_tarea, eliminar_tarea, filtrar_tareas

tareas = cargar_datos()

while True:
    print("\n- - - MENU - - -")
    print("1. Crear Tarea")
    print("2. Mostrar Tareas")
    print("3. Marcar Completada")
    print("4. Editar Tarea")
    print("5. Eliminar Tarea")
    print("6. Filtrar Tareas")
    print("7. Salir")
    
    opc = input("\nDigite la opción deseada: ")
    while not opc.isdigit() or int(opc) < 1 or int(opc) > 7:
        print("Valor no válido, intente nuevamente.")
        opc = input("\nDigite la opción deseada: ")
    opc = int(opc)
    
    if opc == 1:
        crear_tarea(tareas)
    elif opc == 2:
        mostrar_tarea(tareas)
    elif opc == 3:
        marcar_completada(tareas)
    elif opc == 4:
        editar_tarea(tareas)
    elif opc == 5:
        eliminar_tarea(tareas)
    elif opc == 6:
        filtrar_tareas(tareas)
    elif opc == 7:
        guardar_datos(tareas)  
        print("Guardando datos y cerrando...")
        break