from estados import Estados
from cidade import Cidade
from endereco import Endereco
from moradores import Moradores


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