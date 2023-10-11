import subprocess

def run_postgres_container():
    postgres_command = [
        'docker', 'run', '--name', 'postgres-container',
        '-e', 'POSTGRES_PASSWORD=mysecretpassword',
        '-d', '-p', '5432:5432', 'postgres:latest'
    ]

    # Run the PostgreSQL container
    subprocess.run(postgres_command)
    # Enter the PostgreSQL container's bash shell
    enter_container_command = [
      #  'docker', 'exec', '-it', 'postgres-container', 'bash'
    ]
    # Connect to PostgreSQL with the "postgres" user
    psql_command = [
      #  'psql', '-U', 'postgres'
    ]
    # Create a database named "postgres-container" within the PostgreSQL container
    create_database_command = [
      #  'CREATE DATABASE "postgres-container";'
    ]

    # Run the commands within the PostgreSQL container's shell
    subprocess.run(enter_container_command)
    subprocess.run(psql_command)
    subprocess.run(create_database_command)
    subprocess.run(postgres_command)

def run_metabase_container():
    metabase_command = [
        'docker', 'run', '-d', '-p', '3000:3000',
        '--name', 'metabase', 'metabase/metabase:latest'
    ]
    subprocess.run(metabase_command)