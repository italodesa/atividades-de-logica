def imprimir_decrescente(n):
    if n == 0:
        print(n)
        return
    print(n)
    return imprimir_decrescente(n-1)

imprimir_decrescente(5)