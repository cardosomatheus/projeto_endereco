from random import randint
import requests
from geopy.geocoders import Nominatim
import pycep_correios


def validacao_ceps_csv():
    """Retorna o cep selecionado randomicamente do arquivo csv 
    -- ele confirma se o cep tem 9 caracteres e retira as quebras de linhas"""
    lista_cep = []
    with open('ceps_separados.csv', 'r') as ceps:
        for linha in ceps.readlines():
            if len(linha) == 9:
                lista_cep.append(linha.replace('\n',''))
    return lista_cep[randint(0,len(lista_cep))]


def cep_por_endereco():
    url = f"https://viacep.com.br/ws/{validacao_ceps_csv()}/json"
    r = requests.get(url)
    json = r.json()
    return str(json['cep'])


def endereco_por_completo():
    endereco = pycep_correios.get_address_from_cep(cep_por_endereco())

    geolocator = Nominatim(user_agent="test_app")
    location = geolocator.geocode(endereco['logradouro'] + ", " + endereco['cidade'] + " - " + endereco['bairro'])

    print(endereco)
    print(location.latitude,location.longitude)

print(endereco_por_completo())
