CREATE OR REPLACE FUNCTION FNC_FK_PID_CIDADE (PNOME_CIDADE VARCHAR2)
RETURN NUMBER IS
 VPID_CIDADE NUMBER;
BEGIN
    SELECT PID INTO VPID_CIDADE FROM TB_CIDADE WHERE CIDADE = PNOME_CIDADE;
    RETURN VPID_CIDADE;
END;
/