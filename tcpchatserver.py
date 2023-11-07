from socket import *
s = socket(AF_INET,SOCK_STREAM)
s.bind(("",8000))
s.listen(5)
c,a = s.accept()
data=""
while(True):
    x=c.recv(100).decode()
    if x=="bye":
        print("Finished")
        break
    print("client:",x)
    data=input()
    c.send(data.encode('utf-8'))
c.close()


