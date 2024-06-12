#############################################################################################
# Program: The classic TIC TAC TOE game (terminal based)
# Author: Jawad
# Date: June 12th, 2024
#############################################################################################

import time


def print_board(mat):
    for row in range(3):
        print(f" {mat[(row*3)+0]} | {mat[(row*3)+1]} | {mat[(row*3)+2]} ")
        if row < 2: 
            print("-----------")


def check_if_input_format_is_valid(in_string, c_plr):
    if ((len(in_string) == 2) and (in_string[0] in '123456789') and (in_string[1] == c_plr)):
        return True
    else:
        return False


def check_if_input_cell_is_empty(in_string, in_mat):
    cell = int(in_string[0])-1

    if in_mat[cell] in 'xo':
        print("Warning! Cell already occupied!")
        return False
    else:
        return True


def weight_calculator(in_mat, c_plr):
    w_mat = [0,0,0,0,0,0,0,0]
    #row
    w_mat[0] = 1 if(in_mat[0] == in_mat[1] == in_mat[2] == c_plr) else 0
    w_mat[1] = 1 if(in_mat[3] == in_mat[4] == in_mat[5] == c_plr) else 0
    w_mat[2] = 1 if(in_mat[6] == in_mat[7] == in_mat[8] == c_plr) else 0
    #col
    w_mat[3] = 1 if(in_mat[0] == in_mat[3] == in_mat[6] == c_plr) else 0
    w_mat[4] = 1 if(in_mat[1] == in_mat[4] == in_mat[7] == c_plr) else 0
    w_mat[5] = 1 if(in_mat[2] == in_mat[5] == in_mat[8] == c_plr) else 0
    #diag
    w_mat[6] = 1 if(in_mat[0] == in_mat[4] == in_mat[8] == c_plr) else 0
    w_mat[7] = 1 if(in_mat[2] == in_mat[4] == in_mat[6] == c_plr) else 0

    return sum(w_mat)


def initials(in_mat):
    print("---------------------------------------------")
    print("|             TIC * TAC * TOE               |")
    print("---------------------------------------------")
    print("Input in any cell as: cell x/o. Ex: 5x or 3o")
    print("CELL MAPPING:")
    print_board(in_mat)
    print("---------------------------------------------")
    r_int = int(time.time())

    if r_int % 2 == 0:
        return 'x'
    else:
        return 'o'


def input_prompt_and_check(c_player, t_mat):
    is_correct = False

    while(not is_correct):
        in_v = input("Enter player 'o': ") if c_player == 'o' else input("Enter player 'x': ")

        if (check_if_input_format_is_valid(in_v, c_player) and check_if_input_cell_is_empty(in_v, t_mat)):
            is_correct = True
            break
        else:
            print("Give input correctly.")
    return in_v


def board_update(u_in, i_con, b_mat):
    win_plr = '.'
    player = '-'

    cell_num = int(u_in[0]) - 1
    cell_val = u_in[1]
    b_mat = b_mat[:cell_num] + cell_val + b_mat[cell_num + 1:]

    print_board(b_mat)

    x_weight = weight_calculator(b_mat, 'x')
    o_weight = weight_calculator(b_mat, 'o')

    if x_weight > 0:
        win_plr = 'x'
    if o_weight > 0:
        win_plr = 'o'

    if u_in[1] == 'x':
        player = 'o'
    if u_in[1] == 'o':
        player = 'x'

    return b_mat, player, win_plr


#   MAIN and RUN
def main():

    game_matrix = '123456789' # 9 chars
    winner = '.'
    user_input = '---'
    condition = 'INIT'
    current_player = None

    current_player = initials(game_matrix)
    game_matrix = game_matrix.replace('123456789', '         ')
    print(f"Player '{current_player}' gets the first move !! :) ")

    print_board(game_matrix)  # show empty board at first

    while(winner == '.'):
        user_input = input_prompt_and_check(current_player, game_matrix)
        game_matrix, current_player, winner = board_update(user_input, condition, game_matrix)

    print(f"player '{winner}' has won the game. Congrats! ")



if __name__ == "__main__":
    main()



