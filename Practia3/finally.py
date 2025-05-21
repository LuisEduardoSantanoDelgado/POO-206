try:
    print("Intentando dividir...")
    resultado = 10 / 0
except ZeroDivisionError:
    print("No puedes dividir entre cero.")
finally:
    print("Este mensaje siempre se deberá de imprimir.")