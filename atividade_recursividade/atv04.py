def inverter_vetor(vetor, i=None):
    if i == None:
        i = len(vetor) - 1
    if i == 0:
        return [vetor[0]]
    return [vetor[i]] + inverter_vetor(vetor, i-1)

print(inverter_vetor([1,2,3,4,5]))