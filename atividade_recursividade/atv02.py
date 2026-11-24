def soma_vetor(vetor,i=None) -> int:
    if i == None:
        i = len(vetor)-1
    if i == 0:
        return vetor[i]
    return vetor[i] + soma_vetor(vetor,i-1)



vetor = [1,2,3,4,5,6,7,8,9,10]
print(soma_vetor(vetor))