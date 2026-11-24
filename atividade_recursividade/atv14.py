def fatorial(n):
    if n == 0:
        return 1
    if n == 1:
        return n
    return n * fatorial(n-1)

def super_fatorial(n):
    if n == 0:
        return 1
    if n == 1:
        return n
    return fatorial(n) * super_fatorial(n-1)

print(super_fatorial(4))