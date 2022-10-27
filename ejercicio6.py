numeros=[6, 6, 8, 4, 3, 5, 5]

print(numeros)
def modificar(numeros):
    for numero in numeros:
        if numeros.count(numero)>1:
            numeros.remove(numero)
    print("Si eliminamos los elementos duplicados la lista queda así: {}".format(numeros))

    numeros=sorted(numeros)
    numeros=numeros[::-1]
    print("Ahora ordenada de mayor a menor queda así: {}".format(numeros))
    pares=[]
    for i in numeros:
        if i%2==0:
            pares.append(i)
        else:
            numeros.pop()
    suma=sum(pares)
    print("Los numeros pares son {}, siendo su suma {}".format(pares, suma))
    
    pares.append(suma)
    pares=sorted(pares, reverse=True)
    print("La lista quedaría ahora así, añadiendo como primer elemento la suma: {}".format(pares))
    print(pares)
   
    print(pares[0] == sum(pares[1:]))
modificar(numeros)


