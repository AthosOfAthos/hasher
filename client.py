import hashlib, socket
guess = "cat"

def get():
	client = socket.socket()
	client.connect((host,port))
	print("Conected to server")
	client.send(str("get").encode())
	return client.recv(1024).decode()

print ("Starting hasher client")
host = socket.gethostname()
port = int(input("Enter port: "))
print (get())

