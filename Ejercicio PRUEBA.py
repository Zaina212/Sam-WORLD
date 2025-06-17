esquema=3
completo= 0 
incompleto=0


while True:
    try:
        pacientes = int(input("Ingrese cuantas personas se verificaran"))
        break
    except ValueError:
        print("Debe ingresar un numero entero")
        
for i in range(pacientes): # contador = 1 while
# contador <= pacientes:
    dosis=10
    while True:
       try:       
            dosis = int(input(f" Ingrese el numero de dosis recibidas por la persona {(i+1)}(el esquema completo es de {esquema} dosis) "))
              
            break
       except ValueError:
            print("Debe ingresar un numero entero")
            
    if dosis== esquema:
        print ("Esquema completo")
        completo +=1
        print("Esquema incompleto")
        incompleto +=1
print("Esquema termnado")