def is_minuscula(l):
    if (ord(l) >= 97) and (ord(l) <= 127):
        return True
    return False

print(is_minuscula('A'))