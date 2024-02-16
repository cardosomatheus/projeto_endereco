from modulos import requests, sigla_paises


class Paises:
    def __init__(self, sigla_pais):
        self.sigla_pais = sigla_pais
        self._api_pais  = f'https://servicodados.ibge.gov.br/api/v1/paises/{self.sigla_pais}'
        self._dados_json = requests.get(self._api_pais).json()

    @property
    def api_paises(self):
        return self._dados_json 
    
    @property
    def localizacao_pais(self):
        return self.api_paises[0]['localizacao']







