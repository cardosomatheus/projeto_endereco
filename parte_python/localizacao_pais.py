from pais import Paises
from modulos import declarative_base, sessionmaker, Column, String, Integer, ForeignKey, engine



Base = declarative_base() 
Session = sessionmaker(bind=engine)
session = Session()


class Localizacao(Base):
    __tablename__ = 'tb_localizacao'
    
    id         = Column(Integer, primary_key=True)
    regiao     = Column(String(100))
    sub_regiao = Column(String(100))
    regiao_intermediaria = Column(String(100))


    def __repr__(self):
        return f'localizacao(id= {self.id}, regiao = {self.regiao}, sub_regiao= {self.sub_regiao}, regiao_intermediaria= {self.regiao_intermediaria})'


#brasil = Paises('BR')
#print(brasil.localizacao_pais)

        
Base.metadata.create_all(engine)