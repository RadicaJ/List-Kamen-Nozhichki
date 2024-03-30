import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # kreiranje soket
        self.server = "127.0.0.1"  # IP adresa na serverot
        self.port = 5555  # portata na serverot
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):  # go vraka brojot na igracot koj e dodelen na klientot
        return self.p

    def connect(self):  # go povrzuva klientot so serverot
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):  # ispraka podatoci do serverot i prima odgovor
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048*2))
        except socket.error as e:
            print(e)