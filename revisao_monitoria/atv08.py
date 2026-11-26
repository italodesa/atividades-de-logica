# 8. A sequência de Fibonacci começa com 0 e 1, e cada termo seguinte é a soma dos dois anteriores.
# Crie  uma  função  recursiva  chamada  fibonacci  que  receba  uma  posição  n  e  retorne  o  termo
# correspondente. Considere fibonacci(0) = 0 e fibonacci(1) = 1.
# 0 1 1 2 3 5...

def fib(n):
    if n == 1:
        return 0
    if n== 2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(4))