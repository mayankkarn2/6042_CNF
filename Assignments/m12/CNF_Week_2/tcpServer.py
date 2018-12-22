import socket
import select
import threading
import csv

def file_reader():
    filename = "data.csv"
    data = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            data.append(row)
        return data

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('127.0.0.1', 5001))
    s.listen(20)

    while True:
        conn, addr = s.accept()
        print ('connection from : '+ str(addr))
        threading.Thread(target = respond, args = (conn, addr).start())

def respond(conn, addr):
    dump = file_reader()
    is_connected = True
    while is_connected:
        success = 'ATTENDANCE-SUCCESS'
        fail = 'ATTENDANCE-FAILURE'
        data = c.recv(1024).decode()
        if not data:
            break
        print ("from connected user : " + str(data)) 
        for i in range(len(dump)):
            details = row.split(",")
            if data == details[0]:
                c.send(str(details[1]).encode())
                answer = c.recv(1024).decode()
                if answer == details[2]:
                    c.send(str(success).encode())
                else:
                    c.send(str(fail).encode())
            if i == len(dump)-1:
                c.send('Not found')
                break
    print("server closed from" + str(addr))
    c.close()

if __name__ == "__main__":
    main()
