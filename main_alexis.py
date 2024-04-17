from interfaces import Board, Token
from random_strategy import RandomStrategy
import copy

# Create a new board instance
ma_board = Board(6, 7, 4)

# List to hold board instances after each possible move
ma_board_s = []


def test():
    for i in range(7):  # Iterate over each column (0 to 6)
        # Create a deep copy of the original board
        new_board = copy.deepcopy(ma_board)
        # Simulate a move by playing Token.RED in column i
        new_board.play(i, Token.RED)
        # Append the modified board to the list
        ma_board_s.append(new_board)


# Populate the list with modified board instances
test()


# Define a function to format and print board states side by side
def print_boards_side_by_side(boards):
    num_boards = len(boards)
    if num_boards == 0:
        return

    # Get dimensions of each board
    board_height = boards[0].height
    board_width = boards[0].width

    # Print each row of boards side by side
    for row in range(board_height):
        row_strings = []
        for board in boards:
            # Get the tokens for the current row from each board
            row_tokens = [board.box(row, col).value for col in range(board_width)]
            row_strings.append(" ".join(row_tokens))
        # Print the row strings side by side
        print("   ".join(row_strings))


# Print all board states next to each other
print("Board States After Red Player's Moves:")
print_boards_side_by_side(ma_board_s)


# Function to count potential winning lines for a player on a given board
def count_winning_lines(board, player_token):
    height = board.height
    width = board.width
    to_win = board.to_win

    winning_lines_count = 0

    # Check rows
    for row in range(height):
        for start_col in range(width - to_win + 1):
            line_tokens = [board.box(row, start_col + col) for col in range(to_win)]
            if all(token == player_token or token == Token.EMPTY for token in line_tokens):
                winning_lines_count += 1

    # Check columns
    for col in range(width):
        for start_row in range(height - to_win + 1):
            line_tokens = [board.box(start_row + row, col) for row in range(to_win)]
            if all(token == player_token or token == Token.EMPTY for token in line_tokens):
                winning_lines_count += 1

    # Check diagonals (both directions)
    for start_row in range(height - to_win + 1):
        for start_col in range(width - to_win + 1):
            # Check diagonals going from top-left to bottom-right
            line_tokens = [board.box(start_row + k, start_col + k) for k in range(to_win)]
            if all(token == player_token or token == Token.EMPTY for token in line_tokens):
                winning_lines_count += 1

            # Check diagonals going from top-right to bottom-left
            line_tokens_rev = [board.box(start_row + k, start_col + to_win - 1 - k) for k in range(to_win)]
            if all(token == player_token or token == Token.EMPTY for token in line_tokens_rev):
                winning_lines_count += 1

    return winning_lines_count

print(count_winning_lines(ma_board_s[0],Token.RED))