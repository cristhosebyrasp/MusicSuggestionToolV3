import pyodbc
import main


# Trusted Connection to Named Instance
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=.\SQL2K19;DATABASE=SampleDB;Trusted_Connection=yes;')
cursor=connection.cursor()
cursor.execute("SELECT @@VERSION as version")
while 1:
    row = cursor.fetchone()
    if not row:
        break
    print(row.version)
cursor.close()
connection.close()