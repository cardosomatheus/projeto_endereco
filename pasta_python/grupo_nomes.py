import pandas as pd
from random import randint
from datetime import date, datetime, timedelta
from engine_banco import engine

class Moradores:
    def __init__(self):
        self.__menor_data = date.today().replace(year = date.today().year - 80)
        self.__maior_data = date.today().replace(year = date.today().year - 18)


    def inserindo_moradores(self, dataframe):
        try:
            tamanho_df_separado = 100
            dados_dividos = [dataframe.to_dict('records')[i:i +tamanho_df_separado] for i in range (0,dataframe.shape[0],tamanho_df_separado)]
            with engine.connect() as conn:
                for divisao_dados in dados_dividos:
                    conn.execute(
                        '''INSERT INTO TB_CLIENTES (NOME,GENERO,DATA_NASCIMENTO) 
                                        VALUES (:NOME, :GENERO, :DATA_NASCIMENTO)''', divisao_dados
                    )
                    conn.execute('COMMIT')
        except Exception as error:
            print('falha na inserção',error)    


    def lendo_arquivo(self):
        dados = pd.read_csv('pasta_python/grupos.csv')
        return self.seleciona_campos(dataframe = dados)
    
    @property
    def data_nascimento(self):
        diferenca_entre_datas  = self.__maior_data - self.__menor_data
        dias_aleatorio = randint(0, diferenca_entre_datas.days)
        return self.__menor_data + timedelta(days=dias_aleatorio)
       

    def seleciona_campos(self, dataframe):
        dataframe = dataframe[['name','classification']]
        dataframe = dataframe.dropna(subset=['name','classification'])
        dataframe['data_nascimento'] = 0
        dataframe['data_nascimento'] = pd.to_datetime(dataframe['data_nascimento'].apply(lambda x: self.data_nascimento))
        dataframe['name']            = dataframe['name'].astype(dtype='string')
        dataframe['classification']  = dataframe['classification'].astype(dtype='string')
        return dataframe


moradores = Moradores()
print(moradores.lendo_arquivo())