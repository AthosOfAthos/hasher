import socket
control = socket.socket()
host = socket.gethostbyname(socket.gethostname())
port = input("Enter port: ")
loop = True
while loop:
	command = input("Enter a command: ")
	control.connect((host, port))
	if command == "exit":
		control.send()
