#!/usr/bin/env python3

# Requirement for Python Upload 05 about OOP-Advanced:
#
#
# a) Comments required: Add your Name
#    remove this comments or other unused lines of code

# b) For advanced Object-oriented Programming:


# improvement of Py04 code:

# b0
#   read (and test) the given class "Chessman" (with name and position)
#   read (and test) the given class "ChessBoard" (which includes a list of chessmen)
#
# b1
#   use Operator - Overloading (__add__, __iadd__,.... to allow
#      adding a chessman to the list of chessmen on a chessboard with operator "+"
#      override operator "+"   to return a copy of a chess-board with chessman added and
#      override operator "+="  to add a chessman to the chess-board) and
#      override operator "==" to compare two games (are all the chessmen on the same locations?)
# b2
#   use multiple inheritance to
#	   create another base class named Shape
#      i.e. a class to "draw" wooden/stone/brick figures
#      (Note: we do not draw anything in 2D, we are just simulating!)
#      method "__str__" ... which returns the shape, color and position
#      but also the used material: "Black wooden Bishop on a3".

# === neither algorithms nor consistency checks required ===

class MovableObject:
	def __init__(self, x, y):
		self.posX = x
		self.posY = y

	def move(self, toX, toY):
		self.posX = toX
		self.posY = toY

	def __str__(self):
		return "{} {} at {}{}".format(self.color, self.name, self.posX, self.posY)


class Shape:
	def __init__(self, material):
		self.material = material

	def __str__(self):
		return "{} {} {}".format(self.color, self.material, self.name)


class ChessPiece(MovableObject, Shape):
	abbrev = {'k': "King", 'q': "Queen", 'r': "Rook",
			  'b': 'Bishop', 'n': 'Knight', 'p': 'Pawn'}

	def __init__(self, name, x, y, material="wooden"):
		super().__init__(x, y)
		Shape.__init__(self, material)
		self.color = "Black" if name.islower() else "White"
		self.name = ChessPiece.abbrev[name.lower()]
		self.x = x
		self.y = y


class Board:
	def __init__(self, chessmen):
		self.chessmen = chessmen

	def __str__(self):
		return " and ".join(map(str, self.chessmen)) + "."

	def __add__(self, figure):
		board = list(self.chessmen)
		board.append(figure)
		return " and ".join(map(str, board)) + "."

	def __iadd__(self, chessmen):
		self.chessmen.append(chessmen)
		return self

	def __eq__(self, chessmen):
		return self.__str__() == chessmen.__str__()


# helpers:
def chessmen(configString):  # "Kc4,rd2,Qb2" lowercase for BLACK
	result = []
	for elem in configString.split(","):
		name = elem[0]  # Black: kqrbnp and White:  KQRBNP
		x = elem[1]
		y = elem[2]
		result += [ChessPiece(elem[0], x, y)]
	return result  # list of objects


# Just for testing:

# (the moodle-"evaluate" might  use different test data set!)

print('\nTEST "multiple inheritance" for a Chessman/Chesswoman:')
newBishop = ChessPiece("b", "a", "1")
print(newBishop)  # Black Bishop at a1

print('\nTEST creation of a Chess board:')
mychessboard = Board(chessmen("Qb2,Rh3"))
print(mychessboard)  # White Queen at b2 and White Rook at h3.

print('\nTest "+" operator overloading')
print(mychessboard + ChessPiece("b", "c", "5"))  # White Queen at b2 and White Rook at h3 and Black Bishop at c5.
print(mychessboard)  # White Queen at b2 and White Rook at h3.

print('\nTest "+=" operator overloading')
mychessboard += newBishop
print(mychessboard)  # White Queen at b2 and White Rook at h3 and Black Bishop at a1.

print('\nTest "==" operator overloading')
yourchessboard = Board(chessmen("Qb2,Rh3,ba1"))
print(yourchessboard)  # White Queen at b2 and White Rook at h3 and Black Bishop at a1.
print("My chess board is equal your board: {}.".format(
	mychessboard == yourchessboard))  # My chess board is equal your board: True.
