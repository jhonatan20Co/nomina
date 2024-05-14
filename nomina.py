empleados = []

def crear_empleado():
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    direccion = input("Dirección: ")
    departamento = input("Departamento: ")
    cargo = input("Cargo: ")
    salario = float(input("Salario: "))
    fecha_ingreso = input("Fecha de ingreso (AAAA-MM-DD): ")
    estado_civil = input("Estado civil: ")

    empleado = {
        "nombre": nombre,
        "edad": edad,
        "direccion": direccion,
        "departamento": departamento,
        "cargo": cargo,
        "salario": salario,
        "fecha_ingreso": fecha_ingreso,
        "estado_civil": estado_civil
    }

    empleados.append(empleado)
    print("Empleado creado exitosamente")

def mostrar_empleados():
    for idx, empleado in enumerate(empleados, start=1):
        print(f"Empleado {idx}: {empleado['nombre']} - Departamento: {empleado['departamento']} - Cargo: {empleado['cargo']} - salario: {empleado['salario']}$ - fecha_ingreso: {empleado['fecha_ingreso']}" )

def actualizar_empleado():
    mostrar_empleados()
    id_empleado = int(input("ID del empleado a actualizar: ")) - 1
    if 0 <= id_empleado < len(empleados):
        campo = input("Campo a actualizar (nombre, edad, direccion, departamento, cargo, salario, fecha_ingreso, estado_civil): ")
        valor = input(f"Nuevo valor para {campo}: ")
        empleados[id_empleado][campo] = valor
        print("Empleado actualizado exitosamente")
    else:
        print("ID de empleado no válido")

def eliminar_empleado():
    mostrar_empleados()
    id_empleado = int(input("ID del empleado a eliminar: ")) - 1
    if 0 <= id_empleado < len(empleados):
        del empleados[id_empleado]
        print("Empleado eliminado exitosamente")
    else:
        print("ID de empleado no válido")

# Menú de opciones
while True:
    print("\nCRUD nomina")
    print("1. Crear Empleado")
    print("2. Mostrar Empleados")
    print("3. Actualizar Empleado")
    print("4. Eliminar Empleado")
    print("5. Salir")

    opcion = input("\nSelecciona una opción: ")

    if opcion == "1":
        crear_empleado()
    elif opcion == "2":
        mostrar_empleados()
    elif opcion == "3":
        actualizar_empleado()
    elif opcion == "4":
        eliminar_empleado()
    elif opcion == "5":
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")