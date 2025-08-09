1º Cria a imagem. 
 -- docker build -t bdoracle_lite .

2º Roda a imagem 
 --   docker run --name bd -p 1521:1521 bdoracle_lite

3º Execuca o processo de carga dos registros.
python3 run.py


Projeto Endereçospyth
Este é um projeto em Python que visa Trazer informações relacionadas a endereços, como unidades federativas (UF), cidades, endereços e moradores. O projeto utiliza um banco de dados Oracle e integra-se com a API do IBGE para obter informações atualizadas sobre cidades e CEPs. Esse projeto é sobre o meu aprendizado e como posso melhora-lo (refotar) a cada novo aprendizado.

Funcionalidades
O projeto oferece as seguintes funcionalidades:


proj/
│
├── main.py
└── rsc/
    ├── __init__.py
 
    └── scripts/
         ├── __init__.py
         └── estados.py
         ├── database.py
         
