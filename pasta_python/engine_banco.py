from  sqlalchemy import create_engine, engine, text
import oracledb


connect = engine.url.URL.create(
    "oracle+oracledb",
    username='userhr',
    password='mcds123',
    host='localhost',
    port=1521,
    database='',
    query=dict(service_name='XEPDB1')
)

engine = create_engine(connect, echo=True)



#with engine.connect() as conn:
#    sql = 'select sysdate from dual'
#    for linha in conn.execute(text(sql)):
#        print(linha)