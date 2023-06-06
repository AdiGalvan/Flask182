class Almacen:
    def _init_(self, id, nombre, clas, marca, precio):
       self.id = id
       self.nombre = nombre
       self.clas = clas
       self.marca = marca
       self.precio = precio

bebida = [] #toda la info se guarda aqui 

def alta():
    id = int(input("Ingrese el ID de la bebida: "))
    nombre = input("Ingrese el nombre de la bebida: ")
    precio = float(input("Ingrese el precio de la bebida: "))
    clas = input("Ingrese la clasificacion de la bebida: ")
    marca = input("Ingrese la marca de la bebida: ")

    bebida.append(id)
    bebida.append(nombre)
    bebida.append(precio)
    bebida.append(clas)
    bebida.append(marca)

    print("La bebida fue dada de alta correctamente")

def baja_articulo():
        id=input("Ingrese el id que desee eliminar: ")
        existe_id=None
        if existe_id(id)=="No existe la bebida":
            print("La bebida que desea eliminar no existe en el almacen")
        else:
            print("La bebida ah sido eliminada exitosamente")

def actualizar():
        id=input("Ingrese el ID de la bebida: ")
        if existeid(id)=="No existe la bebida":
            print("La bebida que desea actualizar no existe en el almacen")
        else:
         nombre=input("Ingrese el nuevo nombre de la bebida: ")
        precio=float(input("Ingrese el nuevo precio de la bebida: "))
        clas=input("Ingrese la clasificacion de la bebida: ")
        marca=input("Ingrese la marca de la bebida: ")
        actualizar(id,nombre,precio,clas,marca)

def mostrar():
       if len(bebida) == 0:
        print("No hay bebidas dentro del almacen")
       else:
         for lista in bebida:
            mostrar_bebida(lista)

def mostrar_bebida(lista):  
            print(f"ID: {lista.id}") 
            print(f"Nombre: {lista.nombre}")
            print(f"Clasificacion: {lista.clas}")
            print(f"Marca: {lista.marca}")
            print(f"Precio: {lista.precio}")
          
def precio_promedio():
    if not bebida:
        print("No hay bebidas dentro del almacen")
    else:
        total = sum(lista.precio for lista in bebida)
        promedio = total / len(bebida)
        print(f"Precio promedio de las bebidas: {promedio}")

def cantidad_marca():
    marca = input("Ingrese el nombre de la marca: ")
    cantidad = sum(1 for lista in bebida if lista.marca == marca)
    print(f"Cantidad de bebidas de la marca {marca}: {cantidad}")

def cantidad_clas():
    clasificacion = input("Ingrese la clasificación: ")
    cantidad = sum(1 for bebidas in bebida if lista.clasificacion == clasificacion)
    print(f"Cantidad de bebidas de la clasificación {clasificacion}: {cantidad}")

def menu():
    print("========BIENVENIDO AL ALMACEN BEBIDAS==========")
    print("================OPCIONES==============")
    print("1...Dar de alta bebida")
    print("2...Dar de baja bebida")
    print("3...Actualizar bebida")
    print("4...Mostrar todas las opciones de bebidas")
    print("5...Calcular precio promedio")
    print("6...Cantidad de Marca de la bebida")
    print("7...Cantidad de Clasificacion de la bebida")
    print("8..Salir")
    

menu()

while True:
    opcion = input("Introduzca la opcion que desee realizar: ")

    if opcion =="1":
        alta()
    elif opcion =="2":
       baja_articulo()
    elif opcion =="3":
        actualizar()
    elif opcion =="4":
        mostrar()
    elif opcion =="5":
        precio_promedio()
    elif opcion == "6":
        cantidad_marca()
    elif opcion == "7":
        cantidad_clas()
    elif opcion == "8":
        print("¡QUE TENGA UN EXCELENTE DIA!")
        break
    else:
        print("La opción es inválida. Ingrese una nueva")


    print()
    menu()
