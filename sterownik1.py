import socket


class Komora():
    def __init__(self, host='10.10.10.100', port=2049):
        self.host = host
        self.port = port

        self.is_connected = False
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.temp_set = None
        self.rh_set = None
        self.rh_current = None
        self.temp_current = None

        self.command=None
        self.response=None

    def set_temp_rh(self,temp,rh):

        #print(str(temp).zfill(4))
        self.temp_set=round(temp,2)
        self.rh_set=rh
        text='{:.2f}'.format(round(self.temp_set,2)).zfill(7)
        print(text)


        self.socket.connect((self.host, self.port))
        self.socket.sendall(b'$01E 0028.0 0035.0 0080.0 0080.0 0000.0 0000.0 0000.0 01101010101010101010101010101010\r')
        self.socket.sendall(b'$01I\r')


    def get_temp_rh(self):
        self.response=self.socket.recv(1024)
        print(self.response)
        return self.response


if __name__ == "__main__":
    kom = Komora()
    kom.set_temp_rh(26.1,33.2)
    kom.get_temp_rh()

"""
HOST = '10.10.10.100'  # The server's hostname or IP address
PORT = 2049  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #s.sendall(b'$01E 0026.0 0035.0 0080.0 0000.0 0000.0 0000.0 0000.0 01101010101010101010101010101010\r')
    #$01I\r
    s.sendall(b'$01I\r')
    # $01E 0021.0 0033.0 0080.0 0000.0 0000.0 0000.0 0000.0 01000001000000000000000000000000\r
    data = s.recv(1024)

print(data)

"""
