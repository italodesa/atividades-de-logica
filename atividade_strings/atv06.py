# 6) Faça um programa que lê uma string s e dois caracteres (exemplo, a e b). O programa deve 
# substituir todas as ocorrências de a por b e mostrar a string resultante. Por exemplo, se for lido 
# a string "goiabada" e os caracteres "a" e "o" a saída deve ser "goiobodo"

s = input("Digite uma palavra ai mano: ")
a = input("Digite um caractere: ")
b = input("Digite um caractere: ")
s2 = ""

for i in s:
    if i == a:
        s2 += b
        continue
    s2 += i
    
print(s2)