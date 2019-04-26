from peer import *

node = Node('localhost', 3400)
node.createSocket()
node.listen()

def printMessage(data):
	print('Recieved ', data['text'])

node.on('msg', printMessage)
