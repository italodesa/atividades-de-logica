# 8) Escreva um programa que: 
# a) lê duas notas de vários alunos e armazena tais notas em um dicionário, onde a chave é o 
# nome do aluno. A entrada de dados deve terminar quando for lida uma string vazia como 
# nome. 
# b) Escreva uma função que retorna a média do aluno, dado seu nome. 
# c) Escreva um programa que exiba o nome é a média do aluno de maior média.

def media(arr) -> int:
    soma = 0
    for i in arr:
        soma += i
    return soma / len(arr)

def mostrar_aluno(dic,nome):
    print(f"Nome: {nome}, Média: {media(dic[nome])}")

def maior_media(dic):
    maior_media = -1
    nome = ""
    for i in dic:
        if media(dic[i]) > maior_media:
            maior_media = media(dic[i])
            nome = i
    print(f"Nome: {nome}, Média: {maior_media}")



count = 1
alunos = {}
while True:
    nome = input(f"Digite o nome do aluno {count}: ")
    if nome == "":
        break
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    count += 1
    alunos[nome] = [nota1,nota2]

while True:
    print("==== Alunos ====")
    print("[ 1 ] Ver media dado o nome")
    print("[ 2 ] nome e média do aluno de meljor média")
    print("[ 0 ] Sair")

    r = int(input("> "))

    match r:
        case 1:
            nome = input("Digite o nome: ")
            mostrar_aluno(alunos,nome)
        case 2:
            maior_media(alunos)
        case 0:
            break
        case _:
            print("Digite uma opção valída")



