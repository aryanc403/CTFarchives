import socket
import re

# https://gist.github.com/leonjza/f35a7252babdf77c8421
class Netcat:

    """ Python 'netcat like' module """

    def __init__(self, ip, port):

        self.buff = ""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))

    def read(self, length = 1024):

        """ Read 1024 bytes off the socket """

        return self.socket.recv(length)

    def read_until(self, data,fl=False):

        """ Read data into the buffer until we have data """

        if fl:
            while True:
                s=self.socket.recv(1024)
                print(s)
                if len(s)==0:
                    exit(0)
        else:
            while not data in self.buff:
                self.buff += self.socket.recv(1024)

        pos = self.buff.find(data)
        rval = self.buff[:pos + len(data)]
        self.buff = self.buff[pos + len(data):]

        return rval

    def write(self, data):

        self.socket.send(data)

    def close(self):

        self.socket.close()

if __name__ == '__main__':
    nc = Netcat('jh2i.com', 50031)

    def level_up(n):
        print("Moving to next level. Current level "+str(n-1))
        nc.write(str.encode('6\n'))
        nc.buff = b''
        string = nc.read_until(b"tank (100000 gold) (level 10)").decode("utf-8")
        nc.write(str.encode(str(n)+'\n'))
        print("Moved to next level. Current level "+str(n))

    def current_balance(s):
        s = s[s.find('Gold: ')+len('Gold: '):]
        s = s[:s.find('Weapon ')-1]
        print("Current gold "+s)
        return int(s)

    cur_level=0
    cost=[100,1000,2000,10000,100000]

    while True:
        nc.buff = b''
        string = nc.read_until(b"7. End journey").decode("utf-8")
        print("[ Read log: "+string+"]")

        if cur_level==len(cost):
            print("Exiting")
            nc.write(str.encode("7\n"))
            nc.read_until(b'keep__calm',True)
        elif current_balance(string)>=cost[cur_level]:
            cur_level+=1
            level_up(cur_level)

        nc.write(str.encode(str(6-cur_level)+'\n'))