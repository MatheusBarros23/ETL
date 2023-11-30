import pandas as pd
from pathlib2 import Path
from sqlalchemy import create_engine

# CSV file path
csv_file = Path("raw_data/dados_modelo_SC.csv")
# Load data from CSV
df = pd.read_csv(csv_file)

# Extract columns 'Date' and 'Close'
df = df[["Operadora","Codigo_do_Cliente","Razao_Social_do_Cliente","Codigo_do_Associado","Nome_do_Associado","Tipo_de_Associado","Sexo","Data_de_Nascimento","Grupo_Tipo_de_Atendimento","Valor","Data_do_Atendimento","Competencia","CGC_do_Prestador_Local","Nome_do_Prestador_Local","Especialidade_Descricao","Prestador_Local_Proprio","Cidade_do_Prestador_Local","Estado_do_Prestador_Local","Codigo_do_Procedimento","Nome_do_Procedimento","Codigo_do_CID","Qtd_Procedimentos","Cod_do_Grupo_de_Contrato","Plano_Codigo","Plano_Descricao","GUIA","Especialidade_Codigo","Classe_de_procedimento","Grupo_Familiar","CPF_Titular","Carteirinha_Titular","Nome_Titular"]]

# PostgreSQL connection parameters
# Transform data as needed (e.g., data type conversions)
db_host = "localhost"
db_port = "5432"
db_name = "postgres_container"
db_user = "postgres"
db_password = 'mysecretpassword'

# Select the columns you want to load into PostgreSQL
selected_columns = ["Operadora","Codigo_do_Cliente","Razao_Social_do_Cliente","Codigo_do_Associado","Nome_do_Associado","Tipo_de_Associado","Sexo","Data_de_Nascimento","Grupo_Tipo_de_Atendimento","Valor","Data_do_Atendimento","Competencia","CGC_do_Prestador_Local","Nome_do_Prestador_Local","Especialidade_Descricao","Prestador_Local_Proprio","Cidade_do_Prestador_Local","Estado_do_Prestador_Local","Codigo_do_Procedimento","Nome_do_Procedimento","Codigo_do_CID","Qtd_Procedimentos","Cod_do_Grupo_de_Contrato","Plano_Codigo","Plano_Descricao","GUIA","Especialidade_Codigo","Classe_de_procedimento","Grupo_Familiar","CPF_Titular","Carteirinha_Titular","Nome_Titular"]
df = df[selected_columns]

# Establish a connection to the PostgreSQL database
connection = None
try:
    engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
    print(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
    connection = engine.connect()

    # Insert the data into the PostgreSQL table
    df.to_sql("dados_modelo_SC", connection, if_exists="append", index=False)

    print("Data loaded successfully into PostgreSQL.")
except Exception as e:
    print(f"Error: {e}")
finally:
    if connection is not None:
        connection.close()