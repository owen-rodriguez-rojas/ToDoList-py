import json
from validaciones import insert_text, insert_id_or_num, confirmacion


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
        titulo = insert_text("Titulo de la tarea: ")
    
        descripcion = insert_text("Descripcion de la tarea: ")
        
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
        
        seguir = validacion_seguir = confirmacion("¿Desea agregar otra tarea? (s/n): ")
        
       
        
        

def mostrar_tarea(tareas):
    if not tareas:
        print("No hay tareas registradas")
    else:
        for i in tareas:
            print(f"{i['id']} | {i['titulo']} | {i['descripcion']} | {i['estado']}")

def marcar_completada(tareas):
    if not tareas:
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

        id_select = insert_id_or_num("Digita el ID de la tarea completada :")

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
    if not tareas:
            print("No hay tareas registradas")
            return
        
        
    id_encontrado = False
    
    while not id_encontrado:
        mostrar_tarea(tareas)
        
        id_select = insert_id_or_num("Digita el ID de la tarea a modificar: ")
    
        for i in tareas:
            if i["id"] == id_select:
                id_encontrado = True
                seguir = "s"
                print("Tarea encontrada: \n")
                print(f"{i['id']} | {i['titulo']} | {i['descripcion']} | {i['estado']}")
                
                while seguir != "n":
                    print("1. Titulo\n2. Descripcion\n3. Estado") 
                    
                    modif = insert_id_or_num("¿Qué campo deseas modificar? ")
                    
                    if modif == 1:
                        print(i["titulo"])
                        titulo = insert_text("Inserta el nuevo titulo: ")
                        i["titulo"] = titulo
                        print("Cambio Exitoso")
                    elif modif == 2:
                        print(i["descripcion"])
                        descripcion = insert_text("Inserta la nueva descripcion: ")
                        i["descripcion"] = descripcion
                        print("Cambio Exitoso")
                    elif modif == 3:
                        estado = 0
                        while estado not in (1, 2):
                            print("1. Completada\n2. Pendiente")
                            estado = insert_id_or_num("Ingresa un valor: ")
                            if estado not in (1, 2):
                                print("Numero fuera de rango...")
                        if estado == 1:
                            i["estado"] = "Completada"
                        elif estado == 2:
                            i["estado"] = "Pendiente"
                            
                    else:
                        print("Numero fuera de rango")
                        continue
                    
                    print("¡Cambio Exitoso!\n")
                    print("\nDatos Actualizados: ")
                    print(i["id"], "|", i["titulo"], "|", i["descripcion"], "|", i["estado"])
                    
                    seguir = confirmacion("¿Desea modificar otro campo? (s/n): ")
                    
        if not id_encontrado:
            print("ID no encontrado, internar nuevamente...")
               
            

def eliminar_tarea(tareas):
    if not tareas:
            print("No hay tareas registradas")
            return
    
    seguir = "s"
    while seguir != "n":
        mostrar_tarea(tareas)
        id_select = insert_id_or_num("Inserta el ID de la tarea a eliminar: ")
        
        id_encontrado = False
        for i in tareas:
            if i["id"] == id_select:
                id_encontrado = True
                print("Tarea Encontrada: ")
                print(f"{i['id']} | {i['titulo']} | {i['descripcion']} | {i['estado']}")
                opc = confirmacion("¿Esta seguro que desea eliminar esta tarea? (s/n): ")
                
                if opc == "s":
                    tareas.remove(i)
                    print("Tarea Eliminada con Exito")
                    mostrar_tarea(tareas)
                else:
                    print("Cancelando Eliminacion...")
                    break
        
        if not id_encontrado:
            print("ID no encontrado, intente nuevamente...")
            continue
        
        seguir = confirmacion("¿Desea eliminar otra tarea? (s/n): ")
                    
                                       
    

def filtrar_tareas(tareas):
    if not tareas:
        print("No hay tareas registradas")
        return
    
    print("\n1.Completadas\n2.Pendientes")
    opc = insert_id_or_num("¿Que tareas deseas visualizar?: ")
    
 
    if opc == 1:
        if not any(i["estado"] == "Completada" for i in tareas):
            print("No hay tareas completadas.")
        else: 
            for i in tareas:
                if i["estado"] == "Completada":
                    print(f"{i['id']} | {i['titulo']} | {i['descripcion']} | {i['estado']}")
                        
    elif opc == 2:
        if not any(i["estado"] == "Pendiente" for i in tareas):
            print("No hay tareas pendientes.") 
        else:
            for i in tareas:
                if i["estado"] == "Pendiente":
                    print(f"{i['id']} | {i['titulo']} | {i['descripcion']} | {i['estado']}")
     
    else:
        print("Numero fuera de rango...")
                         