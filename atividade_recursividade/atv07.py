def mult_rec(x,  y):
    if y == 1:
        return x
    return x + mult_rec(x,y-1)

print(mult_rec(3,3))