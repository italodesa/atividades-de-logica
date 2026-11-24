def pell(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return 2 * pell(n-1) + pell(n-2)

print(pell(6))