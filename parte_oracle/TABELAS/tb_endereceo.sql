﻿CREATE TABLE TB_ENDERECO(	
    P_CEP VARCHAR2(10) NOT NULL, 
	F_UF VARCHAR2(2) NOT NULL, 
	F_CIDADE NUMBER NOT NULL, 
	BAIRRO VARCHAR2(200), 
	RUA VARCHAR2(400), 
    CONSTRAINT PK_ENDERECO PRIMARY KEY (P_CEP),
    CONSTRAINT FK_ENDERECO_UF FOREIGN KEY (F_UF) REFERENCES TB_UF (P_UF) , 
    CONSTRAINT FK_ENDERECO_CIDADE FOREIGN KEY (F_CIDADE) REFERENCES TB_CIDADE (P_CIDADE) 
);