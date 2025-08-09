# 📍 Projeto Endereço

Este projeto em Python tem como objetivo fornecer informações detalhadas sobre endereços, incluindo unidades federativas (UF), cidades e moradores. Utiliza um banco de dados Oracle e integra-se com a API do IBGE para obter dados atualizados sobre cidades e CEPs.

## 🚀 Funcionalidades

- **Integração com a API do IBGE**: obtém informações atualizadas sobre cidades e CEPs.
- **Armazenamento em Banco de Dados Oracle**: utiliza Oracle para persistência de dados.
- **Processo de Carga de Dados**: script Python para carregar registros no banco de dados.
- **Dockerização**: facilita o ambiente de desenvolvimento e execução.

## 🛠 Tecnologias Utilizadas

- **Python 3**
- **Oracle Database**
- **Docker**
- **API do IBGE**
- **Arquivos CSV**
- **Git**

## 📦 Pré-requisitos

- Docker instalado na máquina.
- Python 3 instalado.
- Conta de usuário com permissões adequadas no banco de dados Oracle.

## ⚙️ Como Executar

### 1. Construir a Imagem Docker

```bash
docker build -t bdoracle_lite .
```

### 2. Rodar o Contêiner Docker
```bash
docker run --name bd -p 1521:1521 bdoracle_lite
```

### 3. Crie o arquivo .env com os valores de conexão ao banco.


### 4. Executar o Processo de Carga de Dados
```bash
python3 run.py
```
