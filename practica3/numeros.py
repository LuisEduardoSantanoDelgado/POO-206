while True:
    entrada = input("introduce un número entero: ")
    if entrada.lower() == "salida":
        print("salida")
        break
    try:
        numero = int(entrada)
        if numero < 0:
            raise ValueError("no se aceptan números negativos.")
        if numero % 2 == 0:
            print("el número es par.")
        else:
            print("el número es impar.")
    except:
        print("lo que introduciste no es valido")