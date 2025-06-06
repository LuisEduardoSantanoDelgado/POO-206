palabra1 = input("Palabra 1: ")
palabra2 = input("Palabra 2: ")

letra1 = len(palabra1)
letra2 = len(palabra2)

if letra1 > letra2:
    print("La palabra", palabra1, "es más larga que", palabra2, "por", letra1 - letra2, "letras")
elif letra2 > letra1:
    print("La palabra", palabra2, "es más larga que", palabra1, "por", letra2 - letra1, "letras")
    
    
else:
    print("Las palabras tienen la misma cantidad de caracteres")

