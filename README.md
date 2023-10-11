| insert: Kaggle rest api instructions,  Docker instructions

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

After completing these steps, you should have a PostgreSQL container running with a database named "postgres-container" and a Metabase container running, accessible at `http://localhost:3000`. You can proceed to set up Metabase using its web interface and connect it to the PostgreSQL database you created.
