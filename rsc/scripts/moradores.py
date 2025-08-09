#   Bibliotecas
# Bibliotecas
from random import randrange
from datetime import date, timedelta
from database import conexao_bd
from faker import Faker
from oracledb import IntegrityError
    
class Moradores:
    """Classe para geração e carga de moradores no banco de dados."""

    def __init__(self):
        """Inicializa a conexão com o banco e o gerador de dados Faker."""
        self._faker = Faker('pt_BR')
        self.conexao = conexao_bd()
    
    
    def carga_moradores(self, quantidade: int = 1000):       
        """Insere no banco moradores gerados aleatoriamente."""
        vsql  = """ INSERT 
                        INTO USERADDRESS.TB_MORADORES (NOME, DOCUMENTO, DATA_NASCIMENTO)
                      VALUES (:NOME, :DOCUMENTO, :DATA_NASCIMENTO)
                """            
        with self.conexao.cursor() as conn:
            for valor in self.gera_moradores().values():
                try:
                    conn.execute(vsql,
                                (valor.get('nome'),
                                 valor.get('cep'),
                                 valor.get('data_nascimento')))
                    self.conexao.commit()
                except IntegrityError as e:
                    if e.args[0].code == 1:  
                        continue                   
                    print(e)
                except Exception as e:
                    print(f'Não foi possível inserir o morador: {valor}')
                    continue
            self.conexao.commit()
    
    
    def gera_data_nascimento(self):
        """Gera uma data de nascimento aleatória entre 50 e 80 anos atrás."""
        menor_data_nascimento_permitida = date.today().replace(year=date.today().year - 80)
        maior_data_nascimento_permitada = date.today().replace(year=date.today().year - 50)
        delta = maior_data_nascimento_permitada - menor_data_nascimento_permitida
        delta_inteiro = (delta.days * 24 * 60 * 60) + delta.seconds
        qtd_segundos_aleatorios = randrange(delta_inteiro)
        return maior_data_nascimento_permitada + timedelta(seconds=qtd_segundos_aleatorios)


    def gera_moradores(self, quantidade: int = 1000) -> dict:
        """Gera um dicionário com nomes, documentos e datas de nascimento."""
        if not isinstance(quantidade, int):
            raise Exception('O valor deve ser inteiro.')
        if quantidade <= 1:
            return 'O valor deve ser maior que 1.'
        
        contador = 0
        dict_moradores = {}
        while contador <= quantidade:
            dict_morador = {
                'nome': self._faker.name(),
                'cep': self._faker.cpf(),
                'data_nascimento': self.gera_data_nascimento()
            }
            contador += 1
            dict_moradores[contador] = dict_morador
        return dict_moradores

              
        
        


morador = Moradores()
morador.carga_moradores(0)