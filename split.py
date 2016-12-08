#!/usr/bin/env python

import fileinput
i = 1
fout = open("output0.txt", "wb")
for line in fileinput.FileInput("E:\sddump\data2\T_SHIP_DATA_TABLE.sql", "UTF-8"):
  fout.write(line)
  i+=1
  if i%40000 == 0:
    fout.close()
    fout = open("output%d.txt"%(i/40000),"wb")

fout.close()