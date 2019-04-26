import threading
import socket
import json
import sys

dbg = 0

def debug(m):
	if(dbg):
		print(m)

class Node:
	#Class that defines the current node
	
	def __init__(self,hname,hport):
		self.hostname = hname
		self.port = hport
		self.succ = ''
		self.pred = ''
		self.listener = {}


	def createSocket(self):
		#Function for creating a socket on the node to listen.
		try:
			sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		except socket.error, msg:
			print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
			sys.exit();
		try:
			sock1.bind((self.hostname, self.port))
		except socket.error , msg:
			print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message: ' + msg[1]
			sys.exit()
		sock1.listen(10)
		self.sock =  sock1
		debug('Created socket at ' + self.hostname + ':' + str(self.port))

	def emit(self, tag, clientHostname, clientPort, msg):
		# Function to send requests and responses to specified targets
		data = tag + '|' + json.dumps(msg)
		try:
			sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			remote_ip = socket.gethostbyname( clientHostname )
			sock2.connect((remote_ip , int(clientPort)))
			sock2.send(data)
			sock2.close()
			debug('Sent: ' + data + ' to ' + clientHostname + ':' + str(clientPort))
		except socket.error, msg:
			print(clientHostname + ':' + str(clientPort) + ' is not online')

	def on(self, tag, func):
		self.listener[tag] = func
		debug('Added listener for ' + tag)


	def listen(self):
		def listenAux():
			while 1:
				conn, addr = self.sock.accept()
				req = conn.recv(1024)	
				msg = req.split('|')
				if req:
					tag = msg[0]
					data = json.loads(msg[1])
					if self.listener[tag]:
						self.listener[tag](data)	
				else:
					break
		
		debug('Listening')
		threading.Thread(target=listenAux).start()


