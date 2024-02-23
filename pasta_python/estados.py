#   Bibliotecas
import requests
from engine_banco import conexao
from geopy.geocoders import Nominatim




class Estados:
    def __init__(self) -> None:
        self.__uf_json = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados').json()
        

    def estados_brasileiros(self):
        with conexao.cursor() as conn:
            for estado in self.__uf_json:
                cod_ibge = estado["id"]
                sigla_uf = estado["sigla"] 
                nome_uf  = estado["nome"]
                regiao   = estado["regiao"]["nome"]

                insercao_sql  = """ INSERT INTO TB_UF (P_UF, COD_IBGE, ESTADO, REGIAO)
                                        VALUES (:P_UF, :COD_IBGE, :ESTADO, :REGIAO)"""

                conn.execute(insercao_sql, [sigla_uf,cod_ibge,nome_uf,regiao])
                conexao.commit()

    
    
