# SOCKET CLIENT
import socket

# Set IP address and port number
IPaddr = "0.0.0.0"; 
portNum = 8080

# S = socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to IP address at port number
s.connect((IPaddr, portNum))

# Declare message to send
msg = "Hello in Python\n"

# Print message to client
print("Sending: ", msg)

# Send message to server
s.sendall(msg.encode())

# Receive and print
data = s.recv(1024)
print("Received: ", data.decode())

# Close socket
s.close()
