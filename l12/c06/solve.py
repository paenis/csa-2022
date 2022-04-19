import socket

HOST = 'services.cyberprotection.agency'
PORT = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
    
	def sr(*data):
		for item in data:
			print('>',repr(item))
			s.sendall(item.encode())
			rcv = s.recv(1024)
			print('<', repr(rcv))
    

	data = s.recv(1024)
	print(data := data.decode())

	nums = [*map(int,data.strip().split('\n'))]
	print(nums)

	res = (nums[0]*nums[1])//nums[2]
	print(res)
	sr(str(res))
