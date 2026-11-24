quantity = float(input("Entre com a quantidade: "))
m_de_100 = 0
m_de_5 = 0
m_de_10 = 0
m_de_50 = 0
m_de_1 = 0

while quantity > 0:
    if quantity >= 100:
        quantity -= 100
        m_de_100 += 1

    elif quantity >= 50:
        quantity -= 50
        m_de_50 += 1

    elif quantity >= 10:
        quantity -= 10
        m_de_10 += 1

    elif quantity >= 5:
        quantity -= 5
        m_de_5 += 1

    else:
        quantity -= 1
        m_de_1 += 1

print(f"{m_de_100} moedas de M$ 100")
print(f"{m_de_50} moedas de M$ 50")
print(f"{m_de_10} moedas de M$ 10")
print(f"{m_de_5} moedas de M$ 5")
print(f"{m_de_1} moedas de M$ 1")


for i in range(len())