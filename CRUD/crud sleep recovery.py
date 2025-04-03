usuarios = [
    {"idUsuarios": 1, "Nombre": "Juan", "RangoEdad": "Adultos (26-64 años)", "CorreoElectronico": "juan@example.com", "Contrasena": "1234", "NivelActividadFisica": "Moderado", "HoraDormir": "22:00", "HoraDespertar": "06:00"}
]

registros_sueno = [
    {"idRegistrosSueno": 1, "idUsuarios": 1, "TipoSueno": "Dormir", "Hora": 10, "Minutos": 30, "Meridiano": "PM", "FechaRegistro": "2024-09-01", "HoraRegistro": "22:30:00"}
]

preferencias_usuario = [
    {"idPreferenciasUsuario": 1, "Preferencia": "Temperatura Ambiente", "Valor": "Fría", "idUsuarios": 1}
]

recomendaciones = [
    {"idRecomendaciones": 1, "RangoEdad": "Adultos (26-64 años)", "Recomendacion": "Dormir entre 7 y 9 horas"}
]

#funciones CRUD para Usuarios
def mostrar_usuarios():
    for usuario in usuarios:
        print(f"ID Usuario: {usuario['idUsuarios']}")
        print(f"Nombre: {usuario['Nombre']}")
        print(f"Correo: {usuario['CorreoElectronico']}")
        print(f"Rango de Edad: {usuario['RangoEdad']}")
        print(f"Nivel de Actividad Física: {usuario['NivelActividadFisica']}")
        print(f"Hora de Dormir: {usuario['HoraDormir']}")
        print(f"Hora de Despertar: {usuario['HoraDespertar']}")
        print()

def crear_usuario():
    idUsuarios = len(usuarios) + 1
    nombre = input("Ingrese nombre: ")
    rango_edad = input("Ingrese rango de edad: ")
    correo = input("Ingrese correo: ")
    contrasena = input("Ingrese contraseña: ")
    nivel_actividad = input("Ingrese nivel de actividad física (Bajo/Moderado/Alto): ")
    hora_dormir = input("Ingrese hora de dormir (HH:MM): ")
    hora_despertar = input("Ingrese hora de despertar (HH:MM): ")
    
    nuevo_usuario = {
        "idUsuarios": idUsuarios,
        "Nombre": nombre,
        "RangoEdad": rango_edad,
        "CorreoElectronico": correo,
        "Contrasena": contrasena,
        "NivelActividadFisica": nivel_actividad,
        "HoraDormir": hora_dormir,
        "HoraDespertar": hora_despertar
    }
    usuarios.append(nuevo_usuario)
    print("Usuario creado con éxito.\n")

def eliminar_usuario():
    idUsuarios = int(input("Ingrese el ID del usuario a eliminar: "))
    global usuarios
    usuarios = [usuario for usuario in usuarios if usuario['idUsuarios'] != idUsuarios]
    print("Usuario eliminado con éxito.\n")

#funcionesCRUD para RegistrosSueno
def mostrar_registros_sueno():
    for registro in registros_sueno:
        print(f"ID Registro: {registro['idRegistrosSueno']}")
        print(f"ID Usuario: {registro['idUsuarios']}")
        print(f"Tipo de Sueño: {registro['TipoSueno']}")
        print(f"Hora: {registro['Hora']}:{registro['Minutos']} {registro['Meridiano']}")
        print(f"Fecha de Registro: {registro['FechaRegistro']}")
        print(f"Hora de Registro: {registro['HoraRegistro']}")
        print()

def crear_registro_sueno():
    idRegistrosSueno = len(registros_sueno) + 1
    idUsuarios = int(input("Ingrese ID del usuario: "))
    tipo_sueno = input("Ingrese tipo de sueño (Dormir/Despertar): ")
    hora = int(input("Ingrese la hora (HH): "))
    minutos = int(input("Ingrese los minutos (MM): "))
    meridiano = input("Ingrese meridiano (AM/PM): ")
    fecha_registro = input("Ingrese la fecha de registro (YYYY-MM-DD): ")
    hora_registro = input("Ingrese la hora de registro (HH:MM:SS): ")

    nuevo_registro = {
        "idRegistrosSueno": idRegistrosSueno,
        "idUsuarios": idUsuarios,
        "TipoSueno": tipo_sueno,
        "Hora": hora,
        "Minutos": minutos,
        "Meridiano": meridiano,
        "FechaRegistro": fecha_registro,
        "HoraRegistro": hora_registro
    }
    registros_sueno.append(nuevo_registro)
    print("Registro de sueño creado con éxito.\n")

