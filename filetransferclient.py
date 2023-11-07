from socket import *

s = socket(AF_INET, SOCK_STREAM)

s.connect(("127.0.0.1",8000)) # Connect

data = s.recv(100).decode()# Get response

print(data)

file = open(r"E:\cn programs\hello.txt",'w')

file.write(data)

file.close()

s.close()
