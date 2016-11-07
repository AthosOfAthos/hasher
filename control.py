import socket
control = socket.socket()
host = socket.gethostbyname(socket.gethostname())
port = input("Enter port: ")
loop = True
while loop:
	command = input("Enter a command: ")
	control = socket.socket()
	control.connect((host, int(port)))
	if command == "exit":
		control.send(str("exit").encode())
		loop = False
	else:
		control.send(command.encode())
	control.close()
