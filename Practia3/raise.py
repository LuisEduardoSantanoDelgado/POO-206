edad = int(input("Introduce tu edad: "))

if edad < 0:
    raise ValueError("La edad no puede ser negativa.")

print("Edad válida:", edad)



