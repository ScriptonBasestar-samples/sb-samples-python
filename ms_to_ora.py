#!/usr/bin/env python

# https://pypi.python.org/pypi/cx_Oracle/
# https://haandol.wordpress.com/2014/04/17/windows%EC%97%90-cx_oracle-%EC%84%A4%EC%B9%98%ED%95%98%EC%97%AC-%EC%9B%90%EA%B2%A9-oracle-%EC%84%9C%EB%B2%84%EC%97%90-%EC%A0%91%EA%B7%BC%ED%95%98%EA%B8%B0/

import cx_Oracle
import pymssql

import os

os.environ["NLS_LANG"] = ".AL32UTF8"

START_VALUE = u"Unicode \u3042 3".encode('utf-8')
END_VALUE = u"Unicode \u3042 6".encode('utf-8')


dbMS = pymssql.connect(server='mssql erver ip', user='mssql user', password='mssql password', database='mssql database')
cursorMS = dbMS.cursor()

dsnOra = cx_Oracle.makedsn("oracle server ip", 1521, "sidname")
dbOra = cx_Oracle.connect("oracle user", "oracle password", dsnOra)
cursorOra = dbOra.cursor()

cursorMS.execute('SELECT * FROM SchemaName.TableName order by id asc')
row = cursorMS.fetchone()
while row:
    print(str(row[0]) + " " + str(row[1]) + " " + str(row[2]))
    # print(row[0] + " " + row[1] + " " + row[2] + " " + row[3])
    # print(row[1])
    # break

    #DESC는 CLOB
    cursorOra.setinputsizes(DETAILDESC=cx_Oracle.CLOB)
    cursorOra.execute("""INSERT INTO SchemaName.TableName (id, name, desc)
 VALUES (:ID, :NAME, :DESC)""",
                   ID=str(row[0]), NAME=row[1], DESC=str(row[3]).encode("utf-8"))

    dbOra.commit()
    row = cursorMS.fetchone()

dbMS.close()
cursorMS.close()

cursorOra.close()
dbOra.close()
