from math import pi

def volume_esfera(raio):
    v = (4 * pi * raio**3) / 3
    return v

r = float(input("Escreva o raio da esfera"))
print(f"O volume do {r} é {volume_esfera(r)}")
