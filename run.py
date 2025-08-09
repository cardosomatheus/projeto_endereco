from rsc.scripts.estados import Estados
from rsc.scripts.cidade import Cidade
from rsc.scripts.endereco import Endereco
from rsc.scripts.moradores import Moradores


def main():
    """Execulta todo o processo via python."""
    print('Inserindo estados...')
    estados = Estados()
    estados.carga_estados_brasileiros()

    print('Inserindo cidades...')
    cidade = Cidade()
    cidade.carga_cidades()

    print('Inserindo enderecos...')          
    endereco = Endereco()
    endereco.carga_enderecos()
  
    print('Inserindo moradores...')
    moradores = Moradores()
    moradores.carga_moradores(100)



if __name__ == '__main__':
    main()