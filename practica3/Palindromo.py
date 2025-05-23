while True:
    texto = input("ingresa la palabra: ")
    if texto.lower() == "salida":
        print("salida")
        break
    
    try:
        limpio = texto.replace(" ", "").lower()

        if limpio == limpio[::-1]:
            print("es palíndroma.")
        else:
            print("no es palíndroma.")
    except:
        print("Lo que introduciste no es válido")