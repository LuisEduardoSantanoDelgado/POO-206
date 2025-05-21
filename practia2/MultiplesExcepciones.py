try:
    numero = int(input("introduce un número"))
    resultado = 10 / numero
except (ValueError, ZeroDivisionError):
    print("Error:valor o división entre cero.")


