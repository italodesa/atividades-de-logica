def is_raiz_exata(r):
    v = 1
    while v**v < r:
        v += 1
    if v**v == r:
        return True
    return False

print(is_raiz_exata(4))