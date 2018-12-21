import socket 
import select 
import sys 
import _thread


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('localhost', 4001))
serversocket.listen(20)

clients = [] 

def thread(c, add):  

    Welcome_msg = "Welcome to this chatroom!"
    c.send(str.encode(Welcome_msg)) 
  
    while True:  
        data = c.recv(2048) 
        if data: 
            print(str(add[1]) + ":" + str(data))
            send_all(str(add[1]) + ":" + str(data) , c) 
        else: 
            remove(c) 


def send_all(msg, conn):
    for c in clients:
    	# if(c != conn):   
        c.send(str.encode(msg))

def remove(c):
    clients.remove(c)


while True: 
    conn, addr = serversocket.accept() 
    clients.append(conn) 
    print(str(addr[1]) + " client connected")
    _thread.start_new_thread(thread,(conn,addr))     
  
conn.close() 
server.close() 