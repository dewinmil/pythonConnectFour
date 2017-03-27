import sys
import getopt

class Flags:
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
					sys.stdout.write(board[count+1][i] + " ")
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
					sys.stdout.write(board[count+1][i] + " ")
				sys.stdout.write("\n");
			sys.stdout.write("\n\ncolumns " + str(count) + " to " + str(count+49))
			sys.stdout.write("\n\n")
		sys.stdout.write("\n\n")
			
	







if __name__ == '__main__':
	flags = Flags();
	board = [["*" for x in range(flags.height)] for y in range(flags.width)]
	flags.Display(board)




