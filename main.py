# global variables
gameover = False 
empty_cell = ' '
g_row = 0
g_col = 0

# creates the connect 4 board by adding new rows and appending empty cells to each row
def create_board(): #TODO: remove hard code
	board = []
	for i in range(6):
		new_row = []
		for i in range(7):
			new_row.append(empty_cell)
		board.append(new_row)
	return board

g_board = create_board()

# prints the game board so that it looks nice
def print_board(board): #TODO: remove hard code 
	for i in range(6):
		print(board[i])
	print("\n")

print_board(g_board)


# checks if it is a valid move, specifically if the column inputted is from 1-7 and if that column is empty; checking for integer is done in player_move
def valid_move(board, col, token): 
	if not (col >= 1 and col <= 7):
		return False
	elif board[0][col - 1] != empty_cell and board[1][col - 1] != empty_cell and board[2][col - 1] != empty_cell and board[3][col - 1] != empty_cell and board[4][col - 1] != empty_cell and board[5][col - 1]!= empty_cell:
		return False
	else:
		return True

# places the token in the place the user asked for
def place_token(board, col, token):
	row = 5
	while board[row][col-1] != empty_cell:
		row = row - 1
	board[row][col-1] = token
	return row

# checks to see if the player has won vertically 
def check_col_win():
	if g_row <= 2 and g_board[g_row + 1][g_col] == token_type and g_board[g_row + 2][g_col] == token_type and g_board[g_row + 3][g_col] == token_type: 
		return True

# checks to see if the player has won horizontally
def check_row_win():
	for i in range(0,4):
		if g_board[g_row][i] != empty_cell and g_board[g_row][i] == g_board[g_row][i + 1]:
			if g_board[g_row][i + 1] == g_board[g_row][i + 2]:
				if g_board[g_row][i + 2] == g_board[g_row][i + 3]:
					return True
	return False

	# pseudo code:
	# for i in range(4):
		# if col[i] == col[i+1]
		#   if col[i+1]== col[i+2]
		#		if col[i+2] == col[i+3]
					# win  break

# the next 4 functions are used for the check_diag_function (which checks if the player has won diagonally); these functions check up or down, to the left or right to see if 3 more of the same token are found. The appropriate function is used based on the location of the token.

def diag_check_down_right():
	for i in range(1,3):
		if g_board[g_row + i][g_col + i] != token_type:
			return False
	return True

def diag_check_down_left():
	for i in range(1,3):
		if g_board[g_row + i][g_col - i] != token_type:
			return False
	return True

def diag_check_up_right():
	for i in range(1,3):
		if g_board[g_row - i][g_col + i] != token_type:
			return False
	return True

def diag_check_up_left():
	for i in range(1,3):
		if g_board[g_row - i][g_col - i] != token_type:
			return False
	return True


# using the 4 above functions, checks to see if the player has won diagonally
def check_diag_win():

	if g_row == 0 or g_row == 1 or g_row == 2:
		if g_col == 0 or g_col == 1 or g_col == 2:
			if diag_check_down_right():
				return True
		elif g_col == 3:
			if diag_check_down_right() or diag_check_down_left():
				return True
		elif g_col == 4 or g_col == 5 or g_col == 6:
			if diag_check_down_left():
				return True
			
	elif g_row == 3 or g_row == 4 or g_row == 5:
		if g_col == 0 or g_col == 1 or g_col == 2:
			if diag_check_up_right():
				return True
		elif g_col == 3:
			if diag_check_up_right() or diag_check_up_left():
				return True
		elif g_col == 4 or g_col == 5 or g_col == 6:
			if diag_check_up_left():
				return True
	
	return False


	# pseudo code:
	#if row == 0, 1, or 2:
		# if column == 0, 1, or 2:
			#for i in range(3):
				# if row -1, col +1 != same
					#return false 
			#return true
		# if column == 3 check left and right
		# if column == 4, 5, or 6 check left (col - 1)
	# if row == 3, 4, or 5:
		# if column == 0, 1, or 2:
			# for i in range(3):
				# if row + 1, col + 1 != same
					# return false 
			# return true
		# if column == 3 check left and right
		# if column == 4, 5, or 6 check left (col - 1)


# this is everything that happens when it's a player's turn; it begins by rejecting any inputs that aren't integers (not done in valid move function; didn't work) and then checking validity further with vaild move function. Then it places the token and finally checks if the player can win any of the 3 ways, and if they can, tells them so and ends the game
def player_move():
	global g_col, g_row, gameover
	while True:
		input_col = input('Player {}: What column do you want to place your token in? '.format(player_num))
		if not input_col.isdigit():
			print("This is not a valid entry!")
		else:
			column = int(input_col)
			g_col = column - 1
			break

	if valid_move(g_board, column, token_type):
		g_row = place_token(g_board, column, token_type)
		print_board(g_board) 
	else:
		print("That is not a valid move!")
	
	if check_col_win():
		print('Player {} wins vertically!'.format(player_num))
		gameover = True
	elif check_row_win():
		print('Player {} wins horizontally!'.format(player_num))
		gameover = True
	elif check_diag_win():
		print('Player {} wins diagonally!'.format(player_num))
		gameover = True


# implements the player_move function by making it repeat twice (once per player) and changing the token and player number accordingly
while gameover == False:
	player_num = 1
	while player_num < 3 and gameover == False:
		if player_num == 1:
			token_type = 'X'
		else:
			token_type = 'O'
		player_move()
		player_num += 1

	