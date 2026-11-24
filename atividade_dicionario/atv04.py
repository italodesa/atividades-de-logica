# 4) A conta do cartão de crédito de uma pessoa pode ser modelada por um dicionário com os 
# campos saldo, com o saldo devedor da conta, transações, com o número de transações que 
# gerou  esse  saldo,  e  média,  com  a  média  de  gastos  por  transação.  Escreva  uma  função 
# compra, que recebe como parâmetros o dicionário com a conta e o valor da compra e retorna 
# um novo dicionário para aquela conta, com o saldo devedor, número de transações e média de 
# gastos atualizados

# media = valor / gasto total / n de transações
def compra(dic: dict,valor: int) -> dict:
    new = {
        "saldo": dic["saldo"] + valor,
        "transacoes": dic["transacoes"] + 1,
        "media": (dic["saldo"] + valor) / (dic["transacoes"] + 1)
    }
    return new


conta_cartao = {
    "saldo": 500,
    "transacoes": 5,
    "media": 100
}

print(compra(conta_cartao,200))
