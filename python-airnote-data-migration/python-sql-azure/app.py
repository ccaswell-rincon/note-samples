
import azure.identity
import pandas as pd
import os
import pyodbc, struct
# Define connection details
server = "notehubsensordata.database.windows.net"
database = "Notehub_Sensor_Data"

# Connection string
conn_string = f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};Authentication=ActiveDirectoryInteractive;Encrypt=yes;TrustServerCertificate=no;"

try:
    conn = pyodbc.connect(conn_string)
    print("✅ Successfully connected to Azure SQL Database!")

    # Create a cursor
    cursor = conn.cursor()

except Exception as e:
    print(f"❌ Connection failed: {e}")

# Bulk insert command
#cursor.execute("""
#BULK INSERT testnotehub
#FROM 'I:\GIS\Data_Solutions\note-samples\python-airnote-data-migration\python-sql-azure\testnotehub.csv'
#WITH (FORMAT = 'CSV', FIRSTROW = 2, FIELDTERMINATOR = ',', ROWTERMINATOR = '\n')
#""")

#conn.commit()
#cursor.close()
#conn.close()

#print("✅ Bulk data import completed!")

# Azure SQL connection using SQLAlchemy - is this needed? tbd 
from sqlalchemy import create_engine
engine = create_engine("mssql+pyodbc://ccaswell@rinconconsultants.com:Tuckerman*1@notehubsensordata.database.windows.net/Notehub_Sensor_Data?driver=ODBC+Driver+18+for+SQL+Server")

#run script 
#!python main.py
#FIGURE OUT HOW TO GET THE OUTPUT OF MAIN.PY into the SQL Notebook "testnotehub"
# store output
#!python main.py  -d dev:863740067277423
output = os.popen("python main.py -d dev:863740067277423").read()
#data = pd.read_csv(StringIO(output))
#df = pd.DataFrame(data)
#print(df)
# Insert data into SQL Server
#df.to_sql("testnotehub", engine, if_exists="append", index=False)
