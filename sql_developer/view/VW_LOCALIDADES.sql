CREATE OR REPLACE VIEW VW_LOCALIDADES AS 
select 
    A.BAIRRO,
    A.CEP,
    A.LATITUDE,
    A.LONGITUDE,
    B.ESTADO||'-'||A.SIGLA_UF ESTADO_UF,
    B.COD_IBGE IBGE_UF,
    B.REGIAO,
    C.COD_IBGE IBGE_CIDADE,
    C.CIDADE,
    C.CIDADE_AREA,
    D.LOGRADOURO,
    D.TIPO
FROM TB_BAIRRO A 
JOIN TB_UF B ON A.SIGLA_UF = B.SIGLA_UF
JOIN TB_CIDADE C ON A.PID_CIDADE = C.PID
JOIN TB_LOGRADOURO D ON C.PID = D.PID_CIDADE;