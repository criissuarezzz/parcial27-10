#Realiza los siguientes ejercicios en un fichero llamado Ejercicio1.py:
#*Convertir la variable "var_1" en todas las letras mayúsculas y en minúsculas (var_1 = "Módulo 1 de Python ")

#*Consulta el tamaño o la longitud de la variable "var_1" y calcula la división de ese numero entre "7" redondeado a 4 decimales

#*Realiza una función llamada funcion1  que calcule siguiente operación para que el resultado final sea igual a cero (0) //12 - (4 * 2) - (2 + 2)
#*Realiza una función llamada funcion2 para que calcule la siguiente operación para que el resultado final sea igual a catorce (14)// 12 - 4 * (2 - 2) + 2
#*Realiza una función llamda funcion3 para pedir al usuario que introduzca su edad, y después imprimir en la pantalla si es meyor de edad o no


var_1=str("Módulo 1 de Python")
var_1cap=var_1.upper()
var_1low=var_1.lower()
print(var_1,",", var_1cap,",",var_1low)

print("La longitud de este texto es", len(var_1))
div= len(var_1)/7
redondeado=round(div,4)
print("Dividiendo este número entre 7=", redondeado)

def funcion1():
    print("12 - (4 * 2) - (2 + 2)=")
    print (12 - (4 * 2) - (2 + 2))
funcion1()

def funcion2():
    print("12 - 4 * (2 - 2) + 2=")
    print(12 - 4 * (2 - 2) + 2)
funcion2()

def funcion3():
    edad= int(input("Introduzca su edad:"))
    if edad>=18:
        print("Usted es mayor de edad")
    else:
        print("Usted es menor de edad")
funcion3()