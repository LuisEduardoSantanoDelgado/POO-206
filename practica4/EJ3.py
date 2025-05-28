try:
    frase = input("Introduce una frase: ")
    letra = input("Introduce una letra: ")
    
    if len(letra) != 1:
        raise ValueError("Solo una letra.")
    
    contador = 0
    for l in frase.lower():
        if l == letra.lower():
            contador += 1
    
    print("La letra aparece", contador, "veces.")
    
except:
    print("Error, por favor introduce una frase y una letra válidas.")
    