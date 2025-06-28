def reservar(nombre_reservas, maximo_stock):
    total_reservado = sum(nombre_reservas.values())
    if total_reservado >= maximo_stock:
        print("No hay más stock disponible para reservar.")
        return nombre_reservas

    print("\n-- Reservar Zapatillas --")
    nombre = input("Nombre del comprador: ")

    if nombre in nombre_reservas:
        print("Error: esa persona ya tiene una reserva.")
        return nombre_reservas

    clave = input("Digite la palabra secreta para confirmar la reserva: ")

    if clave != "EstoyEnListaDeReserva":
        print("Error: palabra clave incorrecta. Reserva no realizada.")
        return nombre_reservas

    nombre_reservas[nombre] = 1
    print("Reserva realizada exitosamente para", nombre)
    return nombre_reservas


def buscar(nombre_reservas):
    print("\n-- Buscar Zapatillas Reservadas --")
    nombre = input("Nombre del comprador a buscar: ")

    if nombre not in nombre_reservas:
        print("No se encontró ninguna reserva con ese nombre.")
        return nombre_reservas

    cantidad = nombre_reservas[nombre]

    if cantidad == 2:
        tipo = "VIP"
    else:
        tipo = "estándar"

    print("Reserva encontrada:", nombre, "-", cantidad, "par(es)", "(", tipo, ")")

    if cantidad == 1:
        respuesta = input("¿Desea pagar adicional para VIP y reservar 2 pares? (s/n): ")
        if respuesta.lower() == "s":
            nombre_reservas[nombre] = 2
            print("Reserva actualizada a VIP. Ahora", nombre, "tiene 2 pares reservados.")
        else:
            print("Manteniendo reserva actual.")
    return nombre_reservas


def ver_stock(nombre_reservas, maximo_stock):
    print("\n-- Ver Stock de Reservas --")
    reservados = sum(nombre_reservas.values())
    disponibles = maximo_stock - reservados
    print("Pares reservados:", reservados)
    print("Pares disponibles:", disponibles)


def menu():
    reservas = {}
    stock_total = 20

    while True:
        print("\nTOTEM AUTOATENCIÓN RESERVA STRIKE")
        print("1.- Reservar zapatillas")
        print("2.- Buscar zapatillas reservadas")
        print("3.- Ver stock de reservas")
        print("4.- Salir")
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            reservas = reservar(reservas, stock_total)
        elif opcion == "2":
            reservas = buscar(reservas)
        elif opcion == "3":
            ver_stock(reservas, stock_total)
        elif opcion == "4":
            print("\nPrograma terminado...")
            break
        else:
            print("Está equivocado. Debe ingresar una opción entre 1 y 4.")


menu()

