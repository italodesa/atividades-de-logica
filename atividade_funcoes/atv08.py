def mes(n):
    primeiro_trimestre = {
        1: "janeiro",
        2: "fevereiro",
        3: "março"
    }

    if primeiro_trimestre.get(n) == None:
        print("mês inválido")
        return
    
    print(primeiro_trimestre.get(n))
    return

mes(3)