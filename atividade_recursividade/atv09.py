def imprimir_crescente(n,i=0):
    if i == n:
        print(i)
        return
    print(i)
    return imprimir_crescente(n,i+1)

imprimir_crescente(5)