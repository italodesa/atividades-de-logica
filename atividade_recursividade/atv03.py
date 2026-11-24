def soma(n: int) -> int:
    if n <= 1:
        return n
    return n + soma(n-1)

print(soma(5))