#funciones CRUD para PreferenciasUsuario
def mostrar_preferencias_usuario():
    for pref in preferencias_usuario:
        print(f"ID Preferencia: {pref['idPreferenciasUsuario']}")
        print(f"ID Usuario: {pref['idUsuarios']}")
        print(f"Preferencia: {pref['Preferencia']}")
        print(f"Valor: {pref['Valor']}")
        print()

def crear_preferencia_usuario():
    idPreferenciasUsuario = len(preferencias_usuario) + 1
    idUsuarios = int(input("Ingrese ID del usuario: "))
    preferencia = input("Ingrese la preferencia: ")
    valor = input("Ingrese el valor de la preferencia: ")
    
    nueva_preferencia = {
        "idPreferenciasUsuario": idPreferenciasUsuario,
        "Preferencia": preferencia,
        "Valor": valor,
        "idUsuarios": idUsuarios
    }
    preferencias_usuario.append(nueva_preferencia)
    print("Preferencia del usuario creada con éxito.\n")

# Funciones CRUD para Recomendaciones
def mostrar_recomendaciones():
    for rec in recomendaciones:
        print(f"ID Recomendación: {rec['idRecomendaciones']}")
        print(f"Rango de Edad: {rec['RangoEdad']}")
        print(f"Recomendación: {rec['Recomendacion']}")
        print()

def crear_recomendacion():
    idRecomendaciones = len(recomendaciones) + 1
    rango_edad = input("Ingrese el rango de edad: ")
    recomendacion = input("Ingrese la recomendación: ")
    
    nueva_recomendacion = {
        "idRecomendaciones": idRecomendaciones,
        "RangoEdad": rango_edad,
        "Recomendacion": recomendacion
    }
    recomendaciones.append(nueva_recomendacion)
    print("Recomendación creada con éxito.\n")

#menu principal del CRUD
def menu_principal():
    while True:
        print("Seleccione una tabla para gestionar:")
        print("1. Usuarios")
        print("2. Registros de Sueño")
        print("3. Preferencias de Usuario")
        print("4. Recomendaciones")
        print("5. Salir")
        tabla = int(input())

        if tabla == 1:
            menu_usuarios()
        elif tabla == 2:
            menu_registros_sueno()
        elif tabla == 3:
            menu_preferencias_usuario()
        elif tabla == 4:
            menu_recomendaciones()
        elif tabla == 5:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Menús secundarios para cada tabla
def menu_usuarios():
    while True:
        print("Gestión de Usuarios:")
        print("1. Crear usuario")
        print("2. Mostrar usuarios")
        print("3. Eliminar usuario")
        print("4. Volver al menú principal")
        opcion = int(input())
        if opcion == 1:
            crear_usuario()
        elif opcion == 2:
            mostrar_usuarios()
        elif opcion == 3:
            eliminar_usuario()
        elif opcion == 4:
            break
        else:
            print("Opción inválida.")

def menu_registros_sueno():
    while True:
        print("Gestión de Registros de Sueño:")
        print("1. Crear registro de sueño")
        print("2. Mostrar registros de sueño")
        print("3. Volver al menú principal")
        opcion = int(input())
        if opcion == 1:
            crear_registro_sueno()
        elif opcion == 2:
            mostrar_registros_sueno()
        elif opcion == 3:
            break
        else:
            print("Opción inválida.")

def menu_preferencias_usuario():
    while True:
        print("Gestión de Preferencias de Usuario:")
        print("1. Crear preferencia")
        print("2. Mostrar preferencias")
        print("3. Volver al menú principal")
        opcion = int(input())
        if opcion == 1:
            crear_preferencia_usuario()
        elif opcion == 2:
            mostrar_preferencias_usuario()
        elif opcion == 3:
            break
        else:
            print("Opción inválida.")

def menu_recomendaciones():
    while True:
        print("Gestión de Recomendaciones:")
        print("1. Crear recomendación")
        print("2. Mostrar recomendaciones")
        print("3. Volver al menú principal")
        opcion = int(input())
        if opcion == 1:
            crear_recomendacion()
        elif opcion == 2:
            mostrar_recomendaciones()
        elif opcion == 3:
            break
        else:
            print("Opción inválida.")

# Ejecutar menu principal
menu_principal()
