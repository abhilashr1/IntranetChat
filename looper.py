import socket
import neighbour

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = neighbour.get_address()
port = 12346

server.bind((address,port))
server.listen(5)
print('>> Listening ... ')
while True:
    client_socket,client_address = server.accept()
    print('-----\nNew Accept:\nClient Socket: ',client_socket,'\nClient Address: ',client_address)
    entire_message=''
    while True:
        msg = client_socket.recv(1024)
        if not msg:
            break
        entire_message+=msg.decode(encoding='utf-8')
    msg = entire_message.split(':::::')
    dest = msg[0]
    message = msg[1]
    print(dest)
    print(message)

