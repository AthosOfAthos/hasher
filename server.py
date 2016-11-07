import socket
hash = "1c3ea6f2b8cf5653460ddf549a52ff4b"
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
	if command == "exit":
		listen = False
	elif command == "get":
		connection.send(hash.encode())
		print("Sent hash to: ", addr)
	connection.close()
	print(str(command))
#server.shutdown()
server.close()
print("Server closed")
