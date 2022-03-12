#
# Connect to alien server ('localhost', 10000),
# Then send USER followed by aliensignal,
# Then send PASS followed by unlockserver,
# Next SEND followed by moonbase.
# Then send END and if all followed key will provided.
#
# Note: You must receive data back from the server after you send each message
#


import socket

HOST = 'localhost'       # The remote host
PORT = 10000             # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    def sr(*data):
      for item in data:
        s.sendall(item.encode())
        rcv = s.recv(1024)
        print('Received', repr(rcv))
    #data = s.recv(1024)
    sr('USER','aliensignal')
    sr('PASS','unlockserver')
    sr('SEND','moonbase')
    sr('END')

