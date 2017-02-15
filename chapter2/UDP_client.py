import socket

target_host="127.0.0.1"
target_port=9999

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

client.sendto("not hello world",(target_host,target_port))

data,addr=client.recvfrom(1204)

print data
