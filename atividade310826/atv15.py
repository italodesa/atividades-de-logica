from math import pi
a = float(input("Enter a A: "))
b = float(input("Enter a B: "))
c = float(input("Enter a C: "))

area_triangulo = a * b / 2
area_circle = pi * (c * c)
area_trapezio = ((a+b) * c) / 2
area_quadrado = b * b
area_retangulo = a * b

print(f"A area do triangulo que tem A por base e B por altura é: {area_triangulo}")
print(f"A area do circulo de raio C é: {area_circle}")
print(f"A area do trapezio que tem A e B por bases e C por altura é: {area_trapezio}")
print(f"A area do quadrado de lado B é: {area_quadrado}")
print(f"A area do rentangulo de lados A e B é: {area_retangulo}")