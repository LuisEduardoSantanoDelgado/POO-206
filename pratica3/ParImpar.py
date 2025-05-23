while True:
    try:
    
        numero = int(input("Introduce un número entero:"))
        if numero % 2 == 0:
            print("El número es par.")
        else:
            print("El número es impar.")          
    except:
        print("Por favor, introduce un número entero válido.")
        break
        