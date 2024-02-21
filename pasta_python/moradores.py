import pandas as pd
from random import randint
from datetime import date, datetime, timedelta, time
from engine_banco import conexao

    
class Moradores:
    def __init__(self):
        self.__menor_data = date.today().replace(year = date.today().year - 80)
        self.__maior_data = date.today().replace(year = date.today().year - 18)
        self.__arquivo_csv = 'pasta_python/grupos.csv'

    
    def inserindo_moradores(self, dataframe):
        print('Iniciando execução do processo de inserção dos dados.')
        with conexao.cursor() as conn:
            cuncksize = 1000
            dados_em_1000 = [dataframe.to_dict('records')[i:i+cuncksize] for i in range(0, dataframe.shape[0], cuncksize)]
            insercao_sql  = """ INSERT INTO TB_MORADORES (P_MORADOR, NOME, GENERO, DATA_NASCIMENTO)
                                    VALUES (SQ_MORADORES.NEXTVAL, :NOME, :GENERO, :DATA_NASCIMENTO)"""
            
            print('INSERINDO OS DADOS: QTD DE DADOS', dataframe.shape[0])
            for dados_divididos in dados_em_1000:
                conn.executemany(insercao_sql,dados_divididos)
                conexao.commit()
            print('INSERÇÃO FINALIZADA.')


    def lendo_arquivo(self):
        dados = pd.read_csv(self.__arquivo_csv)
        return self.seleciona_campos(dataframe = dados)
    
    
    @property
    def data_nascimento(self):
        hora = time(00, 00, 0)
        diferenca_entre_datas  = self.__maior_data - self.__menor_data
        dias_aleatorio = randint(0, diferenca_entre_datas.days)
        data_aleatoria = self.__menor_data + timedelta(days=dias_aleatorio)
        data_combinada =  datetime.combine(data_aleatoria, hora)
        return data_combinada
    

    def seleciona_campos(self, dataframe):
        dataframe.rename(columns={"name": "nome", "classification": "genero"}, inplace=True)
        dataframe = dataframe[['nome','genero']]
        dataframe = dataframe.dropna(subset=['nome','genero'])
        dataframe['data_nascimento'] = 0
        dataframe['data_nascimento'] = pd.to_datetime(dataframe['data_nascimento'].apply(lambda x: self.data_nascimento))
        dataframe['nome']            = dataframe['nome'].astype(dtype='string')
        dataframe['genero']          = dataframe['genero'].astype(dtype='string')
        return dataframe[['nome','genero','data_nascimento']]


if __name__ == '__main__': 
    moradores = Moradores()
    moradores.inserindo_moradores(dataframe=moradores.lendo_arquivo())


