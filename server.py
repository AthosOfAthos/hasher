import socket
print("Starting hasher server")
server = socket.socket()
host = socket.gethostbyname(socket.gethostname())
port = int(input("Enter port: "))
server.bind((host, port))
print("Server bound to: ", host, ":", port)
server.listen(5)
listen = True
while listen:
	connection, addr = server.accept()
	command = connection.recv(1024).decode()
	connection.close()
	print(str(command))
	listen = False;
#server.shutdown()
server.close()
print("Server closed")
