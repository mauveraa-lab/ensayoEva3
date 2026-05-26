print("Bienvenido alsistema de gestion de bicicletas")
capacidad_maxima =  25
bicis_disponible = 25
viajes_activos = 0
ejecutando = True
#ciclo principal
while ejecutando:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. bicicletas disponibles")
    print("2. Arrendar bicicletas (Salida)")
    print("3. Devolver bicicletas (Entrada)")
    print("4. Historial viajes activos")
    print("5. Salir")
    try:
        opcion = int(input("Seleccione una opcion (1-5): "))
    except ValueError:
        print("Opcion no valida,por favor,ingrese un numero entre 1 y 5")
        continue
        #opcion 1
    if opcion == 1:
        print(f"\n[info] cantidad actual de bicicletas disponible: {bicis_disponible}")
    #opcion 2 arrendar bicicletas
    elif opcion == 2:
        print(f"\n--- Arrendar bicicletas (disponibles: {bicis_disponible})---")
        if bicis_disponible == 0:
            print("lo sentimos, no quedan bicicletas disponibles")
        else:
            try:
                cantidad_a_arrendar = int(input("¿Cuantas bicicletas desea arrendar? "))
                if cantidad_a_arrendar <= 0:
                    print("Error: la cantidad a arrendar debe ser mayor a 0")
                elif cantidad_a_arrendar > bicis_disponible:
                    print(f"No hay suficientes bicicletas, puede arrendar hasta: {bicis_disponible}")
                else:
                    bicis_disponible -= cantidad_a_arrendar
                    viajes_activos += cantidad_a_arrendar
                    print(f"Arriendo exitoso, ha retirado {cantidad_a_arrendar} bicis")
            except ValueError:
                print("Error, debe ingresar un numero entero")
    #opcion 3- devolver bicicletas
    elif opcion == 3:
        diferencia = capacidad_maxima-bicis_disponible
        print(f"\n--- DEVOLVER BICICLETAS (espacio libre en estacion: {diferencia})")
        try:
            cantidad_a_devolver = int(input("¿Cuantas bicicletas desea devolver?: "))
            if cantidad_a_devolver <= 0:
                print("Error: la cantidad a resolver debe ser mayor a 0")
            elif bicis_disponible + cantidad_a_devolver > capacidad_maxima:
                print(f"Error: No se pueden devolver tantas bicicletas, supera cantidad maxima de 25 bicis")
            else:
                bicis_disponible += cantidad_a_devolver
                viajes_activos -= cantidad_a_devolver
                print(f"Devolucion exitosa ha regresa {cantidad_a_devolver} bicicletas" )
        except ValueError:
            print("Error: debe ingresar un numero entero valido")
    #opcion4: historial viajes activos
    elif opcion == 4:
        print(f"\n[HISTORIAL] actualmente hay {viajes_activos} bicicleta(s) en uso por usuario")