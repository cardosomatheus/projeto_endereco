
CREATE OR REPLACE PROCEDURE SP_INSERIR_CLIENTES(P_NOMES VARCHAR2, P_GENERO VARCHAR2, P_DT_NASCIMENTO DATE) 
AS
    VIDADE NUMBER;
BEGIN 
    VIDADE := TRUNC((MONTHS_BETWEEN(SYSDATE,P_DT_NASCIMENTO))/12);
    INSERT INTO TB_CLIENTES(NOME, GENERO, DATA_NASCIMENTO,IDADE) VALUES (P_NOMES,P_GENERO,P_DT_NASCIMENTO,VIDADE);
    COMMIT;
END;
/
