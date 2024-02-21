from random import randint
import requests
from geopy.geocoders import Nominatim
import pycep_correios



class Endereco:
    def __init__(self, cep):
        self.url = requests.get(f"https://viacep.com.br/ws/{cep}/json").json()


def validacao_ceps_csv():
    # Alterar a validação para regex
    """CEP do arquivo csv e confirma tem 9 caracteres e retira as quebras de linhas"""
    lista_cep = []
    with open('ceps_separados.csv', 'r') as ceps:
        for linha in ceps.readlines():
            if len(linha) == 9:
                lista_cep.append(linha.replace('\n',''))
    return lista_cep[randint(0,len(lista_cep))]




ed = Endereco('33822-125')
print(ed.url)