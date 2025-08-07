from rsc.scripts.estados import Estados
from rsc.scripts.cidade import Cidade
from rsc.scripts.endereco import Endereco
from rsc.scripts.moradores import Moradores


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