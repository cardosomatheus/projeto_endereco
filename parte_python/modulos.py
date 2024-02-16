import requests
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, URL
from sqlalchemy import text
import oracledb

        
objeto_url = URL.create(
    'oracle+oracledb',
    username="system",
    password="mcds123",  
    host="localhost",
    port=1521,
    database='',
    query=dict(service_name= 'xe')
)
engine = create_engine(objeto_url)


sigla_paises = [
    'AF','ZA','AL','DE','AD','AO','AG','SA','DZ','AR','AM','AU','AT','AZ','BS','BD','BB','BH',
    'BY','BE','BZ','BJ','BO','BA','BW','BR','BN','BG','BF','BI','BT','CV','CM','KH','CA','QA','KZ',
    'TD','CL','CN','CY','CO','KM','CG','CI','CR','HR','CU','DK','DJ','DM','EG','SV','AE','EC','ER','SK',
    'SI','ES','US','EE','SZ','ET','FJ','PH','FI','FR','GA','GM','GH','GE','GD','GR','GT','GY','GN','GQ',
    'GW','HT','NL','HN','HU','YE','MH','SB','IN','ID','IR','IQ','IE','IS','IL','IT','JM','JP','JO','KI',
    'KW','LA','LS','LV','LB','LR','LY','LI','LT','LU','MK','MG','MY','MW','MV','ML','MT','MA','MU','MR',
    'MX','MM','FM','MZ','MD','MC','MN','ME','NA','NR','NP','NI','NE','NG','NO','NZ','OM','PW','PA','PG',
    'PK','PY','PE','PL','PT','KE','KG','GB','CF','KR','CD','DO','KP','CZ','RO','RW','RU','WS','SM','LC',
    'KN','ST','VC','SC','SN','SL','RS','SG','SY','SO','LK','SD','SS','SE','CH','SR','TJ','TH','TZ','TL',
    'TG','TO','TT','TN','TM','TR','TV','UA','UG','UY','UZ','VU','VE','VN','ZM','ZW'
]

with engine.connect() as  conn:
    sql = 'select sysdate from dual'
    for row in  conn.execute(text(sql)):
        print(row)
        

