import oracledb


class inserir_registros:

    def conexao_local_host():
        try:
            return oracledb.connect(user='system',password='mcds123',dsn='system@//localhost:1521/xe')
        except:
            return f'Falha de conexão com o banco de dados local!!!'
        
    def inserir_tb_uf():
        with open('estados_uf.txt','r') as estados:
            connection = inserir_registros.conexao_local_host()
            registros = estados.readlines()
            for i in registros:
                i = i.replace('\n','').split(',')
                print(i)    
                sql = """INSERT INTO TB_UF (SIGLA_UF, COD_IBGE ,ESTADO ,REGIAO)  
                            VALUES (:SIGLA_UF, :COD_IBGE ,:ESTADO ,:REGIAO)"""

                cursor = connection.cursor()
                cursor.execute(sql,[i[0],i[1],i[2],i[3]])
                connection.commit()

    def inserir_tb_municipio():
        with open('municipios.txt','r') as municipio:
            connection = inserir_registros.conexao_local_host()
            registros = municipio.readlines()
            for i in registros:
                i = i.replace('\n','').split(',')
                print(i)    
                sql = """INSERT INTO TB_MUNICIPIO (SIGLA_UF ,COD_IBGE ,MUNICPIO ,LATITUDE ,LONGITUDE)  
                            VALUES (:SIGLA_UF ,:COD_IBGE ,:MUNICPIO ,:LATITUDE ,:LONGITUDE)"""

                cursor = connection.cursor()
                cursor.execute(sql,[i[0],i[1],i[2],i[3],i[4]])
                connection.commit()

    def inserir_tb_cidade():
        with open('cidades.csv','r',encoding='UTF-8') as cidade:
            connection = inserir_registros.conexao_local_host()
            registros = cidade.readlines()
            for i in registros:
                i = i.replace('\n','').split(';')
                print(i)    
                sql = """INSERT INTO TB_CIDADE (COD_IBGE,SIGLA_UF, CIDADE,CIDADE_AREA)  
                            VALUES (:COD_IBGE,:SIGLA_UF,:CIDADE,:CIDADE_AREA)"""

                cursor = connection.cursor()
                cursor.execute(sql,[float(i[2]),i[1],i[0],float(i[3])])
                connection.commit()

"""
    def inserir_tb_bairro():
        with open('informacoes_bairros_logradouros.csv','r',encoding='UTF-8') as bairro:
            connection = inserir_registros.conexao_local_host()
            csv = bairro.readlines()
            for i in csv:
                i = i.replace('\n','').split(';')
                sql = INSERT INTO TB_BAIRRO (SIGLA_UF,BAIRRO,CIDADE,CEP,CIDADE_IBGE,LATITUDE,LONGITUDE,CIDADE_AREA)
                            VALUES (:SIGLA_UF,:BAIRRO,:CIDADE,:CEP,:CIDADE_IBGE,:LATITUDE,:LONGITUDE,:CIDADE_AREA)
                
                cursor = connection.cursor()
                cursor.execute(sql,[i[4],i[2],i[3],i[0],float(i[7]),i[5],i[6],float(i[8])])
                connection.commit()
                print(f'{i[4]},{i[2]},{i[3]},{i[0]},{i[7]},{i[5]},{i[6]},{i[8]}')
"""                
           
#inserir_registros.inserir_tb_uf()
#inserir_registros.inserir_tb_municipio()
#inserir_registros.inserir_tb_bairro()

inserir_registros.inserir_tb_cidade()

