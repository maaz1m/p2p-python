from peer import *

node = Node('localhost', 3300)
node.createSocket()
node.listen()
node.emit('msg', 'localhost', 3400, {'text': 'hello'})

