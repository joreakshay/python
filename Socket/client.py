import socket
import sys
import string
class ServerInfo():
	def __init__(self,ip="localhost",port=10004,ststud_command="ps",output_file="server1.txt"):
		self.ip=ip
		self.port=port
		self.ststud_command=ststud_command
		self.output_file=output_file
		self.sock=""
	def __del__(self):
		del(self)
	def connect(self):
		# Create a TCP/IP socket
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		# Connect the socket to the port where the server is listening
		server_address = (self.ip,self.port)
		print('connecting to %s port %s' % server_address)
		self.sock.connect(server_address)
		
		try:
			# Send data
			message = 'India is my Country, all Indians are my brothers & sisters.'
			print('sending "%s"' % message)
			while 1:
				#sock.send(bytes(message, 'UTF-8')) # 3 & above
				sock.sendall(message) # 2.7
			
				# Look for the response
				amount_received = 0
				amount_expected = len(message)
		
				while amount_received < amount_expected:
					data = sock.recv(10)
					amount_received += len(data)
					print('received "%s"' % data)
		
				message = input("Enter msg:-")
		
		finally:
			print('closing socket')
		sock.close()
