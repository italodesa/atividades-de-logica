# 6) Faça um programa que leia nomes de alunos e suas respectivas notas até que o nome ’oooo’ 
# seja informado, após o fim da leitura, imprima o nome do aluno que possui a maior nota. Obs.: 
# Use dicionário para resolver essa questão. 

alunos = {}

nome_maior = ""
while True:
    nome = input("Digite o nome: ")
    if nome == "oooo":
        break
    nota = float(input("Digite a nota: "))
    alunos[nome] = nota


print(alunos)
maior = -1.0

# for nome in alunos -> o nome é as chaves
for i in alunos.keys():
    if alunos[i] > maior:
        maior = alunos[i]
        nome = i

if maior > 0:
    print(f"a maior nota foi do {nome}, e ele tirou: {nota}")

