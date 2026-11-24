def imprime_serie(i, j, k):
    if i > j:
        return
    print(i)
    return imprime_serie(i+k,j,k)

imprime_serie(2,10,2)