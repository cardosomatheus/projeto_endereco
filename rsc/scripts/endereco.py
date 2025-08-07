import requests
import pandas as pd
from rsc.scripts.database import conexao

class Endereco:
    def __init__(self):
        self.__caminho_arquivo = 'cep.tsv'
        self.__cidades_listadas = dict()


    def inserindo_endereco(self, dataframe):
        dataframe = dataframe.to_dict('records')
        with conexao.cursor() as conn:
            insercao_sql = """ INSERT INTO TB_ENDERECO (P_CEP,F_UF,F_CIDADE,BAIRRO,RUA)
                                    VALUES (:P_CEP,:F_UF,:F_CIDADE,:BAIRRO,:RUA) """
                                    
            conn.executemany(insercao_sql, dataframe)
            conexao.commit()
    
    def endereco(self):
        dados = pd.read_csv(self.__caminho_arquivo, sep='\t')
        dados.rename(columns={'cep':'p_cep','estado':'f_uf'}, inplace=True)
        print('Identificando as Cidades, aguarde um momento...')
        dados['f_cidade']  = dados['cidade'].apply(lambda x: self.identifica_cidade(x))       
        dados.dropna(inplace=True)
        dados['f_cidade']   = dados['f_cidade'].astype('int')
        dados['f_uf']       = dados['f_uf'].apply(lambda x: x[0:2])
        
        return dados[['p_cep','f_uf','f_cidade','bairro','rua']]


    def identifica_cidade(self, nome_cidade:str):
        if "'" in nome_cidade:
            nome_cidade = nome_cidade.replace("'", '')
        
        if nome_cidade in self.__cidades_listadas:
            return self.__cidades_listadas[nome_cidade]
        
        else:        
            sql= f"""SELECT P_CIDADE FROM TB_CIDADE where CIDADE = '{nome_cidade}'""" 
            with conexao.cursor() as conn:
                for consulta_cidade in conn.execute(sql):              
                    if consulta_cidade is not None:
                        self.__cidades_listadas[nome_cidade] = int(consulta_cidade[0])
                        return int(consulta_cidade[0])
                    else:
                        return None
