import socket
import threading
import pickle
from game import Game

server = "127.0.0.1" # definiranje IP adresa na serverot
port = 5555 # definiranje na porta

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # kreiranje soket so IPv4 adresiranje i TCP protokol

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2) # serverot pocnuva da slusha
print("Waiting for a connection, Server Started") # pecati poraka deka serverot ceka konekcii

connected = set()
games = {}
idCount = 0


def threaded_client(conn, p, gameId):  # ovaa funkcija ja regulira komunikacijata so klientot vo posebna nitka
    global idCount                     # conn e objekt za konekcija koj pretstavuva klient, p e broj na igracot i gameId e ID na igrata vo koja ucestvuva klientot
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()

            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get":
                        game.play(p, data)

                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()



def accept_connections():  # ovaa funkcija gi prifaka dojdovnite vrski
    while True:
        conn, addr = s.accept()
        print("Connected to:", addr)

        global idCount
        idCount += 1
        p = 0
        gameId = (idCount - 1)//2
        if idCount % 2 == 1:
            games[gameId] = Game(gameId)
            print("Creating a new game...")
        else:
            games[gameId].ready = True
            p = 1

        threading.Thread(target=threaded_client, args=(conn, p, gameId)).start()


if __name__ == "__main__":
    accept_connections()