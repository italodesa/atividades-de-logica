def imprimir_pares(n,i=None):
    if i == None:
        i = n
    if i == 0:
        return
    if i % 2 == 0:
        print(i)
    return imprimir_pares(n,i-1) 

imprimir_pares(10)