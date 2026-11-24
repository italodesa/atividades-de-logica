# 33) Escreva um programa que gere, para um valor n ≥ 0 fornecido pelo usuário, 
# um "quadrado" de n linhas e n colunas que tenha caracteres '*' nas posições 
# da diagonal principal e os caracteres '.' nas demais posições. Por exemplo, 
# para n = 5 o programa deve gerar o quadrado descrito ao lado

# 1,2,3,4..n
ast = 0
n = int(input("Digite um número: "))
cn = n-1
for i in range(n):
    print(("." * ast)+"*"+("."*cn))
    ast += 1
    cn -= 1