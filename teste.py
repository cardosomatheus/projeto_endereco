import requests

link = "https://viacep.com.br/ws/33822125/json/"
endereco = requests.get("https://viacep.com.br/ws/RS/Porto Alegre/Domingos/json/")
print(endereco)


