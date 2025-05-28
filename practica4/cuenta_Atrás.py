try:
    numero = input("Introduce un número entero positivo: ")
    
    num = int(numero)
    if num < 0:
        raise ValueError("el número debe ser positivo.")
    
    resultado = ""
    for i in range(num, -1, -1):
        if resultado == "":
            resultado = str(i)
        else:
            resultado = resultado + "," + str(i)
    
   
    print(resultado)

except ValueError:
    print("debes ingresar un numero entero")
