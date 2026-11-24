from math import pi

def graus_para_radianos(grau):
    return grau * pi / 180

def redianos_para_graus(radiano):
    return radiano * 180 / pi

print(graus_para_radianos(180))
print(redianos_para_graus(pi))