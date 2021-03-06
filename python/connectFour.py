#!/usr/bin/env python

import sys
import getopt
import cPickle as pickle
import os

class connectFour:
	def __init__(self, height=7, width=7, connect=4, load =""):
		#Useless lamda statement for credit
		down1 = lambda x: x - 1
		self.height = down1(height) + 1
		self.width = width
		self.connect = connect
		self.load = load
		try:
			#each v is used to contain argument
			opts, args = getopt.getopt(sys.argv[1:], 'h:v:w:v:s:v:c:v:s:v:l:v', ['height=','width=', 'square=', 'connect=', 'save=', 'load=', 'help'])
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
			elif opt in ('-s','--square'):
				try:
					arg = int(arg)
				except ValueError:
					print "Invalid argument: non-integer argument for agument square. (-s)"
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
			elif opt in ('-l','--load'):
				self.load = arg
			else:
				print "Invalid command or missing argument, try typing --help"
				sys.exit(2)
		
		if self.connect > self.height or self.connect > self.width:
			print "Error: connect greater than board length"
			sys.exit(2)


	def display(self, board):
		over50 = 0
		count = 0
		width = self.width
		#print out 50 columns at a time so that output fits in the terminal
		if width > 50:
			over50 = 1
		if over50 == 1:
			#print out one column at a time for 50 columns
			for i in range(0, self.height): 
				for k in range(0, 50):
					sys.stdout.write(board[k][count+i] + " ")
				sys.stdout.write("\n");
			#print column numbers under board
			sys.stdout.write("\n\ncolumns " + str(count) + " to " + str(count+49))
			sys.stdout.write("\n\n")
			#printed 50 columns - edit edit remaining columns and increment count
			width = width - 50
			#count compensates for the reduction in width
			count = count + 50

			#check number of columns left to print
			if width < 50:
				over50 = 0

		#less than 50 columns left to print			
		if width != 0:
			for i in range(0, self.height):
				for j in range(0, width):
					sys.stdout.write(board[count + j][i] + " ")
				sys.stdout.write("\n");
			#print column numbers under board
			sys.stdout.write("\n\ncolumns " + str(count) + " to " + str(count+width - 1))
			sys.stdout.write("\n\n")
		sys.stdout.write("\n\n")
			
	def playCol(self, board, colNum, player):
		colNum = int(colNum)
		if colNum > (self.width -1) or colNum < 0:
			print "\nError: Exceeds Board Proportions"
			return " "
		for i in range(0, self.height-1):		
			if board[colNum][i+1] != "*":
				if board[colNum][i] != "*":
					print("\nError: Column Full")
					break
				if player == 1:
					board[colNum][i] = "X"
					results = [colNum, i]
					break	
				else:
					board[colNum][i] = "O"
					results = [colNum, i]
					break	
			#case for when the column is empty
			if i+1 == self.height -1 and board[colNum][i] =="*":
				if player == 1:
					board[colNum][i+1] = "X"
					results = [colNum, i+1]
					break	
				else:
					board[colNum][i+1] = "O"
					results = [colNum, i+1]
					break	
		return results
	
	def checkHor(self, board, rowNum, player):
		count = 0
		#convert player number to board object
		if player == 1:
			player = "X"
		else:
			player = "O"
		
		#count consecutive cells possessed by the player, return 1 for victory
		for i in range(0, self.width):
			if board[i][rowNum] == player:
				count = count + 1
			else:
				count = 0
			if count >= self.connect:
				return 1
			
	def checkVert(self, board, colNum, player):
		count = 0
		#convert plater number to board object
		if player == 1:
			player = "X"
		else:
			player = "O"
		#count consecutive cells possessed by the player, return 1 for victory
		for i in range(0, self.height):
			if board[colNum][i] == player:
				count = count + 1
			else:
				count = 0
			if count >= self.connect:
				return 1

	def checkDiagnalDown(self, board, colNum, rowNum, player):
		count = 0
		offset = 0
		distToEdge = 0
		startPosx = 0
		startPosy = 0
		startIndex = 0
		maximum = 0
		
		#convert player to board object
		if player == 1:
			player = "X"
		else:
			player = "O"	
		
		#set offset to whichever is closer to the top or left edges
		#set our starting x or y position (one of thse will remain 0).
		if colNum <= rowNum:
			offset = colNum
			startPosy = rowNum - offset
		else:
			offset = rowNum
			startPosx = colNum - offset

		#find out how far we can loop
		if (self.width - startPosx) < (self.height - startPosy):
			maximum = self.width
		else:
			maximum = self.height
		#loop along remaining width or height
		for i in range(0, maximum):
			if (startPosy + i) > (self.height  - 1) or (startPosx + i) > (self.width -1):
				break
			#count consecutive cells possessed by the player, return 1 for victory
			if board[startPosx +i][startPosy + i] == player:
				count = count + 1
				if count >= self.connect:
					return 1
			else:
				count = 0

	def checkDiagnalUp(self, board, colNum, rowNum, player):
		count = 0
		offset = 0
		distToEdge = 0
		startPosx = 0
		startPosy = 0
		startIndex = 0
		maximum = 0
		
		#set player to it's board object	
		if player == 1:
			player = "X"
		else:
			player = "O"	
			
		offset = rowNum + colNum
		startPosy = offset
		
		#if out starting y value is greater than the height of the board then
		#set the starting x value to the extra
		if offset > (self.height - 1):
			offset = offset - (self.height - 1)
			startPosx = offset
			startPosy = self.height - 1
		
		#find how far we can loop
		if (self.width - startPosx) < (self.height - startPosy):
			maximum = self.width
		else:
			maximum = self.height
		
		for i in range(0, maximum):
			#catch if out of bounds
			if(startPosy + i) < 0 or (startPosx +i) > (self.width -1):
				break
			#count consecutive cells possessed by the player and return 1 for victory
			if board[startPosx + i][startPosy - i] == player:
				count = count + 1
				if count >= self.connect:
					return 1
			else:
				count = 0

	def saveGame(self, board, player, filename):
		#create object to be saved
		savefile = [board, self.width, self.height, self.connect, player]
		
		#path to the save file directory
		filename = "saveFile/" + filename
		
		#if the save file directory doesn't exist, make it.
		if not os.path.exists("saveFile/"):
			os.makedirs("saveFile/")
		
		#save to the save file
		with open(filename, "wb") as f:
			pickle.dump(savefile, f)
		
		
	def loadGame(self, filename):
		
		#oath to the save file directory
		filename = "saveFile/" + filename
		
		#load to loadfile
		with open(filename, "rb") as f:
			loadfile = pickle.load(f)
		
		return loadfile
	
	#used to determine if user input is a number
	def isNumber(self, num):
		try:
			int(num)
			return True
		except ValueError:
			return False;

