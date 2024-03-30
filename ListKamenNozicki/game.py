class Game:
    def __init__(self, id):
        self.p1Went = False # promenliva koja oznacuva dali prviot igrac napravil poteg
        self.p2Went = False # promenliva koja oznacuva dali vtoriot igrac napravil poteg
        self.ready = False # promenliva koja oznacuva dali igrata moze da zapocne
        self.id = id # identifikator na igra
        self.moves = [None, None] # lista na potezi na igracite
        self.wins = [0,0] # lista za pobedite na igracite
        self.ties = 0

    def get_player_move(self, p): # vraka poteg na igracot p
        return self.moves[p]

    def play(self, player, move):  # izvrsuvanje na poteg od strana na igracot player
        self.moves[player] = move
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True

    def connected(self):  # proveruva dali igrata moze da zapocne
        return self.ready

    def bothWent(self):  # proveruva dali dvata igraci veke izvrsile poteg
        return self.p1Went and self.p2Went

    def winner(self):  # odreduva koj igrac e podbednik vrz osnova na potezite koi gi napravile

        p1 = self.moves[0].upper()[0]
        p2 = self.moves[1].upper()[0]

        winner = -1
        if p1 == "К" and p2 == "Н":
            winner = 0
        elif p1 == "Н" and p2 == "К":
            winner = 1
        elif p1 == "Л" and p2 == "К":
            winner = 0
        elif p1 == "К" and p2 == "Л":
            winner = 1
        elif p1 == "Н" and p2 == "Л":
            winner = 0
        elif p1 == "Л" and p2 == "Н":
            winner = 1

        return winner

    def resetWent(self):  # gi resetira potezite na igracite
        self.p1Went = False
        self.p2Went = False