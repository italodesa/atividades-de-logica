# 7) Escreva uma função “inva” em Python que recebe um dicionário d e retorna um dicionário 
# “inverso” do dicionário dado, onde, a cada valor v de d está associada a lista das chaves de d 
# que levam a v. Exemplos: 

# eu vou criar um dicionario com coda valor de dentro dos valores, e seu valor vai ser uma lista de cada chave em que ele aparece

def inva(dic) -> dict:
    new = {}
    for i in dic:
        if new.get(dic[i]) != None:
            new[dic[i]].append(i)
            continue
        new[dic[i]] = [i]
    return new

teste = {
    "ito": 10,
    "lavis": 20,
    "milu":10
}

print(inva(teste))



