# 🧑‍💻 Gestor de Tareas en Consola (Python)

## 📌 Descripción
Este proyecto consiste en el desarrollo de un gestor de tareas (To-Do List) en consola utilizando Python.

Permite administrar tareas mediante operaciones fundamentales como crear, visualizar, completar, eliminar, filtrar y editar tareas, incorporando persistencia de datos mediante archivos JSON.

---

## 🎯 Objetivo
Aplicar los conocimientos básicos de Python para construir una aplicación funcional que permita:

- Crear tareas
- Visualizar tareas
- Marcar tareas como completadas
- Editar tareas
- Eliminar tareas
- Filtrar tareas por estado
- Guardar información de manera persistente

---

## ⚙️ Funcionalidades

### ➕ Crear tarea
- Solicita título y descripción
- Genera un ID único automático
- Asigna estado inicial: **Pendiente**
- Registra la tarea en el sistema

### 📋 Mostrar tareas
- Lista todas las tareas registradas
- Muestra:
  - ID
  - Título
  - Descripción
  - Estado (Pendiente / Completada)
  - Fecha de creación (opcional)

### ✅ Marcar tarea como completada
- Permite seleccionar una tarea por su ID
- Cambia su estado a **Completada**

### ✏️ Editar tarea
- Permite seleccionar una tarea por su ID
- Modificar título, descripción o estado
- Incluye validación de datos

### ❌ Eliminar tarea
- Permite seleccionar una tarea por su ID
- Solicita confirmación antes de eliminar
- Elimina la tarea del sistema

### 🔍 Filtrar tareas
- Mostrar solo tareas **Pendientes**
- Mostrar solo tareas **Completadas**

### 🚪 Salir
- Finaliza la ejecución del programa
- Guarda automáticamente los datos en archivo JSON

---

## 🧠 Estructura del programa

El sistema incluye:

- Menú interactivo en consola
- Uso de listas para almacenar tareas
- Uso de diccionarios para representar cada tarea
- Persistencia de datos mediante archivos JSON
- Separación en módulos para mejor organización
- Funciones independientes para cada operación

---

## 🛠️ Tecnologías utilizadas

- Python 3
- JSON (para almacenamiento de datos)

---

## 📚 Conceptos aplicados

- Variables  
- Listas  
- Diccionarios  
- Funciones (`def`)  
- Condicionales (`if`, `elif`, `else`)  
- Ciclos (`while`, `for`)  
- Manejo de archivos (`json`)  
- Validación de datos  
- Modularización del código  

---

## 📂 Estructura del proyecto
ToDoList-py/  
├── main.py → Menú principal del sistema  
├── funciones.py → Lógica del programa (crear, mostrar, marcar completada, editar, eliminar, filtrar)  
├── data.json → Almacenamiento de tareas  
└── README.md → Documentación del proyecto  

---

## 🚀 Cómo ejecutar

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/owen-rodriguez-rojas/ToDoList-py

2. Entrar al proyecto:
    cd ToDoList-py

3. Ejecutar el programa:
    python main.py

---

## 🎓 Aprendizajes

Durante este proyecto se desarrollaron habilidades como:

- Lógica de programación aplicada
- Manejo de estructuras de datos
- Persistencia de información con JSON
- Validación de entradas del usuario
- Organización modular del código
- Desarrollo de aplicaciones interactivas en consola

---

## 🚀 Próximas mejoras
- Agregar prioridad a tareas (Alta, Media, Baja)
- Implementar edición de tareas completa
- Agregar fechas con datetime
- Búsqueda de tareas por texto
- Interfaz gráfica (Tkinter)
- Versión web (Flask o FastAPI)

---

## 🧑‍💻 Autor
- Owen Rojas
