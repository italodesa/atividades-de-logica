def log(base,logaritmando):
    # Usando o método da bisseção
    expoente = 0
    while logaritmando ** expoente < base:
        expoente += 1
    if logaritmando ** expoente == base:
        return expoente
    
    superior = expoente
    inferior = expoente - 1
    m = (superior + inferior) / 2

    while superior - inferior > 0.000001:
        m = (superior + inferior) / 2
        if logaritmando ** m > base:
            superior = m
        else:
            inferior = m
    return (superior + inferior) / 2




print(log(1,2))