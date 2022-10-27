#En este ejercicio se os pide crear un fichero llamado listasCEU.py que realice las siguientes funcionnes
#Define una lista que contenga al menos 4 elementos de todos los tipos de valores permitidos en Python.
#Selecciona cada dos elementos (uno si otro no) desde el final de la lista.
#Cambia solamente la posición del primer elemento con el último elemento de la lista.
#Elimina el último elemento de la lista modificada en el paso anterior.
#Crea una nueva lista con la repetición de los elemento de la lista guardada en el paso anterior.
valor1=int(input("Introduzca un número entero:"))
valor2=float(input("Introduzca un número decimal:"))
valor3=str(input("Introduzca una palabra:"))
num1=input("introduzca un número:")
num2=input("Introduzca otro número:")
valor4=bool(num1>num2)
lista=[valor1, valor2, valor3, valor4]
print(lista.reverse())
print(lista[::2])
lista=lista.reverse()



