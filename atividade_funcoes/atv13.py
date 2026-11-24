def is_primo(n):
    if n == 1:
        return True
    for i in range (2,n):
        if n % i == 0:
            return False
    return True

def is_regular(number):
    fatores = {}
    # 4 /2 = 2
    # 2 / 2
    # 1 / acabou
    while number > 1:
        n = 2
        while (number % n != 0 or not is_primo(n)):
            n += 1
        if fatores.get(n) == None:
            fatores[n] = 1
        else:
            fatores[n] += 1

        number /= n 

    for i in fatores.keys():
        if i > 5:
            return False
    return True

print(is_regular(5))