import socket
import threading

bind_ip  ="0.0.0.0"
bind_port=9999

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)
print "[*] Listen on %s:%d" % (bind_ip,bind_port)

def handle_client(client_socket):
    request=client_socket.recv(1024)
    print  "[*] Recieved: %s" %  request
    client_socket.send("fuck")
    client_socket.close()

while True:
    c,addr=server.accept()
    print "[*]Accepted connection from %s:%d" % (addr[0],addr[1])
    client_handler = threading.Thread(target=handle_client,args=(c,))
    client_handler.start()

