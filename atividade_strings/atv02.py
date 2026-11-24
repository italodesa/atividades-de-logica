# 2) Escreva um programa que leia um texto pelo teclado e exiba este texto em letras maiúsculas

texto = input("Digite um texto: ")
texto_upper = ""
for i in texto:
    if i == " ":
        texto_upper = texto_upper + i
        continue
    if ord(i) < 97:
        texto_upper = texto_upper + i
        continue
    texto_upper = texto_upper + chr(ord(i) - 32)

print(texto_upper)
