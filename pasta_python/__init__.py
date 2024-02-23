from estados import Estados
from cidade import Cidade
from endereco import Endereco
from moradores import Moradores


if __name__ == '__main__':
    #print('Inserindo estados...')
    #estados = Estados()
    #estados.estados_brasileiros() 

    #print('Inserindo cidades...')
    #cidade = Cidade()
    #cidade.inserindo_cidades(dataframe=cidade.lendo_arquivo())

    #print('Inserindo enderecos...')          
    #endereco = Endereco()
    #endereco.inserindo_endereco(dataframe=endereco.endereco())
    
    print('Inserindo moradores...')
    moradores = Moradores()
    moradores.inserindo_moradores(dataframe=moradores.lendo_arquivo())