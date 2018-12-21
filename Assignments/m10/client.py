import socket 
import select 
import sys 

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 4001))




  
while True: 
    sockets_list = [sys.stdin, clientsocket] 
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[]) 

    for socks in read_sockets: 
        if socks == clientsocket: 
            message = socks.recv(2048) 
            print(str(message.decode()))
        else: 
            message = sys.stdin.readline() 
            clientsocket.send(str.encode(message))
            sys.stdout.flush() 
