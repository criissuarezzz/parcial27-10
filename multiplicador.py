def multiplicador():
    while True:
        numero_magico=int(123456790)
        print("El número mágico es: {}".format(numero_magico))
        numero_usuario=int(input("Introduce un número entre 1 y 9:"))
        while not 1<=numero_usuario<=9:
            numero_usuario=input("Introduce un número entre 1 y 9:")
            try:
                numero_usuario=(int(numero_usuario))
            except:
                numero_usuario==0 or numero_usuario>9
            print("El número introducido es", numero_usuario)
    
        nuevo_numero_usuario=numero_usuario*9
        print("Multiplicando", numero_usuario, "por 9, el resultado optenido es", nuevo_numero_usuario)

        nuevo_numero_usuario=nuevo_numero_usuario*numero_magico
        print("Ahora el resultado obtenido de multiplicar el numero anterior, por el número mágico es", nuevo_numero_usuario)
multiplicador()
