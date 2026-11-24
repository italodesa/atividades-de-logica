import random
lista = []
for i in range(50):
    lista.append(random.randint(0,100))

print("Print normal:")
for i in lista:
    print(i,end=" ")

print()

print("Print reverso")
for i in range(len(lista)-1,-1,-1):
    print(lista[i],end=" ")