def sumar_lista(numeros):
    tmp = 0

    for i in range(len(numeros)):
        tmp += numeros[i]

    result = tmp
    return result

print(sumar_lista([2,5,3]))

