# 16) Escreva um programa que mostre os números quadrados perfeitos entre 100 e 200.

print("Quadrados perfeitos entre 100 e 200:")
for i in range(100,201):
    raiz = int(i ** 0.5)
    if (raiz * raiz == i):
        print(i)