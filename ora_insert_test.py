#!/usr/bin/env python
#-*- coding: utf-8 -*-

import cx_Oracle


#한글깨짐 해결s
import os

os.environ["NLS_LANG"] = ".AL32UTF8"

START_VALUE = u"Unicode \u3042 3".encode('utf-8')
END_VALUE = u"Unicode \u3042 6".encode('utf-8')
#한글깨짐 해결e

dsnOra = cx_Oracle.makedsn("localhost", 1521, "SCHEMANAME")
dbOra = cx_Oracle.connect("system", "admin", dsnOra)
cursorOra = dbOra.cursor()

# cursorOra.setinputsizes(PRODID=None, SEQ=None, IMAGENAME=None)
cursorOra.setinputsizes(DETAILDESC=cx_Oracle.CLOB)
cursorOra.execute("""INSERT INTO shopping.product (PRODID, PRODIMAGE, PRODDESC)
 VALUES (:PRODID, :PRODIMAGE, :PRODDESC)""",
    PRODID=10002, PRODIMAGE=str("10002image."), DETAILDESC=str("설명설명매우좋고비싼명품유럽수제와우정말세련장인왕족뽀와리"))
dbOra.commit()

cursorOra.close()
dbOra.close()
