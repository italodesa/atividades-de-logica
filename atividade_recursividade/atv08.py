def potencia(x:int,k:int) -> int:
    if k == 1:
        return x
    return x * potencia(x,k-1)

print(potencia(2,4))