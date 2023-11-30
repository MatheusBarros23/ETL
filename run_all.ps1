# Copiar o arquivo kaggle.json para o diretório .kaggle
Copy-Item -Path .\kaggle.json -Destination C:\Users\mathe\.kaggle

$venvPath = ".\venv\Scripts\Activate"

# Ativar a virtual environment
if (Test-Path $venvPath) {
    & $venvPath
} else {
    Write-Host "A virtual environment não foi encontrada. Por favor, ajuste o caminho."
}

# Copiar o arquivo kaggle.json para o diretório .kaggle
Copy-Item -Path .\kaggle.json -Destination C:\Users\mathe\.kaggle

# Executar o script Python
python .\jobs_etl\job_1.py

# Criar um contêiner PostgreSQL
docker run --name postgres_container -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 postgres:latest

# Aguardar por 5 segundos
Start-Sleep -Seconds 8

# Executar um comando dentro do contêiner PostgreSQL para criar um banco de dados
docker exec -it postgres_container psql -U postgres -c "CREATE DATABASE `"postgres_container`";"

# Conectar-se ao PostgreSQL
psql -U postgres

# Criar o banco de dados "postgres_container"
CREATE DATABASE "postgres_container";

# Aguardar por 5 segundos
Start-Sleep -Seconds 8

# Executar o script Python
python .\jobs_etl\job_2.py

# Executar o contêiner Metabase
docker run -d -p 3000:3000 --name metabase metabase/metabase