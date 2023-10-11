import pandas as pd
from pathlib2 import Path
from sqlalchemy import create_engine

# CSV file path
csv_file = Path("raw_data/World-Stock-Prices-Dataset.csv")

# Load data from CSV
df = pd.read_csv(csv_file)

# Extract columns 'Date' and 'Close'
df = df[['Date', 'Close', 'Brand_Name','Ticker','Industry_Tag', 'Country']]

# PostgreSQL connection parameters
# Transform data as needed (e.g., data type conversions)
db_host = "0.0.0.0"
db_port = "5432"
db_name = "postgres-container"
db_user = "postgres"
db_password = 'mysecretpassword'

# Select the columns you want to load into PostgreSQL
selected_columns = ["Date", "Close",'Brand_Name','Ticker','Industry_Tag', 'Country']  # Adjust column names as needed
df = df[selected_columns]

# Establish a connection to the PostgreSQL database
try:
    engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
    print(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
    connection = engine.connect()

    # Insert the data into the PostgreSQL table
    df.to_sql("stock_prices", connection, if_exists="replace", index=False)
    print("Data loaded successfully into PostgreSQL.")
except Exception as e:
    print(f"Error: {e}")

finally:
    connection.close()