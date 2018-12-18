import socket
def conversion(data):
	tokens = data.split(" ")
	toDollar = int(tokens[2]) * convert_toDollar(tokens[1])
	print(toDollar)
	toCurrency = convert_toCurrency(toDollar, tokens[-1])
	print(tokens[-1])
	print(toCurrency)
	return toCurrency

def convert_toCurrency(toDollar, d):
	print("d:" + str(d))
	if d == 'INR':
		return toDollar * 67
	elif d == 'Pounds':
		return toDollar * 0.75
	elif d == 'Dollar':
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
	host = socket.gethostname()
	port = 5000
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host,port))
	print("server started")
	while True:
		data, addr = s.recvfrom(1024)
		print("message from: " + str(addr))
		print("from connect user: " + str(data.decode()))
		res = conversion(str(data.decode()))
		print("sending: " + str(res))
		s.sendto(str(res).encode(), addr)
	s.close()

if __name__ == '__main__':
    server_program()