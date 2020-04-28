gameover = False
empty_cell = ' '
g_row = 0
g_col = 0

def create_board():
	board = []
	for i in range(6):
		new_row = []
		for i in range(7):
			new_row.append(empty_cell)
		board.append(new_row)
	return board

g_board = create_board()

def print_board(board):
	for i in range(6):
		print(board[i])
	print("\n")

print_board(g_board)


def valid_move(board, col, token):
	if not (col >= 1 and col <= 7):
		return False
	elif board[0][col - 1] != empty_cell and board[1][col - 1] != empty_cell and board[2][col - 1] != empty_cell and board[3][col - 1] != empty_cell and board[4][col - 1] != empty_cell and board[5][col - 1]!= empty_cell:
		return False
	else:
		return True

def place_token(board, col, token):
	row = 5
	while board[row][col-1] != empty_cell:
		row = row - 1
	board[row][col-1] = token
	return row

def check_col_win():
	if g_row <= 2 and g_board[g_row + 1][g_col] == token_type and g_board[g_row + 2][g_col] == token_type and g_board[g_row + 3][g_col] == token_type: 
		return True

def check_row_win():
	for i in range(0,4):
		if g_board[g_row][i] != empty_cell and g_board[g_row][i] == g_board[g_row][i + 1]:
			if g_board[g_row][i + 1] == g_board[g_row][i + 2]:
				if g_board[g_row][i + 2] == g_board[g_row][i + 3]:
					return True
	return False

	# for i in range(4):
		# if col[i] == col[i+1]
		#   if col[i+1]== col[i+2]
		#		if col[i+2] == col[i+3]
					# win  break

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


def check_diag_win():
	if g_row == 0 or g_row == 1 or g_row == 2:
		if g_col == 0 or g_col == 1 or g_col == 2:
			if diag_check_down_right():
				return True
			else:
				return False
		elif g_col == 3:
			if diag_check_down_right() or diag_check_down_left():
				return True
			else:
				return False
		elif g_col == 4 or g_col == 5 or g_col == 6:
			if diag_check_down_left():
				return True
			else:
				return False
	elif g_row == 3 or g_row == 4 or g_row == 5:
		if g_col == 0 or g_col == 1 or g_col == 2:
			if diag_check_up_right():
				return True
			else:
				return False
		elif g_col == 3:
			if diag_check_up_right() or diag_check_up_left():
				return True
			else:
				return False
		elif g_col == 4 or g_col == 5 or g_col == 6:
			if diag_check_up_left():
				return True
			else:
				return False


	
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

		
while gameover == False:

	while True:
		input_col = input('What column do you want to place your token in? ')
		if not input_col.isdigit():
			print("This is not a valid entry!")
		else:
			column = int(input_col)
			g_col = column - 1
			break
	token_type = input("What's your token? ")

	if valid_move(g_board, column, token_type):
		g_row = place_token(g_board, column, token_type)
		print_board(g_board) 
	else:
		print("That is not a valid move!")
	
	if check_col_win():
		print('You win vertically!')
		gameover = True
	elif check_row_win():
		print('You win horizontally!')
		gameover = True
	elif check_diag_win():
		print('You win diagonally!')
		gameover = True