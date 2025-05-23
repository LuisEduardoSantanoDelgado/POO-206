while True:
    contraseña = input("introduce la contraseña:")
    if contraseña.lower() == "salida":
        print("salida")
        break

    if len(contraseña) < 10:
        print("Tu contraseña es muy corta.")
        continue

    tiene_num = any(c.isdigit() for c in contraseña)
    tiene_especial = any(c in "/\!@#$%^&*()_[]{}|;:,.<>?+-=" for c in contraseña)

    if not tiene_num:
        print("debe tener al menos un número.")
    elif not tiene_especial:
        print("debe tener al menos un carácter")
    else:
        print("Contraseña válida.")
