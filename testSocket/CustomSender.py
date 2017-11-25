# -*- coding: utf-8 -*-
# Echo client program
import socket
import sys
import time

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
s = None

t0 = time.time()
for inum in range(1,100000):
    for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
            s = socket.socket(af, socktype, proto)
        except socket.error as msg:
            s = None
            continue
        try:
            s.connect(sa)
        except socket.error as msg:
            s.close()
            s = None
            continue
        break

    if s is None:
        print 'could not open socket'
        time.sleep(10)
        continue
#        sys.exit(1)

    sendString = """
    1   1     -50.00
    2   1     -50.00
    3   1     -50.00
    4   1     -50.00
    5   1     -50.00
    6   1     -50.00
    7   1     -50.00
    8   1     -50.00
    9   1     -50.00
    10   1     -50.00
    11   1     -50.00
    12   1     -50.00
    13   1     -50.00
    14   1     -50.00
    15   1     -50.00
    16   1     -50.00
    17   1     -50.00
    18   1     -50.00
    19   1     -50.00
    20   1     -50.00
    21   1     -50.00
    22   1     -50.00
    23   1     -50.00
    24   1     -50.00
    25   1     -50.00
    26   1     -50.00
    27   1     -50.00
    28   1     -50.00
    29   1     -50.00
    30   1     -50.00
    31   1     -50.00
    32   1     -50.00
    33   1     -50.00
    34   1     -50.00
    35   1     -50.00
    36   1     -50.00
    37   1     -50.00
    38   1     -50.00
    39   1     -50.00
    40   1     -50.00
    41   1     -50.00
    42   1     -50.00
    43   1     -50.00
    44   1     -50.00
    45   1     -50.00
    46   1     -50.00
    47   1     -50.00
    48   1     -50.00
    49   1     -50.00
    50   1     -50.00
    51   1     -50.00
    52   1     -50.00
    53   1     -50.00
    54   1     -50.00
    55   1     -50.00
    56   1     -50.00
    57   1     -50.00
    58   1     -50.00
    59   1     -50.00
    60   1     -50.00
    61   1     -50.00
    62   1     -50.00
    63   1     -50.00
    64   1     -50.00
    65   1     -50.00
    66   1     -50.00
    67   1     -50.00
    68   1     -50.00
    69   1     -50.00
    70   1     -50.00
    71   1     -50.00
    72   1     -50.00
    73   1     -50.00
    74   1     -50.00
    75   1     -50.00
    76   1     -50.00
    77   1     -50.00
    78   1     -50.00
    79   1     -50.00
    80   1     -50.00
    81   1     -50.00
    82   1     -50.00
    83   1     -50.00
    84   1     -50.00
    85   1     -50.00
    86   1     -50.00
    87   1     -50.00
    88   1     -50.00
    89   1     -50.00
    90   1     -50.00
    91   1     -50.00
    92   1     -50.00
    93   1     -50.00
    94   1     -50.00
"""
    
    #s.sendall('Hello, world'+str(inum))
    s.send('{"name":"jsonStyle1", "WFT":"안녕친구야", "VAL":32.3}')
    data = s.recv(4096)
    s.send('{"name":"jsonStyle2", "WFT":"안녕친구야", "VAL":32.3}')
    data = s.recv(4096)
    s.send('{"name":"jsonStyle3", "WFT":"안녕친구야", "VAL":32.3}')
    data = s.recv(4096)
    
#    totalsent = 0
#        while totalsent < MSGLEN:
#            sent = self.sock.send(msg[totalsent:])
#            if sent == 0:
#                raise RuntimeError("socket connection broken")
#            totalsent = totalsent + sent
    
    s.close()
print 'Received', repr(data)
t1 = time.time()

print "exe time : ", t1-t0












