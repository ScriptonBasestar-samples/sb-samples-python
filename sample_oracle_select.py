import cx_Oracle

PORT_NUM = 1521
dsn = cx_Oracle.makedsn("SERVER_HOST", PORT_NUM, "ORCLE_SID_NAME")
db = cx_Oracle.connect("USERNAME", "PASSWORD", dsn)
cursor = db.cursor()

cursor.execute("""SELECT * FROM sso_data.t_users where rownum < 100""")
row = cursor.fetchone()
while row:
    print(str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]))
    row = cursor.fetchone()
