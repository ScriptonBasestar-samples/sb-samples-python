
import pymssql

conn = pymssql.connect(server='ipiphosthost', user='username', password='pwd_passwddddrd', database='dbnanmmnell')
cursor = conn.cursor()
cursor.execute('SELECT top 100 * FROM prod')
row = cursor.fetchone()
while row:
    print(str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]))
    row = cursor.fetchone()
