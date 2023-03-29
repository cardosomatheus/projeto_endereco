from random import randint


def nome_masculino():
    with open('nomes_masculinos.txt') as arq:
        return arq.readlines()[randint(0,99)]        
    
def nome_feminino():
    with open('nomes_femininos.txt') as arq:
        return arq.readlines()[randint(0,99)]  
    
def sobrenome():
    with open('sobrenomes.txt') as arq:
        return arq.readlines()[randint(0,27)]  
    
    
print(nome_masculino(),nome_feminino(),sobrenome())