# Python P2P API
A very basic implementation of peer to peer networking in Python

## USAGE & EXAMPLES
_________________

### Peers:

*peer1.py* 

`from node import *

node = Node('localhost', 3400)
node.createSocket()
node.listen()

def printMessage(data):
	print('Recieved ', data['text'])

node.on('msg', printMessage)`

*peer2.py* 

`from node import *

node = Node('localhost', 3300)
node.createSocket()
node.listen()

node.emit('msg', 'localhost', 3400, {'text': 'hello'})`


