from board import Board
import random
import time

DICE_MIN, DICE_MAX = 1, 6

board = Board()
is_running = True
turn = 0


while is_running:
    if board.has_winner():
        print("Game over.")
        break

    dice = random.randint(DICE_MIN, DICE_MAX)
    print(f"{dice=}")

    # Which moves are available?
    legal_moves = board.collect_legal_moves(dice, DICE_MAX)

    for piece, new_position in legal_moves:
        print(piece, "->", new_position)
    print()

    # Pick a random move
    if legal_moves:
        piece, new_pos = random.choice(legal_moves)
        print(piece, "->", new_pos)
        board.move_piece(piece, new_pos)
    else:
        print("No moves available")

    turn += 1
    time.sleep(1)
    print()

print(f"{turn=}")
