#   Bibliotecas
import requests
from database import conexao_bd
from oracledb import IntegrityError


class Estados:
    """ Classe de Estados """
    def __init__(self) -> None:
        self.conexao = conexao_bd()


    def estados_brasileiros(self) -> None:
        """ Esse metodo tenta iserir todas as UFs  brasileiras do endpoint."""
        uf_json = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados').json()
        sql_insercao_uf  = """INSERT 
                                INTO USERADDRESS.TB_UF (UF,     
                                                    COD_IBGE,
                                                    NOME,
                                                    REGIAO)
                               VALUES (:UF,
                                       :COD_IBGE,
                                       :NOME,
                                       :REGIAO)
                            """

        
        """ Insere as UFs do json, uma por uma."""
        with self.conexao.cursor() as conn:
            for uf in uf_json:
                try: 
                    conn.execute(sql_insercao_uf, 
                                [uf["sigla"],
                                uf["id"],
                                uf["nome"],
                                uf["regiao"]["nome"]]
                                )
                    self.conexao.commit()
                    
                except IntegrityError as e:
                    """ Contraint unica de UF, tratemento de exceção para isso. """ 
                    if e.args[0].code == 1:  
                        continue                   
                    print(e)
                           
                except Exception as e:
                    print(f'Não foi possivel inserir a uf:  {uf["sigla"]}')
                    continue

                



ufs = Estados()

ufs.estados_brasileiros()






    
    
