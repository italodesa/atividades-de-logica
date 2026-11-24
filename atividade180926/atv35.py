# 35) Um funcionário responsável pela expedição na Companhia UESPI tem o seguinte problema. 
# O  produto  é  muito  frágil  e  deve  ser  enviado  em  caixas  especiais.  Essas  caixas  estão 
# disponíveis  em quatro  tamanhos:  extragrande, grande, médio  e  pequeno,  as  quais podem 
# conter até 50, 20, 5 e 1 unidade, respectivamente. Escreva um programa que lê a quantidade 
# de produtos que deve ser enviada e imprima o número de caixas extragrande, grande, média 
# e pequena necessários para enviar os produtos utilizando o menor número de caixas e com a 
# menor quantidade de espaço desperdiçado. Execute o programa para 3, 18, 48, 78 e 10598 
# produtos a serem enviados. A saída deve ser semelhante a seguinte:
#  
# Obs: O programa deve continuar funcionando até que 
# seja informada uma quantidade de produtos igual a 0 
# (zero). 

# Caixa     Quant 
# --------- ----- 
# Extra     211 
# Grande    2 
# Média     1 
# Pequena   3 



while True:
    c_extra = 0
    c_grande = 0
    c_media = 0
    c_pequena = 0
    print("Digite a quantidade de produtos igual a 0 para sair")
    quantidade_de_produtos = int(input("Digite a quantidade de produtos: "))
    if quantidade_de_produtos == 0:
        break

    while quantidade_de_produtos > 0:
        if quantidade_de_produtos >= 50:
            quantidade_de_produtos -= 50
            c_extra += 1

        elif quantidade_de_produtos >= 20:
            quantidade_de_produtos -= 20
            c_grande += 1

        elif quantidade_de_produtos >= 5:
            quantidade_de_produtos -= 5
            c_media += 1

        else:
            quantidade_de_produtos -= 1
            c_pequena += 1

    print(f"{'caixa':<9}{'Quant':>5}")
    print(f"{'-' * 9} {'-' * 5}")

    print(f"{'Extra':<9}{c_extra:>5}")
    print(f"{'Grande':<9}{c_grande:>5}")
    print(f"{'Média':<9}{c_media:>5}")
    print(f"{'Pequena':<9}{c_pequena:>5}")