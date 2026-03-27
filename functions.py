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
    pass

def eliminar_tarea(tareas):
    pass

def filtrar_tareas(tareas):
    pass

def editar_tarea(tareas):
    pass



