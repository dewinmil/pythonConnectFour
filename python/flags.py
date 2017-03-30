import sys
import getopt

class connectFour:
	def __init__(self, height=7, width=7, connect=4, save="", load =""):
		self.height = height
		self.width = width
		self.connect = connect
		self.save = save
		self.load = load
		try:
			opts, args = getopt.getopt(sys.argv[1:], 'h:v:w:v:b:v:c:v:s:v:l:v', ['height=','width=', 'both=', 'connect=', 'save=', 'load=', 'help'])
		except getopt.GetoptError:
			print "Invalid command or missing argument, try typing --help"
			sys.exit(2)
	
		for opt, arg in opts:	
			if opt == '--help':
				print "this is my help statement"
				sys.exit(2)
			elif opt in ('-h', '--height'):
				try:
					arg = int(arg)
				except ValueError:
					print "Invalid argument: non-integer argument for argument height. (-h)"
					sys.exit(2)
				self.height = arg
			elif opt in ('-w', '--width'):
				try:
					arg = int(arg)
				except ValueError:
					print "Invalid argument: non-integer argument for argument width. (-w)"
					sys.exit(2)
				self.width = arg
			elif opt in ('-b','--both'):
				try:
					arg = int(arg)
				except ValueError:
					print "Invalid argument: non-integer argument for agument both. (-b)"
					sys.exit(2)
				self.height = arg
				self.width = arg
			elif opt in ('-c','--connect'):
				try:
					arg = int(arg)
				except ValueError:
					print "Invalid argument: non-integer argument for agument connect. (-c)"
					sys.exit(2)
				self.connect = arg
			elif opt in ('-s','--save'):
				self.save = arg			
			elif opt in ('-l','--load'):
				self.load = arg
			else:
				print "Invalid command or missing argument, try typing --help"
				sys.exit(2)
		
		if self.connect > self.height or self.connect > self.width:
			print "Error: connect greater than board length"
			sys.exit(2)
	def Display(self, board):
		over50 = 0
		count = 0
		if self.width > 50:
			over50 = 1
		if over50 == 1:
			for i in range(0, self.height): 
				for k in range(0, 50):
					sys.stdout.write(board[k][count+i] + " ")
				sys.stdout.write("\n");
			sys.stdout.write("\n\ncolumns " + str(count) + " to " + str(count+49))
			sys.stdout.write("\n\n")
			self.width = self.width - 50
			count = count + 50
			if self.width < 50:
				over50 = 0
			
		if self.width != 0:
			for i in range(0, self.height):
				for j in range(0, self.width):
					sys.stdout.write(board[j][count+i] + " ")
				sys.stdout.write("\n");
			sys.stdout.write("\n\ncolumns " + str(count) + " to " + str(count+49))
			sys.stdout.write("\n\n")
		sys.stdout.write("\n\n")
			
	def playCol(self, board, colNum, player):
		
		if colNum > (self.width -1) or colNum < 0:
			print "\nError: invalud column number"
			exit(3)
		for i in range(0, self.height-1):		
			if board[colNum][i+1] != "*":
				if board[colNum][i] != "*":
					print("\nError: column already full")
					return	
				if player == 1:
					board[colNum][i] = "X"
					return
				else:
					board[colNum][i] = "O"
					return
			if i+1 == self.height -1 and board[colNum][i] =="*":
				if player == 1:
					board[colNum][i+1] = "X"
					return
				else:
					board[colNum][i+1] = "O"
					return
	
	def checkHor(self, board, rowNum, player):
		count = 0
		if player == 1:
			player = "X"
		else:
			player = "O"
		for i in range(0, self.width):
			if board[i][rowNum] == player:
				count = count + 1
			else:
				count = 0
			if count >= self.connect:
				return 1
			
	def checkVert(self, board, colNum, player):
		count = 0
		if player == 1:
			player = "X"
		else:
			player = "O"
		for i in range(0, self.width):
			if board[colNum][i] == player:
				count = count + 1
			else:
				count = 0
			if count >= self.connect:
				return 1
		





if __name__ == '__main__':
	game = connectFour();
	board = [["*" for x in range(game.height)] for y in range(game.width)]
	game.Display(board)
	game.playCol(board, 0, 1)
	game.Display(board)
	game.playCol(board, 0, 1)
	game.Display(board)
	game.playCol(board, 0, 1)
	game.Display(board)
	game.playCol(board, 0, 1)
	game.Display(board)
	
	i = game.checkVert(board, 0, 1);
	if i == 1:
		print "winner"
	else:
		print "loser"

