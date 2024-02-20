import pandas as pd
from random import randint
from datetime import date, datetime, timedelta, time
from sqlalchemy import Table, Column, MetaData, String, Integer, Date, insert, Sequence
from engine_banco import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from engine_banco import engine

    
class Moradores:
    def __init__(self):
        self.__menor_data = date.today().replace(year = date.today().year - 80)
        self.__maior_data = date.today().replace(year = date.today().year - 18)

    
    def inserindo_moradores(self, dataframe):
        tb_morador = Table('tb_moradores',
                MetaData(),
#                Column("p_morador", Integer,Sequence('SQ_MORADORES'), primary_key=True),
                Column("nome", String(100)),
                Column("genero", String(1)),
                Column("data_nascimento", Date)
            )
        with engine.connect() as conn:
            for  row in dataframe.to_dict('records'):
                insert_stmt = insert(tb_morador).values(row)
                conn.execute(insert_stmt, row)
                print(insert_stmt)
                #print(row)
            



    def lendo_arquivo(self):
        dados = pd.read_csv('pasta_python/grupos.csv')
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


#if __name__ == '__main__': 
moradores = Moradores()
dataframe = moradores.lendo_arquivo()
moradores.inserindo_moradores(dataframe=dataframe)


from sqlalchemy import create_engine
from sqlalchemy import inspect


#insp = inspect(engine)
#print(insp.get_table_names())