CREATE OR REPLACE FUNCTION FNC_INSERIR_CEP_LOGRADOURO (PCEP_INDEX NUMBER)
RETURN VARCHAR2 IS
    VCEP VARCHAR2(9);
BEGIN
    SELECT CEP INTO VCEP FROM TB_LOGRADOURO WHERE PID = PCEP_INDEX;
    
   RETURN VCEP;
END;
/


