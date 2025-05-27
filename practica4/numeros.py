try:
    numero = input("introduce un número mayor que 10 ")
    n = int(numero)
    if n <= 10:
        raise ValueError("el número debe ser mayor que 10")
    
    resultado = ""
    for i in range(3, n + 1):
        if i % 2 != 0:
            if resultado == "":
                resultado = str(i)
            else:
                resultado = resultado + "," + str(i)
    
    print("Números impares desde 2 hasta", n, ":")
    print(resultado)
    
except ValueError:
    print("se debe de introducir un número entero válido y mayor que 10")
    