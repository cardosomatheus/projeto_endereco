#   Bibliotecas
import requests
from geopy.geocoders import Nominatim

#   Classes
class Estados_Municipios_Brasileiros:
    def __init__(self):
        self.requisicao_uf = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados')
        self.link_municipio = f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{self.id_estados()}/microrregioes'
        self.requisicao_mun = requests.get(self.link_municipio)


    def informacoes_estados_txt(self):
        # Retorna cod_ibge,sigla_uf,estado e regiao de todos os estados do Brasil escritos em TXT
        with open ('estados_uf.txt','w') as uf:
            for estado in self.requisicao_uf.json():
                cod_ibge,sigla_uf,nome_uf,regiao = estado["id"],estado["sigla"],estado["nome"],estado["regiao"]["nome"]

                # o print e escrita das informações dos estados brasileiros
                print(f'{sigla_uf},{cod_ibge},{nome_uf},{regiao}')
                uf.write(f'{sigla_uf},{cod_ibge},{nome_uf},{regiao}\n')


    def id_estados(self):
        # retorna todos os ID dos estados brasileiros na variavel id_estados
        id_estados = ''
        for estado in self.requisicao_uf.json():
            id_estados += f'{estado["id"]}|'
        return id_estados[:-1]   
    
    
    def municpios_por_estado(self):
        # retorna um txt com sigla_uf,cod_ibge,nome_municpio,localidade dos muicipios
        with open('municipios.txt','w') as municpios_txt:
            for municipio in self.requisicao_mun.json():
                sigla_uf = f'{municipio["mesorregiao"]["UF"]["sigla"]}'
                cod_ibge,nome_municpio = municipio['id'], municipio['nome']
    
                try:
                    # Faz a busca através do sigla_uf, cod_ibge, nome_municpio retornada em dict
                    geolocator = Nominatim(user_agent="test_app")
                    location = geolocator.geocode(f'{sigla_uf}, {cod_ibge}, {nome_municpio}')
                    latitude, longitude= location.latitude, location.longitude  

                    # o print e escrita das informações dos estados brasileiros
                    print(f'{sigla_uf},{cod_ibge},{nome_municpio},{latitude},{longitude}')
                    municpios_txt.write(f'{sigla_uf},{cod_ibge},{nome_municpio},{latitude},{longitude}\n') 
                except: 
                    # Em caso de error ele passa o municipio e não insere o arquivo txt
                    pass
    

estados = Estados_Municipios_Brasileiros ()       
estados.informacoes_estados_txt()
estados.municpios_por_estado()
