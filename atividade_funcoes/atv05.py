def media(*notas):
    soma = 0
    for i in notas:
        soma += i
    return soma / len(notas)

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

print(f"A média é: {media(nota1,nota2,nota3)}")