import oracledb


def conexao_local_host():
    try:
        return oracledb.connect(user='system',password='mcds123',dsn='system@//localhost:1521/xe')
    except:
        return f'Falha de conexão com o banco de dados local!!!'
    
def inserir_tb_uf():
    with open('estados_uf.txt','r') as estados:
        connection = conexao_local_host()
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
        connection = conexao_local_host()
        registros = municipio.readlines()
        for i in registros:
            i = i.replace('\n','').split(',')
            print(i)    
            sql = """INSERT INTO TB_MUNICIPIO (SIGLA_UF ,COD_IBGE ,MUNICPIO ,LATITUDE ,LONGITUDE)  
                        VALUES (:SIGLA_UF ,:COD_IBGE ,:MUNICPIO ,:LATITUDE ,:LONGITUDE)"""
            cursor = connection.cursor()
            cursor.execute(sql,[i[0],i[1],i[2],i[3],i[4]])
            connection.commit()