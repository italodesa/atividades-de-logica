# 1) Escreva uma função, chamada contaVoigais, que conta todas as vogais presentes no texto 
# recebido  como  parâmetro  e  retorna  um  dicionário  contendo  a  quantidade  de  cada  vogal. 
# Escreva um programa a fim de testar sua função, e exiba, no fim, os dados do dicionário 
# retornado. 

def contarVogais(arr):
    vogais = {}        
    for i in arr:
        if i in 'aeiouAEIOU':
            if (not vogais.get(i.lower())):
                vogais[i.lower()] = 1
            else:
                vogais[i.lower()] += 1
    return vogais

palavra = "oi italo AAA"
print(contarVogais(palavra))