def is_cosoante(l):
    for i in "AEIOUaeiou":
        if l == i:
            return False
    return True

print(is_cosoante('a'))