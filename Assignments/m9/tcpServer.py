import socket
import random
import threading


def Main():
    host  = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host,port))
    s.listen(10)

    while True:
        c, addr = s.accept()
        print ('connection from : '+ str(addr))
        initial = 'welcome to guess my number'
        c.send(str(initial).encode())
        threading.Thread(target = Guess, args = (c, addr)).start()

def Guess(c, addr):
    connection = True
    while connection:
        option1 = 'correct!'
        option2 = 'your number is less than guess'
        option3 = 'your number is greater than guess'
        data = c.recv(1024).decode()
        data = int(data)
        if not data:
            break
        print ("from connected user : " + str(data))
        if(data == num):
            c.send(str(option1).encode())
            connection = False
            break
        elif(data < num):
            c.send(str(option2).encode())
        elif(data >  num):
            c.send(str(option3).encode())
    print("server closed from" + str(addr))
    c.close()

num = random.randrange(1,51)

if __name__ == '__main__':
    Main()