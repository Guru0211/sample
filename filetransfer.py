from socket import *

s = socket(AF_INET,SOCK_STREAM)

s.bind(("",8000))

s.listen(5)

with open(r"E:\cn programs\hi.txt") as file:
    data = file.read()

c,a = s.accept()

print("Received connection from", a)

c.send(data.encode('utf-8'))

c.close()
