> **INSERT**: Kaggle rest api instructions,  Docker instructions

# Setting Up PostgreSQL and Metabase Containers with Docker

This guide will walk you through the process of setting up PostgreSQL and Metabase containers using Docker on your system.

## Prerequisites

- Docker Desktop
- Windows Subsystem for Linux 2 (WSL2)

## Step 1: Pull and Run the PostgreSQL Container

```bash
# Pull the PostgreSQL Docker image if you haven't already
docker pull postgres:latest

# Run the PostgreSQL container with a specified name, password, and port mapping
docker run --name postgres-container -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 postgres:latest
```

This step pulls the PostgreSQL Docker image and runs a container with the name "postgres-container," sets the PostgreSQL password to "mysecretpassword," and maps port 5432 from the container to port 5432 on your host.

## Step 2: Enter the PostgreSQL Container and Create a Database

```bash
# Enter the PostgreSQL container's bash shell
docker exec -it postgres-container bash

# Connect to PostgreSQL with the "postgres" user
psql -U postgres

# Create a database named "postgres-container"
CREATE DATABASE "postgres-container";
```

This step enters the PostgreSQL container's bash shell, connects to PostgreSQL as the "postgres" user, and creates a database named "postgres-container."

## Step 3: Pull and Run the Metabase Container

```bash
# Pull the Metabase Docker image if you haven't already
docker pull metabase/metabase:latest

# Run the Metabase container with port mapping
docker run -d -p 3000:3000 --name metabase metabase/metabase
```

This step pulls the Metabase Docker image and runs a container named "metabase" with port 3000 of the container mapped to port 3000 on your host.

## Step 4: View Metabase Logs

```bash
# View Metabase container logs
docker logs -f metabase
```

This step allows you to view the Metabase container's logs to check the status and access information for Metabase.

Criar um tópico no README para explicar a execução do `run_all.ps1` é uma excelente ideia para fornecer instruções claras aos usuários do seu projeto. Aqui está um exemplo de como você pode estruturar esse tópico:

## Executando o Script `run_all.ps1`

O script `run_all.ps1` é projetado para automatizar a execução de várias tarefas relacionadas ao projeto. Siga as instruções abaixo para executar o script com sucesso.

### Pré-requisitos

Antes de executar o script, certifique-se de ter o seguinte instalado:

- [PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell)

### Passos para Execução

1. **Clone o Repositório:**
   ```bash
   git clone https://github.com/seu-usuario/seu-projeto.git
   cd seu-projeto
   ```

2. **Abra o PowerShell:**
   - Pressione `Win + X` e escolha "PowerShell" no menu.

3. **Configuração de Execução:**
   - Execute o comando abaixo para configurar a execução de scripts não assinados:
     ```powershell
     Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
     ```

4. **Execute o Script:**
   - Navegue até o diretório do projeto e execute o script `run_all.ps1`:
     ```powershell
     .\run_all.ps1
     ```

5. **Acompanhe a Execução:**
   - O script exibirá informações sobre o progresso e quaisquer mensagens de erro.

6. **Concluído:**
   - Após a conclusão, pode esperar +- 10 segundos e poderá acessar o metabase em `http://localhost:3000`.

### Observações Adicionais

- Certifique-se de revisar e personalizar as configurações no script antes da execução, se necessário.
- Se necessário, você pode ajustar as permissões de execução do PowerShell para restringir ou permitir a execução de scripts.
- Se durante a execução do script você encontrar mensagens de erro relacionadas ao psql, como "psql : O termo 'psql' não é reconhecido como nome de cmdlet", pode ignorá-las. Esses erros podem ocorrer devido a configurações específicas do ambiente e geralmente não afetam a funcionalidade do script.

Ao seguir essas instruções, os usuários do seu projeto terão um guia claro sobre como executar o script `run_all.ps1` e quaisquer considerações adicionais que possam ser relevantes para a configuração ou execução bem-sucedida do projeto.

After completing these steps, you should have a PostgreSQL container running with a database named "postgres-container" and a Metabase container running, accessible at `http://localhost:3000`. You can proceed to set up Metabase using its web interface and connect it to the PostgreSQL database you created.
