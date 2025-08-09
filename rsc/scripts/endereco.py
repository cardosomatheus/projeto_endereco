import pandas as pd
from cidade import Cidade
from database import conexao_bd

class Endereco:
    """Classe para manipulação e carga de endereços brasileiros."""

    def __init__(self):
        """Inicializa a conexão com o banco e a instância de Cidade."""
        self.conexao = conexao_bd()
        self.cidade = Cidade()


    def busca_enderecos(self) -> pd.DataFrame:
        """Carrega os dados de endereços a partir de um arquivo CSV."""
        try:
            dtype = {
                'CEP': 'object',
                'Cidade': 'object',
                'Bairro': 'object',
                'Logradouro': 'object',
                'UF': 'object',
            }
            arquivo_csv = 'rsc/files/enderecos.csv'
            dados = pd.read_csv(arquivo_csv, delimiter=',', dtype=dtype)
            dados['id_cidade'] = dados['Cidade'].apply(lambda x: self.cidade.get_id_cidade(x)).astype('Int64')
            dados = dados[['CEP', 'UF', 'id_cidade', 'Logradouro']]
            return dados
        except Exception as e:
            raise Exception(f'Erro no processo de buscar o arquivo de endereço.\n{e}')    


    def carga_enderecos(self) -> None:  
        """Insere no banco os endereços do CSV em lotes de 1000 registros."""      
        dataframe = self.busca_enderecos()
        valor_de_separacao = 1000
        dados_em_1000  = [dataframe.to_dict('records')[tamanho:tamanho+valor_de_separacao] 
                          for tamanho in range(0, dataframe.shape[0], valor_de_separacao)]
        
        with self.conexao.cursor() as conn:
            insercao_sql  = """ INSERT 
                                    INTO USERADDRESS.TB_ENDERECO (CEP,
                                                                  UF,
                                                                  ID_CIDADE,
                                                                  LOGRADOURO)
                                 VALUES (:CEP,
                                         :UF,
                                         :ID_CIDADE,
                                         :LOGRADOURO)
                            """ 
            for dados_divididos in dados_em_1000:
                conn.executemany(insercao_sql, dados_divididos, batcherrors=True)
            self.conexao.commit()                
        print('Processo de carga de Endereços finalizado!!!')



#end = Endereco()
#end.carga_enderecos()