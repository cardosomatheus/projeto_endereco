import oracledb


conexao  = oracledb.connect(user="userhr", password='mcds123',
                              host="localhost", port=1521, service_name="XEPDB1")
