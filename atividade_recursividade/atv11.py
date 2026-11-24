def imprimir_pares(n,i=1):
    if n == i:
        if i % 2 == 0:
            print(i)
        return
    if i % 2 == 0:
        print(i)
    return imprimir_pares(n,i+1) 

imprimir_pares(10)