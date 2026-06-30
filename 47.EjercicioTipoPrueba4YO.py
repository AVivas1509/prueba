"""
lista = [
    diccionario = {"modelo":valor, "anio":valor, "precio": valor, "disponible":valor}
]

"""

# prueba de commit1

# Lista
vehiculos = [];

# funciones

# funciones menu
def mostrar_menu(): 
    print("========== MENÚ PRINCIPAL ==========");
    print("1. Agregar vehículo");
    print("2. Buscar vehículo");
    print("3. Eliminar vehículo");
    print("4. Actualizar disponibilidad");
    print("5. Mostrar vehículos");
    print("6. Salir");
    print("=====================================");

def leer_opc():
    try:
        opc = int(input("Ingrese una opción del menu: "));
    
        if(opc >= 1 and opc <= 6):
            return opc;
        else:
            raise ValueError;

    except ValueError:
        print("La opción del menu debe ser un valor numerico del 1 l 6.");

# funciones para validar
def validar_modelo(modelo):
    return (modelo.strip() != "");

def validar_anio(anio):
    return (anio > 1900);

def validar_precio(precio):
    return (precio > 0);

# funcion agregar un vehiculo
def agregar_vehiculo(vehiculos):
    modelo = input("ingrese el modelo del vehiculo: ");

    if(not validar_modelo(modelo)):
        print("El modelo no puede estar vacio ni contener espacios en blanco.");
        return;
    
    try:
        anio = int(input("Ingrese el añod el vehiculo: "));
    
        if(not validar_anio(anio)):
            raise ValueError;

    except ValueError:
        print("El anio debe ser un valor numerico mayor a 1900.");
        return;

    try:
        precio = float(input("Ingrese el precio del vehiculo: "));
    
        if(not validar_precio(precio)):
            raise ValueError;

    except ValueError:
        print("El precio del vehiculo debe ser un valor mayor a 0.");
        return;

    # crear el diccionario
    auto = {"modelo": modelo, "anio": anio, "precio": precio, "disponibilidad": False};

    # Agregar el auto a la lista
    vehiculos.append(auto);
    print("Vehiculo agregado exitosamente!");

# Función para buscar un vehiculo
def buscar_vehiculo(vehiculos, modelo_buscar):
    for i in range(len(vehiculos)):
        if(vehiculos[i]["modelo"] == modelo_buscar):
            return i;

    return -1;

# funcion para eliminar un vehiculo
def eliminar_vehiculo(vehiculos):
    modelo = input("Ingrese el modelo del auto a eliminar: ");
    posicion = buscar_vehiculo(vehiculos, modelo);

    if(posicion == -1):
        print(f"El vehículo {modelo} no se encuentra registrado");
    else:
        vehiculos.pop(posicion);
        print("Vehiculo eliminado exitosamente!!");

# Funcion para actualizar la disponibilidad
def actualizar_disponibilidad(vehiculos):
    for i in range(len(vehiculos)):
        if(vehiculos[i]["anio"] >= 2020):
            vehiculos[i]["disponibilidad"] = True;

    print("Disponibilidad de vehiculos actualizada correctamente!!");


# funcion que muestra todos los vehiculos
def mostrar_vehiculos(vehiculos):
    actualizar_disponibilidad(vehiculos);

    print("=== LISTA DE VEHICULOS ===");
    print("");

    for auto in vehiculos:
        print(f"Modelo: {auto["modelo"]}");
        print(f"Año: {auto["anio"]}");
        print(f"Precio: {auto["precio"]}");
        print("Estado: DISPONIBLE" if auto["disponible"] else "Estado: NO DISPONIBLE");
        print("********************************************");


# Implementacion del cuerpo
while True:
    mostrar_menu();
    opc = leer_opc();

    if(opc == 1):
        agregar_vehiculo(vehiculos);
    
    elif(opc == 2):
        modelo = input("Ingrese el modelo del vehiculo a buscar: ");    
        posicion = buscar_vehiculo(vehiculos, modelo);
    
        if(posicion == -1):
            print(f"El vehículo {modelo} no se encuentra registrado.");
        else:
            print("DATOS DEL VEHICULO")
            print(f"Modelo: {vehiculos[posicion]["modelo"]}");
            print(f"Año: {vehiculos[posicion]["anio"]}");
            print(f"Precio: {vehiculos[posicion]["precio"]}");
            print("Estado: DISPONIBLE" if vehiculos[posicion]["disponible"] else "Estado: NO DISPONIBLE");

    elif(opc == 3):
        eliminar_vehiculo(vehiculos);
    
    elif(opc == 4):
        actualizar_disponibilidad(vehiculos);

    elif(opc == 5):
        mostrar_vehiculos(vehiculos);

    elif(opc == 6):
        print("Gracias por usar el sistema. Vuelva Pronto");
        break;




