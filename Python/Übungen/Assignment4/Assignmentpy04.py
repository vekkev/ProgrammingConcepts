#!/usr/bin/env python3

# Requirement for Python Upload 04 about OOP-Basics:
#
# a) Comments required: Add your Name
#    remove this comments or other unused lines of code

# b) For basic Object-oriented Programming:
#    b1) create basic classes for a game
#        moveable objects (position, color, move-action, ...)
#    b2) create classes using inheritance for a chess game
#        (cmp: http://www.chesscorner.com/tutorial/learn.htm )
#        Class for each type of chessmen (king=K, queen=Q, rooks=R,
#              bishops=B, knights=N, pawns=P) = moveable objects to deploy
#              on a board (=matrix 1..8 x a..h with a1=lower-left-corner)
#              (Outlook for py05: you will use multiple inheritance)
#    b3) class for chess-game containing list of
#              current chessmen on the chessboard
#             (Outlook for py05 you will override operators such as += )
#
# === neither algorithms nor consistency checks required ===

#### START of my CODE ####

# invent a base class for movable objects

class MovableObjects:

    def __init__(self, position, color, move_action, type):
        self.position = position
        self.color = color
        self.move_action = move_action
        self.type = type;
        # White Rook on position a1

    def toString(self):
        return self.color + " " + self.type + " on position " + self.position


# inherited class for chess pieces

class King(MovableObjects):

    def __init__(self, position, color, move_action, type):
        MovableObjects.__init__(self, position, color, move_action, type)


class Queen(MovableObjects):

    def __init__(self, position, color, move_action, type):
        MovableObjects.__init__(self, position, color, move_action, type)


class Rooks(MovableObjects):

    def __init__(self, position, color, move_action, type):
        MovableObjects.__init__(self, position, color, move_action, type)


class Bishops(MovableObjects):

    def __init__(self, position, color, move_action, type):
        MovableObjects.__init__(self, position, color, move_action, type)


class Knights(MovableObjects):

    def __init__(self, position, color, move_action, type):
        MovableObjects.__init__(self, position, color, move_action, type)


class Pawns(MovableObjects):

    def __init__(self, position, color, move_action, type):
        MovableObjects.__init__(self, position, color, move_action, type)


# class for a chess board

class Board:
    def __init__(self, chessmen=[]):
        self.chessmen = chessmen


#### END of my CODE ####


def chessmen(configString):  # "Kc4,rd2,Qb2" lowercase for BLACK
    result = []
    #### START of my CODE ####
    splitString = configString.split(',')
    for chessmen in splitString:

        # KING
        if chessmen[0].find('K') != -1:
            s = chessmen.strip('K')
            result.append(King(s, "White", "Stand", "King").toString())

        elif chessmen[0].find('k') != -1:
            s = chessmen.strip('k')
            result.append(King(s, "Black", "Stand", "King").toString())
        # QUEEN
        elif chessmen[0].find('Q') != -1:
            s = chessmen.strip('Q')
            result.append(Queen(s, "White", "Stand", "Queen").toString())

        elif chessmen[0].find('q') != -1:
            s = chessmen.strip('q')
            result.append(Queen(s, "Black", "Stand", "Queen").toString())
        # ROOKS
        elif chessmen[0].find('R') != -1:
            s = chessmen.strip('R')
            result.append(Rooks(s, "White", "Stand", "Rook").toString())

        elif chessmen[0].find('r') != -1:
            s = chessmen.strip('r')
            result.append(Rooks(s, "Black", "Stand", "Rook").toString())
        # BISHOPS
        elif chessmen[0].find('B') != -1:
            s = chessmen.strip('B')
            result.append(Bishops(s, "White", "Stand", "Bishop").toString())

        elif chessmen[0].find('b') != -1:
            s = chessmen.strip('b')
            result.append(Bishops(s, "Black", "Stand", "Bishop").toString())
            # PAWNS
        elif chessmen[0].find('P') != -1:
            s = chessmen.strip('P')
            result.append(Pawns(s, "White", "Stand", "Pawn").toString())

        elif chessmen[0].find('p') != -1:
            s = chessmen.strip('p')
            result.append(Pawns(s, "Black", "Stand", "Pawn").toString())

            # KNIGHTS
        elif chessmen[0].find('N') != -1:
            s = chessmen.strip('N')
            result.append(Knights(s, "White", "Stand", "Knight").toString())

        elif chessmen[0].find('n') != -1:
            s = chessmen.strip('n')
            result.append(Knights(s, "Black", "Stand", "Knight").toString())
            # analyse string

    # create some chessmen and add to list

    #### END of my CODE ####
    return result


# helper to make grading (comparing strings) easier
def chessmenToString(configString):
    men = chessmen(configString)
    chessmenstrings = map(str, men)
    return " and ".join(chessmenstrings)


# Just for testing:

# (the moodle-"evaluate" might  use different test data set!)
currentPositions = "Ka1,ra8,ka2,Pb2,Ph2"

pieces = chessmen(currentPositions)
mychessboard = Board(pieces)
for piece in mychessboard.chessmen:
    print(piece)
    # print:
    # White Rook on position a1
    # Black Rook on position a8
    # ...

print(chessmenToString(currentPositions))  # White Rook on position a1 and Black Rook on position a8 and ...