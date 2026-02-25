import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='',
  database='nbu-2012_proyecto_inbicu'
)

myCursor = mydb.cursor()

# First, let's check if there's data in the existing table
myCursor.execute("SELECT * FROM nbu_2012 LIMIT 3")
rows = myCursor.fetchall()
print("Sample data from existing table:")
for row in rows:
    print(f"  {row}")

# Drop the existing table and recreate with correct columns
myCursor.execute("DROP TABLE IF EXISTS nbu_2012")
print("\nOld table dropped")

# Create table with correct column names
create_table_sql = """
CREATE TABLE nbu_2012 (
    CODIGO VARCHAR(20) PRIMARY KEY,
    DETERMINACIONES TEXT,
    Urgencia VARCHAR(10),
    Ref VARCHAR(10),
    `U. B.` VARCHAR(20)
)
"""

myCursor.execute(create_table_sql)
print("New table created with correct columns")

# Import data from CSV
import csv

csv_file = 'NBU_2012.csv'
insert_sql = "INSERT IGNORE INTO nbu_2012 (CODIGO, DETERMINACIONES, Urgencia, Ref, `U. B.`) VALUES (%s, %s, %s, %s, %s)"

count = 0
with open(csv_file, 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)  # Skip header row
    
    for row in reader:
        if len(row) >= 5 and row[0].strip():
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
print(f"Successfully imported {count} rows")

# Verify
myCursor.execute("SHOW COLUMNS FROM nbu_2012")
columns = myCursor.fetchall()
print("\nNew columns in nbu_2012 table:")
for col in columns:
    print(f"  - {col[0]}")

# Test query
myCursor.execute("SELECT `CODIGO` FROM nbu_2012 WHERE `DETERMINACIONES` = 'ACIDIMETRIA GASTRICA , CURVA DE'")
result = myCursor.fetchone()
print(f"\nTest query result: {result}")

myCursor.close()
mydb.close()