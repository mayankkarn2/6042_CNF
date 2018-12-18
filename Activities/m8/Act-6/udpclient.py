import socket

def client_program():
	host = socket.gethostname()
	port = 5001
	server = (host, 5000)
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host,port))
	message = input("->")
	while message.lower().strip() != 'end':
		s.sendto(message.encode(), server)
		data, addr = s.recvfrom(1024)
		print("recieved from server: " + str(data))
		message = input("->")
	s.close()

if __name__ == '__main__':
    client_program()