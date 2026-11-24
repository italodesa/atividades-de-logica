# 5) Faça uma função que encontre todas as chaves que estão associadas a um determinado valor 
# em um dicionário. A função receberá no primeiro parâmetro o dicionário a ser analisado, e 
# como segundo parâmetro o valor da chave a ser buscada. A função retornará uma lista com as 
# chaves  encontradas,  essa  lista  pode  ter  diversos  valores,  apenas  um  ou  nenhum.  Nos 
# exemplos, a função foi chamada de procuraReversa(). Exemplo: 

def procurar_chaves(dic: dict,valor) -> list:
    chaves = []
    for i in dic:
        if dic[i] == valor:
            chaves.append(i)
    return chaves

dic = {
    "oi":1,
    "o":1,
    "i": 2
}

print(procurar_chaves(dic,1))