#Crea un script llamado descomposicion.py que realice las siguientes tareas:
# Debe tomar 1 argumento que será un número entero positivo.
#En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.
#El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... tal que por ejemplo si se introduce el número 3287:

#python descomposicion.py 3647

#El programa deberá devolver una descomposición línea a línea como la siguiente utilizando las técnicas de formateo:

#0007

#0080

#0200

#1000

#Pista

#Que el valor sea un número no significa necesariamente que deba serlo para formatearlo. Necesitarás jugar muy bien con los índices y realizar muchas conversiones entre tipos cadenas, números y viceversa


import sys
print("Introduce un número entero positivo de 4 cifras")
def pedir_numero():
    while True:
        numero=(input("Introduce un número de 4 cifras:")) #str para que se pueda contar el numero de carácteres que posee el número
        if len(numero)!=4:
            print("Escribe un número entero de 4 cifras", file=sys.stderr)
        else:
            return str(numero)

def descomposicion(numero):
    contador=0
    while True:
        for digito in numero:
            contador += 1
            print((digito.ljust(int(contador), '0')).zfill(len(numero)),)
        if contador >= len(numero):
            break

descomposicion(pedir_numero()[::-1])
