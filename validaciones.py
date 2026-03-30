#Refactorizacion

def insert_text(mensaje):
    valor = input(mensaje).strip()
    while valor == "":
        print("Caracteres incorrectos, intente nuevamente...")
        valor = input(mensaje).strip()
    return valor

def insert_id_or_num(mensaje):
    valor = input(mensaje).strip()
    while not valor.isdigit():
        print("Valor invalido, intente nuevamente...")
        valor = input(mensaje).strip()

    return int(valor)

def confirmacion(mensaje):
    valor = input(mensaje).strip().lower()
    while valor not in ("s", "n"):
        print("Valor incorrecto, escribe s o n.")
        valor = input(mensaje).strip().lower()
    return valor
