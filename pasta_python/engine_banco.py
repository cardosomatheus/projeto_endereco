import oracledb


conexao  = oracledb.connect(user="userhr", password='mcds123',
                              host="localhost", port=1521, service_name="XEPDB1")



with conexao.cursor() as conn:
    sql = 'select * from tb_moradores'
    for linha in conn.execute(sql):
        print('linha', linha)