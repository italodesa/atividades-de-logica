# 31) Dado um número inteiro positivo, determine a sua decomposição em fatores 
# primos. A saída do programa deve ser semelhante ao exemplo ao lado. 

n = int(input("Digite um número: "))
value = n
d = 2
while n >= 1:
    if n == 1:
        print(f"{1:>3}")
        break

    if (n % d == 0):
        print(f"{n:>3} | {d}")
        n //= d
        d = 2
    else:
        d += 1