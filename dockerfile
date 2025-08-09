# Imagem lite do DATABASE ORACLE
FROM container-registry.oracle.com/database/free:latest-lite


# Copia o arquivo .sql para ser executado no container
COPY ./home/oracle/myScripts /opt/oracle/scripts/startup

# Define variáveis de ambiente (opcional, pode sobrescrever no `docker run`)
ENV ORACLE_PDB=FREEPDB1
ENV ORACLE_PWD=mcds123
ENV ENABLE_ARCHIVELOG=true
ENV ENABLE_FORCE_LOGGING=true

# Volume do banco
VOLUME /opt/oracle/oradata

# Expondo a porta padrão do Oracle
EXPOSE 1521
