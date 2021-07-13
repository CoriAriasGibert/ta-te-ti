
#----------Global Variables---------------

#------Game board---------

board = [
    "_",
    "_",
    "_",
    "_",
    "_",
    "_",
    "_",
    "_",
    "_",
]

# \\\\\If game stil going//////

game_still_going = True

#++++++ who won or NO_hay_mas_movimientos_posibles?+++++

winner = None

#***** What turn its? *********

current_player = "x"


def display_board():

	print(board[0] + "|", board[1] + "|", board[2])
	print(board[3] + "|", board[4] + "|", board[5])
	print(board[6] + "|", board[7] + "|", board[8])


def play_game():
	#start game with empty boar
	display_board()

	while game_still_going:

		handle_turn(current_player)
		check_if_game_over()
		flip_player()


#------The game has ennded-------
	if winner == "x" or winner == "o":
		print(winner + " GanadorX de un cafecito! ☕️.")
	elif winner == None:
		print("Empate!")


def handle_turn(player):

	position = input("Elige una posicion entre 1 y 9 por favor:  ")
	
	valid=False
	
	while not valid:
	  
	  while position not in ["1","2","3","4","5","6","7","8","9"]:
	    position=input("Posicion invalida, selecciona un numero del 1 al 9: ")
	
	  position = int(position) - 1
	  if board[position] == "_":
	    valid=True
	  else:
	    print("Ese lugar ya esta ocupado, por favor, mueve tu pieza hacia otro lado")
	board[position]=player
	display_board()


def check_if_game_over():
	check_for_winer()
	check_if_NO_hay_mas_movimientos_posibles()


def check_for_winer():
	#set up to globals Variables---------------
	global winner
	#check rows
	row_winner = check_rows()
	#check columns
	columns_winner = check_columns()
	#check diagonals
	diagonals_winner = check_diagonals()

	if row_winner:
		winner = row_winner
	elif columns_winner:
		winner = columns_winner
	elif diagonals_winner:
		winner = diagonals_winner
	else:
		winner = None
	return


def check_rows():
	global game_still_going

	row1 = board[0] == board[1] == board[2] != "_"
	row2 = board[3] == board[4] == board[5] != "_"
	row3 = board[6] == board[7] == board[8] != "_"

	if row1 or row2 or row3:
		game_still_going = False

	if row1:
		return board[0]
	elif row2:
		return board[3]
	elif row3:
		return board[6]
	return


def check_columns():
	global game_still_going

	column1 = board[0] == board[3] == board[6] != "_"
	column2 = board[1] == board[4] == board[7] != "_"
	column3 = board[2] == board[5] == board[8] != "_"

	if column1 or column2 or column3:
		game_still_going = False

	if column1:
		return board[0]
	elif column2:
		return board[1]
	elif column3:
		return board[2]
	return


def check_diagonals():
	global game_still_going

	diagonal1 = board[0] == board[4] == board[8] != "_"
	diagonal2 = board[2] == board[4] == board[6] != "_"

	if diagonal1 or diagonal2:
		game_still_going = False

	if diagonal1:
		return board[0]
	elif diagonal2:
		return board[2]
	return

def check_if_NO_hay_mas_movimientos_posibles():
  global game_still_going
  if "_" not in board:
    game_still_going=False
  return



def flip_player():
	global current_player

	if current_player == "x":
		current_player = "o"
	elif current_player == "o":
		current_player = "x"
	return


play_game()

#board
#display board
#play game
#handle turn
#check win
#check columns
#check diagonals
#check rowms
#check tie
#flip player