if __name__ == '__main__':
	#create a game, a board and a player
	game = connectFour()
	board = [["*" for x in range(game.height)] for y in range(game.width)]
	player = 1	
	
	#for if some1 used -l or --load on launch
	if game.load != "":
		loadfile = game.loadGame(game.load)
		board = loadfile[0]
		game.width = loadfile[1]
		game.height = loadfile[2]
		game.connect = loadfile[3]
		player = loadfile[4]
	
	#sets disp so that we will display our board immediately after loop
	disp = 1
	while(1):
		if(disp == 1):
			game.display(board)
		disp = 1
		print "Type help to learn more about how to play."
		sys.stdout.write("Player " + str(player) + ":")
		
		userInput = sys.stdin.readline(1000).split()
			
		if len(userInput) == 0:
			disp = 0
			continue	

		#exit call		
		if userInput[0] == "exit":
			if len(userInput) == 1:
				break
			else:
				print "Error: Invalid Input"
				disp = 0
				continue

		#print off help statement
		if userInput[0] == "help":
			if len(userInput) == 1:
				print "-Enter column number to play that column."
				print "-Columns are numbered starting from 0."
				print "-Save or load by typing save or load followed by a filename."
				print "-You can display the board at any time by typing display."
				print "-You can exit the game at any time by typing exit."
				print "-Note that the game displays up to 50 columns at a time,"
				print " expanding the window is suggested and should you decide"
				print " to play while using a very large gameboard, it is also"
				print " reccomended that you enable unlimited scrollback on your"
				print " terminal"
			else:
				print "Error: Invalid Input"
			#prevent board from reprinting after command executes
			disp = 0
			continue
	
		#reprint board	
		if userInput[0] == "display":
			if len(userInput) == 1:
				game.display(board)
			else:
				print "Error: Invalid Input"
			#prevent board from reprinting after command executes
			disp = 0
			continue
		
		#save call
		if userInput[0] == "save":
			if len(userInput) == 2:
				game.saveGame(board, player, userInput[1])	
			else:
				print "Error: Invalid Input"
			disp = 0
			continue
		
		#load call
		if userInput[0] == "load":
			if len(userInput) == 2:
				loadfile = game.loadGame(userInput[1])
				if len(loadfile) > 0:
					board = loadfile[0]
					game.width = loadfile[1]
					game.height = loadfile[2]
					game.connect = loadfile[3]
					player = loadfile[4]
					continue
				else:	
					print "Error: Invalid Filename"
					disp = 0
			else:
				print "Error: Invalid Input"
				disp = 0
		
		#check if the user input a number
		if game.isNumber(userInput[0]):
			if len(userInput) == 1:
				results = game.playCol(board, userInput[0], player)
				if len(results) != 2:
					#playCol will have thrown an error
					#prevent board from reprinting	
					disp = 0
					continue
				col = results[0]
				row = results[1]
				
				#check horizontal victory
				checkwin = game.checkHor(board, row, player)
				if checkwin == 1:
					game.display(board)
					print "Player " + str(player) + " Wins!"
					break 
				
				#check vertical victory
				checkwin = game.checkVert(board, col, player)
				if checkwin == 1:
					game.display(board)
					print "Player " + str(player) + " Wins!"
					break 
				
				#check diagnal up victory
				checkwin = game.checkDiagnalUp(board, col, row, player)
				if checkwin == 1:
					game.display(board)
					print "Player " + str(player) + " Wins!"
					break 
				
				#check diagnal down victory
				checkwin = game.checkDiagnalDown(board, col, row, player)
				if checkwin == 1:
					game.display(board)
					print "Player " + str(player) + " Wins!"
					break
			
				#change player	
				if player == 1:
					player = 2
				else:
					player = 1 
			else:
				print "Error: Invalid Input"
				disp = 0

		else:
			print "Error: Invalid Input"
			disp = 0































	
