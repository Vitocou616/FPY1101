#Crear agenda que encierre datos en una lista:
#Estructura:

agenda_personas = []

cantidad_usuario = 4
cont = 0

while cont < cantidad_usuario:

    cont += 1
    #Pedir datos
    nombre = input("Ingrese su nombre: ")
    telefono = input("Ingrese su nombre: ")
    email = input("Ingrese su nombre: ")
    direccion = input("Ingrese su nombre: ")
    try:
        estado = bool(input("Estado usuario (Habilitado = 1 / Inhabilitado = 0): "))
    except ValueError:
        print("El valor para el estado debe ser 1 o 0.")

    datos_persona = { nombre : {
        "telefono": telefono,
        "email": email,
        "direccion": direccion,
        "estado": estado
    }}