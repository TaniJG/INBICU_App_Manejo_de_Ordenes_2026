import mysql.connector
import csv

# Connect to MySQL server (without database first to create it)
mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password=''
)

myCursor = mydb.cursor()

# Create database if not exists
myCursor.execute("CREATE DATABASE IF NOT EXISTS nbu_2012_proyecto_inbicu")
print("Database created or already exists")

# Use the database
myCursor.execute("USE nbu_2012_proyecto_inbicu")

# Create table with correct column names (matching CSV)
# Note: Using backticks for column names that might be reserved words or have spaces
create_table_sql = """
CREATE TABLE IF NOT EXISTS nbu_2012 (
    CODIGO VARCHAR(20) PRIMARY KEY,
    DETERMINACIONES TEXT,
    Urgencia VARCHAR(10),
    Ref VARCHAR(10),
    `U. B.` VARCHAR(20)
)
"""

myCursor.execute(create_table_sql)
print("Table 'nbu_2012' created or already exists")

# Import data from CSV
csv_file = 'NBU_2012.csv'

insert_sql = "INSERT IGNORE INTO nbu_2012 (CODIGO, DETERMINACIONES, Urgencia, Ref, `U. B.`) VALUES (%s, %s, %s, %s, %s)"

count = 0
with open(csv_file, 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)  # Skip header row
    
    for row in reader:
        if len(row) >= 5 and row[0].strip():  # Ensure row has data and CODIGO is not empty
            codigo = row[0].strip()
            determinaciones = row[1].strip() if len(row) > 1 else ''
            urgencia = row[2].strip() if len(row) > 2 else ''
            ref = row[3].strip() if len(row) > 3 else ''
            u_b = row[4].strip() if len(row) > 4 else ''
            
            try:
                myCursor.execute(insert_sql, (codigo, determinaciones, urgencia, ref, u_b))
                count += 1
            except Exception as e:
                print(f"Error inserting row {codigo}: {e}")

mydb.commit()
print(f"Successfully imported {count} rows into nbu_2012 table")

# Verify the import
myCursor.execute("SELECT COUNT(*) FROM nbu_2012")
result = myCursor.fetchone()
print(f"Total rows in table: {result[0]}")

# Test the query that was failing
myCursor.execute("SELECT `CODIGO` FROM nbu_2012 WHERE `DETERMINACIONES` = 'ACIDIMETRIA GASTRICA , CURVA DE'")
result = myCursor.fetchone()
print(f"Test query result for 'ACIDIMETRIA GASTRICA , CURVA DE': {result}")

myCursor.close()
mydb.close()
