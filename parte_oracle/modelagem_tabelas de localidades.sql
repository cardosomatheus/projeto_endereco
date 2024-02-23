CREATE TABLE TB_UF( 
    P_UF VARCHAR2(2) NOT NULL,
    COD_IBGE VARCHAR2(10) NOT NULL, 
    ESTADO  VARCHAR2(30),
    REGIAO VARCHAR(20),
    CONSTRAINT PK_UF PRIMARY KEY (P_UF)
);


CREATE TABLE TB_CIDADE(
    P_CIDADE NUMBER NOT NULL,
    COD_IBGE NUMBER,
    CIDADE VARCHAR2(100),
    F_UF VARCHAR2(2) NOT NULL,
    CIDADE_AREA NUMBER,
    CONSTRAINT PK_CIDADE PRIMARY KEY (P_CIDADE),
    CONSTRAINT FK_CIDADE_UF FOREIGN KEY(F_UF) REFERENCES TB_UF(P_UF)
);


CREATE TABLE TB_ENDERECO(	
    P_CEP VARCHAR2(10) NOT NULL, 
	F_UF VARCHAR2(2) NOT NULL, 
	F_CIDADE NUMBER NOT NULL, 
	BAIRRO VARCHAR2(200), 
	RUA VARCHAR2(400), 
    CONSTRAINT PK_ENDERECO PRIMARY KEY (P_CEP),
    CONSTRAINT FK_ENDERECO_UF FOREIGN KEY (F_UF) REFERENCES TB_UF (P_UF) , 
    CONSTRAINT FK_ENDERECO_CIDADE FOREIGN KEY (F_CIDADE) REFERENCES TB_CIDADE (P_CIDADE) 
);


-- MORADORES
CREATE TABLE TB_MORADORES(
    P_MORADOR NUMBER NOT NULL,
    NOME VARCHAR2(100),
    GENERO CHAR(1) CHECK (GENERO IN('M','F')),
    DATA_NASCIMENTO DATE,
    CONSTRAINT  PK_MORADOR PRIMARY KEY (P_MORADOR)
);
 
 