numbers = input("> ").split(" ")
t = int(numbers[0]) #taxa
c = int(numbers[1]) # preço em reais
k = int(numbers[2]) #preço na moeda dooutro país

if k * t < c:
    print(t * k)
else:
    print(c)