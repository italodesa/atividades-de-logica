def desenha_quadrado(caractere,lado):
    for i in range(lado):
        for j in range(lado):
            print(caractere,end="")
        print()

    print()

    for i in range(lado):
        print(caractere * lado)


desenha_quadrado("+",3)