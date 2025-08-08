import pandas as pd 
from database import conexao_bd

class Cidade:
    def __init__(self):
        self.conexao = conexao_bd()
        

    def busca_cidades(self) -> pd.DataFrame:
        """ Busca os valores contidos no arquivo json e retorna em formato Dataframe"""
        try:
            dtype = {
                    'nome': 'object',
                    'estado': 'object',
                    'cod_ibge': 'object',
                    'area':'float64'
                }
            
            arquivo_csv =  'rsc/files/cidades.csv'
            dados = pd.read_csv(arquivo_csv, delimiter=';', dtype=dtype)
            dados.rename(columns={'estado': 'uf',},inplace=True)
            return dados
        except Exception as e:
            print('Erro no processo de buscar o arquivo de cidade.!!!')    
            print(e)


    def carga_cidades(self) -> None:  
        """ Realiza carga das cidades contida no Dataframe da mil em mil."""      
       
        dataframe = self.busca_cidades()
        valor_de_separacao = 1000
        dados_em_1000  = [dataframe.to_dict('records')
                         [tamanho:tamanho+valor_de_separacao] 
                         for tamanho in range(0, dataframe.shape[0], valor_de_separacao)
                        ]
        
        with self.conexao.cursor() as conn:
            insercao_sql  = """ INSERT 
                                    INTO USERADDRESS.TB_CIDADE (COD_IBGE,
                                                                NOME,
                                                                UF,
                                                                AREA)
                                 VALUES (:COD_IBGE,
                                         :NOME,
                                         :UF,
                                         :AREA)
                            """ 


            for dados_divididos in dados_em_1000:
                conn.executemany(insercao_sql, dados_divididos, batcherrors=True)
        print('Processo de carga de Cidades finalizado!!!')

                    

