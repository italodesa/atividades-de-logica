def menor_do_vetor(vetor, min = None, i = None):
    if i == None:
        i = len(vetor) - 1
        min = vetor[0]

    if i < 0:
        return min
    
    if vetor[i] < min:
        min = vetor[i]

    return menor_do_vetor(vetor,min,i-1)

print(menor_do_vetor([3,4,55,6,7,1,2,999]))