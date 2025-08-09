#   Bibliotecas
import requests
from .database import conexao_bd 
from oracledb import IntegrityError


class Estados:
    """Classe para manipulação de dados das UFs brasileiras."""

    def __init__(self) -> None:
        """Inicializa a conexão com o banco de dados."""
        self.conexao = conexao_bd()


    def busca_ufs(self):
        """Busca a lista de UFs brasileiras na API do IBGE."""
        ufs = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados')
        if ufs.status_code == 200:
            return ufs.json()
        raise Exception('Falha ao buscar as UFs do endpoint')


    def carga_estados_brasileiros(self) -> None:
        """Insere todas as UFs brasileiras obtidas da API do IBGE no banco."""
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
        uf_json = self.busca_ufs()

        with self.conexao.cursor() as conn:
            for uf in uf_json:
                try: 
                    conn.execute(sql_insercao_uf, 
                                [uf["sigla"],uf["id"],uf["nome"],
                                 uf["regiao"]["nome"]])
                    self.conexao.commit()
                except IntegrityError as e:
                    if e.args[0].code == 1:  
                        continue                   
                    print(e)
                except Exception as e:
                    print(f'Não foi possivel inserir a UF: {uf["sigla"]}')
                    continue
            self.conexao.commit()
        print('Processo de carga de UFs finalizado!!!')

