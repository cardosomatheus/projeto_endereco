import pandas as pd 
from engine_banco import conexao

class Cidade:
    def __init__(self):
        self.__arquivo_csv =  'pasta_python/cidades.csv'
        
    def inserindo_cidades(self, dataframe):
        with conexao.cursor() as conn:
            cuncksize = 1000
            dados_em_1000 = [dataframe.to_dict('records')[i:i+cuncksize] for i in range(0, dataframe.shape[0], cuncksize)]
            insercao_sql  = """ INSERT INTO TB_CIDADE (P_CIDADE,COD_IBGE,CIDADE,F_UF,CIDADE_AREA)
                                    VALUES (SQ_CIDADE.NEXTVAL,:COD_IBGE,:CIDADE,:F_UF,:CIDADE_AREA)"""
            
            for dados_divididos in dados_em_1000:
                conn.executemany(insercao_sql,dados_divididos)
                conexao.commit()

            
    def lendo_arquivo(self):
        dados = pd.read_csv(self.__arquivo_csv, delimiter=';')
        dados.rename(columns={'nome':'cidade', 'estado': 'f_uf', 'area':'cidade_area'}, inplace=True)
        dados = dados[['cod_ibge','cidade','f_uf','cidade_area']]
        return dados
    
    


    