import socket
def Main():
    host = '127.0.0.1'
    port = 5000
    sct = socket.socket()
    inp = input("MARK-ATTENDANCE ")
    while inp != 'quit':
        sct.send(inp.encode())
        data = sct.recv(1024)
        if data == "Not found":
            print("Not found")
            break
        else:
            print('Your Secret Question is: ')
            print(data.decode())
            ans = input('Your answer')
            sct.send(ans.encode())
            response = sct.recv(1024).decode()
            if(response == 'success'):
                print('ATTENDANCE-SUCCESS')
                break
    sct.close()

if __name__ == '__main__':
    Main()