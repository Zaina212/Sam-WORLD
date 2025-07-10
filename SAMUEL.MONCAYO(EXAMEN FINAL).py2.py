productos=  {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],'FS1230HD': [249990,0], 
} 

stock= {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0], 
} 

def stock_marca(marca):
    total=0
    for modelo,datos in productos.items():
        if datos[0].lower()==marca.lower():
            total+=stock.get(modelo,[0,0])[1]
    print("El stock es {total}")

def busqueda_precio(P_min,p_max):
    modelos_en_rango=[]
    for modelo, (precio, cant) in stock.items():
        if P_min <= precio <= p_max and cant > 0:
            marca= productos[modelo][0]
            modelos_en_rango.append(f"{marca}--{modelo}")
    if modelos_en_rango:
        print("Los notebooks entre los precios consultados son",sorted(modelos_en_rango))
    else:
        print("No hay notebooks en ese rango de precio")
        
def actualizar_precio(modelo, p ):
    if modelo in stock:
        stock[modelo][0]= p
        return True
    else: 
        return False
    
while True:
    print("\n*** MENU PRINCIPAL ***")
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir.")
    
    opcion= input("Ingrese opcion")
    
    if opcion == "1":
        marca= input("Ingrese marca a consultar")
        stock_marca(marca)
    elif opcion== "2":
        while True:
            try:
                p_min = int(input("Ingrese precio Minimo"))
                p_max= int(input("Ingrese precio Maximo"))
                break
            except ValueError:
                print("Debe ingresar valores enteros")
        busqueda_precio(p_min,p_max)
    
    elif opcion== "3":
        while True:
            modelo = input("Ingrese modelo a actualizar:") 
            try:
                nuevo_precio=int(input("Ingrese nuevo precio"))
            except ValueError:
                print("Debe ingresar un precio valido ")
                continue
            if actualizar_precio(modelo, nuevo_precio):
                print("Precio ACTUALIZADO!!")
            else:
                print("El modelo NO existe")
                
            comtinuar=input("¿Desea actualizar otro precio?(si/no):").lower()
            if comtinuar!= "si":
                break
    elif opcion == "4":
        print("Programa finalizado")
        break
    else:
     print("Debe seleccionar una opcion valida!!!!!")
    
               
            