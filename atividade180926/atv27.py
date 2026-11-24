# 27) Escreva um programa que, para um dado valor inteiro positivo, verifica se tal valor é uma 
# potência de 2. Em caso afirmativo, o programa deve fornecer o valor da potência. Em caso 
# contrário, uma mensagem apropriada deve ser gerada.

n = int(input("Digite um numero: "))


# Operador " & " compara bit a bit, e retorna 1 caso dois bits sejam 1 (tipo um and)
# Nesse contexto, observamos que, um numero que é um quadrado perfeito possui somente um bit ligado
# Por exemplo, 4 = 100,
# e 100 - 1 == 11
# fazendo a comparação:
# 100
#  11
# -----
# 000
#como deu 0, usei o inversor para virar 1

if (not(n & (n-1))):
    print("é um quadrado perfeito")
else:
    print("não é um quadrado perfeito")