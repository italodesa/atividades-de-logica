# 1) Escreva um programa que imprima os números inteiros de 1 a 100
n = 100
for i in range(1,n+1):
    if (i % 10 == 0):
        print(i)
    else:
        if(i < 10):
            print(f"0{i}",end=" ")
        else:
            print(i,end=" ")