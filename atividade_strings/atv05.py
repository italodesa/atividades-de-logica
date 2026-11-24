# 5) Escreva um programa que leia um texto pelo teclado e exiba este texto com as primeiras letras 
# de  cada  palavra  em  maiúsculas.  (Nota:  Uma  palavra  é  qualquer  sequência  de  caracteres 
# separada por um ou mais espaços).

texto = input("Digite um número: ")
texto2 = ""
t = 0
next = False


while t <= len(texto) - 1:
    
    if t == 0:
        if ord(texto[t]) >= 97 and ord(texto[t]) <= 122:
            texto2 = texto2 + chr(ord(texto[t]) - 32)
            t += 1
            continue

    if next:
        if ord(texto[t]) >= 97 and ord(texto[t]) <= 122:
            texto2 = texto2 + chr(ord(texto[t]) - 32)
            t += 1
            next = False
            continue
        texto2 = texto2 + texto[t]
            
    if texto[t] == " ":
        next = True

    texto2 = texto2 + texto[t]

    t += 1

print(texto2)