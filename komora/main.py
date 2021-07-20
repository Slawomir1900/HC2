import socket
import time

HOST = '10.10.10.100'  # The server's hostname or IP address
PORT = 2049  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'$01E 0010.0 0055.0 0080.0 0100.0 0000.0 000000000000000000000000000000000\r')
    #s.sendall(b'$01E 0029.0 0025.8 0080.0 0000.0 0006.0 0100.0 0000.0 01100010101010101010101010101010\r')


while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'$01I\r')
        data = s.recv(1024)
        time.sleep(1)
        print(data)




 #s.sendall(b'$01E 0026.0 0035.0 0080.0 0000.0 0000.0 0000.0 0000.0 01101010101010101010101010101010\r')