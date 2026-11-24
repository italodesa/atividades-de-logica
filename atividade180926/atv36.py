# 36) Escreva um programa que imprime um calendário para 
# um  determinado  mês.  O  calendário  deve  conter  cada 
# dia  do  mês  e  o  dia  da  semana  correspondente.  A 
# entrada consiste de um inteiro especificando em que dia 
# da semana cai o primeiro dia do mês (1 = Domingo, 2 = 
# Segunda, ..., 7 = Sábado) e um inteiro especificando o 
# número de dias que o mês possui. Ao lado, um exemplo 
# para p = 3 e n = 31

primeiro_dia = int(input("Digite em que dia cai o primeiro dia da semana: "))
total_de_dias = int(input("Digite o toal de dias do mês: "))
count_dia = primeiro_dia

print("-" * 21)
print(f"D  S  T  Q  Q  S  S")
print("-" * 21)

print("   " * (primeiro_dia - 1), end="")
for i in range(1,total_de_dias+1):
    print(f"{i:2}",end=" ")

    if (i + primeiro_dia - 1) % 7 == 0:
        print()

print()
print("-" * 21)