# Echo server program
import socket
import sys

HOST = None               # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,
                              socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except socket.error as msg:
        s = None
        continue
    try:
        s.bind(sa)
        s.listen(1)
    except socket.error as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print 'could not open socket'
    sys.exit(1)
inum = 0
while 1:
    conn, addr = s.accept()
    inum += 1
    print 'Connected by', addr, " cnt  ", str(inum)
    while 1:
        try:
            data = conn.recv(4096)
            if not data: break
            print eval(data)
            conn.send(data)
        except Exception, e:
            pass
    conn.close()