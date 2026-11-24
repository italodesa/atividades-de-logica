def contador(n:int, k:int) -> int:
    if n == 0:
        return 0
    if n % 10 == k:
        return 1 + contador(n // 10, k)
    return contador(n // 10, k)

print(contador(1234522,2))