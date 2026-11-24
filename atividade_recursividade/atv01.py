n = 123
n = str(n)

def inverter(n,c=len(n)-1):
    if c == 0:
        return n[c]
    return n[c] + inverter(n,c-1)

print(inverter(n))

# ----------- SOLUÇÂO DOCHAT GPT ------------------

# def inverter(n, invertido=0):
#     if n == 0:
#         return invertido

#     return inverter(n // 10, invertido * 10 + n % 10)


# numero = int(input("Digite um número: "))

# print("Número invertido:", inverter(numero))

# Entendendo as operações:
# - n // 10: remove o último algarismo.
# - n % 10: pega o último algarismo.
# - invertido * 10: abre espaço para adicionar um novo algarismo.
# - invertido * 10 + n % 10: adiciona o algarismo ao número invertido.
# Caso base: quando n == 0, a função retorna o número invertido.

# Resultado
#  123 → 321