# 3) Escreva um programa que leia um texto pelo teclado e exiba este texto em letras minúsculas. 
texto = input("Informe um texto: ")
texto_lower = ""
for i in texto:
    if i == " ":
        texto_lower = texto_lower + i
        continue
    if ord(i) >= 97:
        texto_lower = texto_lower + i
        continue
    texto_lower = texto_lower + chr(ord(i) + 32)

print(texto_lower)