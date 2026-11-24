seq = [int(i) for i in (input("> ").split(" "))]
array_position = [int(i) for i in (input("> ").split(" "))]

ocorrencias = [0] * 10


for valor in seq:
    ocorrencias[valor] += 1

print(ocorrencias)

# 9 4 3 9 1 2 4 5 1 1 9 7 0 5
# 1 9 4 11 13