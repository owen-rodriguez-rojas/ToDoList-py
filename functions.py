import json



def cargar_datos():
    try:
        with open("data.json", "r") as archivo: #Abre archivo en modo lectura
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    

def guardar_datos(tareas):
        with open("data.json", "w")as archivo: #Abre archivo en modo escritura
            json.dump(tareas, archivo, indent=4)



def crear_tarea(tareas):
    seguir = "s"
    while seguir != "n":
        titulo = input("Titulo de la tarea: ").strip()
        while titulo == "":
            print("Titulo no valido, intente nuevamente...")
            titulo = input("Titulo de la tarea: ").strip()
    
        descripcion = input("Descripcion de la tarea: ").strip()
        while descripcion == "":
            print("Descripción Invalida...")    
            descripcion = input("Descripcion de la tarea: ").strip()
        
        if not tareas:
            last_id = 1
        else:
            ultima_tarea = tareas[-1]
            last_id = ultima_tarea["id"] + 1
            
        datos = {
            "id": last_id,
            "titulo": titulo,
            "descripcion": descripcion,
            "estado": "Pendiente"
        }
        tareas.append(datos)
        print(f"Tarea {last_id} {titulo} Agregada Exitosamente")
        
        validacion_seguir = input("¿Desea agregar otra tarea? (s/n): ").strip().lower()
        while validacion_seguir not in ("s", "n"):
            print("Valor incorrecto...")
            validacion_seguir = input("¿Desea agregar otra tarea? (s/n): ").strip().lower()
        seguir = validacion_seguir
       
        
        

def mostrar_tarea(tareas):
    if len(tareas) == 0:
        print("No hay tareas registradas")
    else:
        for i in tareas:
            print(f"{i['id']} | {i['titulo']} | {i['descripcion']} | {i['estado']}")

def marcar_completada(tareas):
    if len(tareas) == 0:
        print("No hay tareas registradas")
        return

    tareas_pendientes = "Pendiente"
    tareas_completadas = "Completada"

    
    if not any(i["estado"] == tareas_pendientes for i in tareas):
        print("No hay tareas pendientes.")
        return
    

    #Alternativa usando all():
    # Verifica si todas las tareas están completadas
    
    """
    if all(i["estado"] == tareas_completadas for i in tareas):
        print("No hay tareas pendientes.")
        return
    """
    
    id_encontrado = False

    while not id_encontrado:

        for i in tareas:
            if i["estado"] == tareas_pendientes:
                print(f"{i['id']} | {i['titulo']} | {i['estado']}")

        id_select = input("Digita el ID de la tarea completada: ").strip()

        while not id_select.isdigit():
            print("ID invalido, intente nuevamente...")
            id_select = input("Digita el ID de la tarea completada: ").strip()

        id_select = int(id_select)

        for i in tareas:
            if i["id"] == id_select:
                if i["estado"] == tareas_pendientes:
                    i["estado"] = tareas_completadas
                    print(f"El estado de la tarea {i['id']} {i['titulo']} cambió a {i['estado']}")
                    mostrar_tarea(tareas)
                    id_encontrado = True
                else:
                    print("Esa tarea ya está completada!")
                    id_encontrado = True
                break

        if not id_encontrado:
            print("ID no encontrado, intentar nuevamente...")
            
                
            
        
def editar_tarea(tareas):
    pass        

def eliminar_tarea(tareas):
    pass

def filtrar_tareas(tareas):
    pass

