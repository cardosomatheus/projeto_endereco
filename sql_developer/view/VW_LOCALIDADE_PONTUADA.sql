CREATE OR REPLACE VIEW VW_LOCALIDADE_PONTUADA AS 
SELECT 
    B.SIGLA_UF,
    B.ESTADO,
    B.REGIAO,
    D.CIDADE,
    A.BAIRRO,
    A.CEP,
    SDO_GEOMETRY(2001,8307,sdo_point_type(A.LATITUDE,A.longitude, NULL), NULL, NULL) GEOMETRIA,   
    C.LOGRADOURO,
    C.TIPO,
    D.COD_IBGE
FROM TB_BAIRRO A
JOIN TB_UF B ON A.SIGLA_UF = B.SIGLA_UF 
JOIN TB_LOGRADOURO C ON A.CEP = C.CEP
JOIN TB_CIDADE D ON D.PID = C.PID_CIDADE;
