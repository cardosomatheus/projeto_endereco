import oracledb
import os
from dotenv import load_dotenv
load_dotenv()


def conexao_bd():
    """ Retorna a conexao com o BD oracle Atraves da variaveis 
        de ambientes configuradas 
    """
    #print(os.getenv("PWD_DATABASE"))
    #print(os.getenv("HOST_DATABASE"))
    #print(os.getenv("PORT_DATABASE"))
    #print(os.getenv("DATABASE"))
    #print(os.getenv("USER_DATABASE"))    
       
    return oracledb.connect(
        user=os.getenv("USER_DATABASE"),
        password=os.getenv("PWD_DATABASE"),
        host=os.getenv("HOST_DATABASE"),
        port=os.getenv("PORT_DATABASE"),
        service_name=os.getenv("DATABASE")
    )
    

