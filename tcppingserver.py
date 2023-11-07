from socket import *
s = socket(AF_INET,SOCK_STREAM)
s.bind(("",12000))
s.listen(5)
while True:
    c,a = s.accept()
    print("Received connection from", a)
    data="Server is Active"
    c.send(data.encode('utf-8'))
c.close()

