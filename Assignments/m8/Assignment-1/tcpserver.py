# to convert one currency rate to other
import socket
def conversion(data):
	tokens = data.split(" ")
	toDollar = int(tokens[2]) * convert_toDollar(tokens[1])
	toCurrency = convert_toCurrency(toDollar, tokens[-1])
	return toCurrency

def convert_toCurrency(toDollar, data):
	if data == 'INR':
		return toDollar * 67
	elif data == 'Pounds':
		return toDollar * 0.75
	elif data == 'Dollar':
		return toDollar;
	else:
		return toDollar * 113.41 
	
def convert_toDollar(data):
	if data == 'INR':
		return 1/67
	elif data == 'Pounds':
		return 1/0.75
	elif data == 'Dollar':
		return 1;
	else:
		return 1/113.41
def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(1)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data = str(conversion(str(data)))
        print("sending:" + str(data))
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
