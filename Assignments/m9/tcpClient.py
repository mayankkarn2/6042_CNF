import socket
def main():
    host  = '127.0.0.1'
    port = 5000
    s = socket.socket()
    s.connect((host,port))
    count = 0
    initial = s.recv(1024)
    print('received from server : '+ initial.decode())
    message = input("Enter your guess : ")
    while message != 'q':
        count += 1
        s.send(message.encode())
        data = s.recv(1024)
        print('received from server : ' + data.decode())
        if(data.decode() == 'correct!'):
            print("Number of guesses :"+str(count))
            break
        message = input("Enter your guess : ")
    s.close()

if __name__ == "__main__":
    main()