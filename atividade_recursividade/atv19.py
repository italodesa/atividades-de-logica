def soma_dos_digitos(n):
    if n == 0:
        return 0
    return (n % 10) + soma_dos_digitos(n // 10)

print(soma_dos_digitos(221))