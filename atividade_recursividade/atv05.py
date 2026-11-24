def serie_harmonica(n: int, i=None) -> float:
    if i == None:
        i = 1
    if i == n:
        return 1/n
    return 1/i + serie_harmonica(n,i+1)

print(serie_harmonica(2))