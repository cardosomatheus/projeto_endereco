from  sqlalchemy import create_engine, engine
import oracledb


connect = engine.url.URL.create(
    "oracle+oracledb",
    username='userhr',
    password='mcds123',
    host='localhost',
    port=1521,
    database='',
    query=dict(service_name='XPDB1')
)

engine = create_engine(engine)

