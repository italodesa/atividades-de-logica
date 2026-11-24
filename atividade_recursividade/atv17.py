def decima_para_binario(n):
    if n < 1:
        return ""
    return decima_para_binario(n//2)  + str(n % 2) 

print(decima_para_binario(10))