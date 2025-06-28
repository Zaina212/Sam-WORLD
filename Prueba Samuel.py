# Haga un programa que permita generar un menú de reservas para la tienda “Za-patillas Strike”. El menú principal debe permitir mostrar 4 opciones:

# TOTEM AUTOATENCIÓN RESERVA STRIKE
# 1.- Reservar zapatillas
# 2.- Buscar zapatillas reservadas.
# 3.- Ver stock de reservas.
# 4.- Salir.

# Todas las opciones del menú deben estar implementadas mediante funciones separadas del código principal (main).
# Al ingresar a la opción 1.- Reservar zapatillas, se debe permitir ingresar nombre de comprador y frase secreta por separado. Para que la reserva sea exitosa se debe cumplir lo siguiente:
# a) El nombre de comprador no debe estar repetido,
# b) Para realizar la reserva el cliente, debe digitar la frase secreta  “EstoyEnLista-DeReserva” respetando las mayúsculas y minúsculas.
# c) hay un stock máximo de 20 reservas, solo una reserva por comprador.
# En caso de cumplir todas las condiciones, la entrada se registra exitosamente.
# Al ingresar la opción 2.- Buscar zapatillas reservadas, el menú debe permitir buscar las reservas mediante el nombre. Si la reserva existe, preguntar si pagar un adicional por la reserva VIP, el cual permite reservar 2 pares de zapatillas
# Al ingresar la opción 3.- Ver Stock de reservas, el menú debe permitir observar el stock de zapatillas ya reservadas y cuantas quedan por reservar. 
# Al ingresar la opción 4.- Salir, el programa debe terminar mostrando:
# Programa terminado...

# Si se ingresa una opción distinta (que no sea 1, 2, 3 o 4), debe mostrarse:

# Debe ingresar una opción válida!!


reservas={}
stock_maximo=20

def menu():
    print("\nTOTEM AUTOATENCIÓN RESERVA STRIKE")
    print("1.- Reservar zapatillas")
    print("2.- Buscar zapatillas reservadas.")
    print(" 3.- Ver stock de reservas.")
    print("4. Salir")
    
    def reservar():
        print("\n-- Reservar Zapatillas")
        nombre= input("Nombre del comprador")
        
        if nombre in reservas:
            print("Error: ese nombre ya tiene una reserva.")
            return
        if cantidad_reservas() >= stock_maximo:
            print ("Error: No hay stock disponible para realizar nuevas reservas")
            return
        clave=input("Digite la clave secreta para confirmar la reserva")
        
        if clave != "Estoy en lista de reserva":
            print("Error: palabra clave incorrecta. Reserva no realizada")
        else:
            reservas[nombre] = 1
            print("Reserva hecha para {nombre}")
            
def buscar():
    print("\n-- buscar zapatillas reservadas--")
    Nombre=input("Nombre del comprador a buscar:")
    
    if Nombre in reservas:
        pares= reservas[nombre]
        tipo="VIP" if pares==2 else "estandar"
        print("Reservas encontradas: {nombre}- {pares} par(es) ({tipo}).")
        if pares == 1 :
            extra = input("¿Desea pagar adicional para ser un VIP y reservar 2 pares? (s/n):")
            if cantidad_reservas()< stock_maximo:
                reservas[nombre]= 2
                print("Reservas acatualizadas a VIP. Ahora {nombre} tiene 2 pares reservados.")
              else:
                print("No se puede actualizar el VIP; stock insuficiente")
             else: 
            print("Manteniendo reserva actual")
         else:
             print("No se necontro ningun areserva con este nombre")
             
def ver_stock():
    print("\n-- ver stock de reservas--")
    reservas= cantidad_reservas()
    disponibles= stock_maximo- resevados
    print("pares reservados {resrvados}")
    print("pares disponibles {disponibles}")
    
def main():
    while True:
        menu()
        opcion= input("Seleccione una opcion (1-4:")
        if opcion == "1":
        elif opcion== "2":
        elif opcion== "3":
            ver_stock()
        elif opcion=="4":
            print("\Programa terminado..."=
                  break
                  else 
                  print("\n Programa terminado:")
main()