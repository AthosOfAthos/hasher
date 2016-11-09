import hashlib, socket
guess = ["test","cat"]

def get():
	client = socket.socket()
	client.connect((host,port))
	print("Conected to server")
	client.send(str("get").encode())
	gethash = str(client.recv(1024).decode())
	client.close()
	return gethash

def send(solution):
	client = socket.socket()
	client.connect((host,port))
	print("Connected to server")
	client.send(solution.encode())
	client.close()

def getOrder():
	print("Fetching orders")
	client = socket.socket()
	client.connect((host,port))
	print("Connected to server")
	client.send("order".encode())
	client.close()

def generate(start):
	

def solve(hashguess):
	hasher = hashlib.new('md4')
	hasher.update(str(hashguess).encode("utf-8"))
	return hasher.hexdigest()

print ("Starting hasher client")
host = socket.gethostname()
port = int(input("Enter port: "))
hash = get()
looping = True
iteration = 0
while looping:
	print("Trying: " + guess[iteration])
	guesshash = solve(guess[iteration])
	if guesshash == hash:
		print("Solution found: " + guess[iteration])
		send(guess[iteration])
		looping = False
	else:
		print("Failed")
		iteration += 1

