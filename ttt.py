###############################################################################
# Program: The classic TIC TAC TOE game (console based)
# Author : Jawad T. Bin Taufik
# Date   : June 12th, 2024
###############################################################################
# time library was used to create 2 random values for the player's move
import time


# prints the cells on the board, take a list of cells as input
def print_board(mat):
    for row in range(3):
        print(f" {mat[(row*3)+0]} | {mat[(row*3)+1]} | {mat[(row*3)+2]} ")
        if row < 2: 
            print("-----------")


# checks if the input string is valid according to rules or not
def check_if_input_format_is_valid(in_string, c_plr):
    return bool(len(in_string) == 2 and in_string[0] in "123456789" 
                and in_string[1] == c_plr)


# checks if the input was accidentally given to an occupied slot
def check_if_input_cell_is_empty(in_string, in_mat):
    cell = int(in_string[0])-1
    if in_mat[cell] in 'xo':
        print("Warning! Cell already occupied!")
        return False
    else:
        return True


# calculates if any player has already completed any valid line
def weight_calculator(in_mat, c_plr):
    w_mat = [0,0,0,0,0,0,0,0]
    # checks 3 of the rows
    w_mat[0] = 1 if(in_mat[0] == in_mat[1] == in_mat[2] == c_plr) else 0
    w_mat[1] = 1 if(in_mat[3] == in_mat[4] == in_mat[5] == c_plr) else 0
    w_mat[2] = 1 if(in_mat[6] == in_mat[7] == in_mat[8] == c_plr) else 0
    # checkes 3 of the columns
    w_mat[3] = 1 if(in_mat[0] == in_mat[3] == in_mat[6] == c_plr) else 0
    w_mat[4] = 1 if(in_mat[1] == in_mat[4] == in_mat[7] == c_plr) else 0
    w_mat[5] = 1 if(in_mat[2] == in_mat[5] == in_mat[8] == c_plr) else 0
    # checks 2 of the diagonals
    w_mat[6] = 1 if(in_mat[0] == in_mat[4] == in_mat[8] == c_plr) else 0
    w_mat[7] = 1 if(in_mat[2] == in_mat[4] == in_mat[6] == c_plr) else 0
    # when a player achieves any valid line, the sum becomes non zero
    return sum(w_mat)


# prints initial information about the game and randomly chooses the first player
def initials(in_mat):
    print("|------------| TIC * TAC * TOE |-----------|")
    print("Input in any cell as: cell x/o. Ex: 5x or 3o")
    print("Cell mapping is shown below:")
    print_board(in_mat)
    print("--------------------------------------------")
    r_int = int(time.time())
    if r_int % 2 == 0:
        return 'x'
    else:
        return 'o'


# calls current player to give input and returns only if the input is valid
def input_prompt_and_check(c_player, t_mat):

    while(True):
        in_v = input("Enter player 'o': "
                    ) if c_player == 'o' else input("Enter player 'x': ")

        if (check_if_input_format_is_valid(
            in_v, c_player) and check_if_input_cell_is_empty(in_v, t_mat)):
            break
        else:
            print("Give input correctly.")
    return in_v


# updates board with valid inputs, checks for winner, toggle players
def board_update(u_in, b_mat):
    # status flags
    win_plr = '.'
    player = '-'
    # update and print the main matrix
    cell_num = int(u_in[0]) - 1
    cell_val = u_in[1]
    b_mat = b_mat[:cell_num] + cell_val + b_mat[cell_num + 1:]
    print_board(b_mat)
    # check for winner
    x_weight = weight_calculator(b_mat, 'x')
    o_weight = weight_calculator(b_mat, 'o')
    if x_weight > 0:
        win_plr = 'x'
    elif o_weight > 0:
        win_plr = 'o'
    elif all(element in 'xo' for element in b_mat):
        win_plr = None
    # toggle players
    if u_in[1] == 'x':
        player = 'o'
    if u_in[1] == 'o':
        player = 'x'
    return b_mat, player, win_plr


# main function: 
def main():
    # initialize the variables
    game_matrix = '123456789'
    winner = '.'
    user_input = '---'
    current_player = None
    # sets up the game matrix and initial player
    current_player = initials(game_matrix)
    game_matrix = game_matrix.replace('123456789', '         ')
    print(f"Player '{current_player}' gets the first move !! :) ")
    # show empty board initially
    print_board(game_matrix) 
    # game loop
    while(winner == '.'):
        user_input = input_prompt_and_check(current_player, game_matrix)
        game_matrix, current_player, winner = board_update(user_input, game_matrix)
    # announce game result
    if winner is None:
        print('The game is drawn. No winner. ')
    else:
        print(f"player '{winner}' has won the game. Congrats! ")


# run main function with name guard
if __name__ == "__main__":
    main()
