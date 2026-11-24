# 20) Escreva um programa que leia uma palavra e verifique se esta palavra representa um
# identificador válido
palavra: str = input("Digite uma palavra:")
valida = True
for i in palavra:
    if i in '@#$%&*(){[]}!?/,.+=-':
        valida = False
        break

if palavra == "":
    valida = False

if valida:
    print("Palavravalida")
else:
    print("Palavra invalida")
    
# ---------------Meu jeito ----------------------------

def verify_word(word: str) -> bool:
    if word == "":
        return False

    for i in palavra:
        if i in '@#$%&*(){[]}!?/,.+=-':
            return False
    