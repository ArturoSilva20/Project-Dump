import socket
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
# Server's IP address
SERVER_IP = sys.argv[1]

# The server's port number
SERVER_PORT = int(sys.argv[2])

key = sys.argv[3]
# The client's socket
cliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Attempt to connect to the server
cliSock.connect((SERVER_IP, SERVER_PORT))

# Send the message to the server
msg = input("Please enter a message to send to the server: ")


paddedmsg = pad(msg,16)
encCipher = AES.new(key, AES.MODE_ECB)
cipherText = encCipher.encrypt(paddedmsg)
# Send the message to the server
# NOTE: the user input is of type string
# Sending data over the socket requires.
# First converting the string into bytes.
# encode() function achieves this.
cliSock.send(cipherText.encode())

