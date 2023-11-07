from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(("127.0.0.1",8000))
while(True):
    a=input()
    s.send(a.encode('utf-8'))  
    if a=='bye':
        print("Finished")
        break
    data = s.recv(100).decode()
    print("server:",data)
s.close()
