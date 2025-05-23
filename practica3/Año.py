while True:
    entrada = input("introduce el año:")
    if entrada.lower() == "salida":
      print("Salida")
      break
    try:
        numero = int(entrada)
        if numero < 0:
           raise ValueError ("no se aceptan numeros negativos")
        if numero % 4 == 0:
            print("el año es bisiesto")
        else:
            print("el año no es bisiesto")
    except:
        print("lo que introduciste no es valifo")
        
        
            
            
            
       
    