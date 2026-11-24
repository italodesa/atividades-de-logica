# 3) Escreva  um  programa  para  armazenar  uma  agenda  de  telefones  em  um  dicionário.  Cada 
# pessoa pode ter um ou mais telefones e a chave do dicionário é o nome da pessoa. Seu 
# programa deve ter as seguintes funções:  

# (a) incluirNovoNome – essa função acrescenta um novo nome na agenda, com um ou mais 
# telefones. Ela deve receber como argumentos o nome e os telefones.  

# (b) incluirTelefone – essa função acrescenta um telefone em um nome existente na agenda. 
# Caso o nome não exista na agenda, você deve perguntar se a pessoa deseja incluí-lo. 
# Caso a resposta seja afirmativa, use a função anterior para incluir o novo nome. 
#  
# (c) excluirTelefone – essa função exclui um telefone de uma pessoa que já está na agenda. Se 
# a pessoa tiver apenas um telefone, ela deve ser excluída da agenda. 

# (d) excluirNome – essa função exclui uma pessoa da agenda. 

# (e) consultarTelefone – essa função retorna os telefones de uma pessoa na agenda. 

def procurar_nome(nome,dicionario):
    if dicionario.get(nome) == None:
        return False
    return True

def adicionar_nome(nome,dicionario):
    if not procurar_nome(nome,dicionario):
        dicionario[nome] = []
        return True
    return False

def remover_telefone(nome,dicionario):
    if not dicionario.get(nome):
        print("Esse nome não existe")
        return False
    print(f"Números do {nome}")
    aux = 1
    for i in dicionario[nome]:
        print(f"{aux} - {i}")
        aux += 1
        n = int(input("Qual você deseja excluir? > "))
        dicionario[nome].pop(n-1)
        return True

def remover_nome(nome,dicionario):
    if not procurar_nome(nome,dicionario):
        return False               
    del dicionario[nome]
    return True

def incluir_telefone(nome,telefone,dicionario):
    if not procurar_nome(nome,dicionario):
        op = input("Seu nome não está na agenda, deseja incluilo? (s/n)")
        if op == 's':
            agenda_telefones[nome] = []
        else:
            return
    
    dicionario[nome].append(telefone)
    print("Número adicionado com sucesso")

def consultar_telefone(nome,dicionario):
   
    if not procurar_nome(nome,dicionario):
        print("Esse nome não existe")
        return False
    print(f"Números do {nome}")
    aux = 1
    for i in dicionario[nome]:
        print(f"{aux} - {i}")
        aux += 1
    return True

agenda_telefones = {}

while True:
    print("===== AGENDA TELEFONICA =====")
    print("[ 1 ] Incluir novo nome")
    print("[ 2 ] Incluir novo telefone")
    print("[ 3 ] Excluir telefone")
    print("[ 4 ] Excluir nome")
    print("[ 5 ] Consultar telefone")
    print("[ 6 ] Sair")
    r = int(input("> "))

    match r:
        case 1:
            nome = input("Digite um novo nome para adicionar: ")

            if adicionar_nome(nome,agenda_telefones):
                print("Nome adicionado com sucesso")

        
        case 2:
            nome = input("Digite seu nome: ")
            telefone = int(input("Digite o telefone"))

            if incluir_telefone(nome,telefone,agenda_telefones):
                print("telefone incluido com sucesso")
            
        case 3:
            nome = input("Digite seu nome: ")

            if remover_telefone(nome,agenda_telefones):
                print("Telefone excluido com sucesso")
            
        case 4:
            nome = input("Digite um nome para você excluir: ")
            if remover_nome(nome,agenda_telefones):
                print("Nome excluido com sucesso")

        case 5:
            nome = input("Digite seu nome: ")
            if not consultar_telefone(nome,agenda_telefones):
                print("Nome não encontrado")

        case 6:
            break
        case 0:
            print(agenda_telefones)
        case _:
            print("Digite uma opção valida")