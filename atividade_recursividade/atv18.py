def incremento_sucessivo(x,y):
    if y == 1:
        return x+1
    return incremento_sucessivo(x+1,y-1)

print(incremento_sucessivo(3,3))