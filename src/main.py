import random


MAX_FIELDS = 22
DICE_MIN, DICE_MAX = 1, 6


def find_move(pos, dice, occupied, max_fields):
    """Returns new position if piece can reach it. None otherwise"""
    # Special case: leave home base
    if pos == 0:
        if dice == DICE_MAX:
            new_pos = 1
            if new_pos not in occupied:
                # Can leave home base
                return new_pos
            else:
                # Field 1 occupied
                return
        else:
            return

    new_pos = pos + dice
    if new_pos > max_fields:
        # piece can't move
        return
    elif new_pos in occupied:
        # collision
        return
    else:
        # can move
        return new_pos


def collect_legal_moves(pieces, dice, occupied, max_fields):
    """Returns all possible moves for given pieces. May be empty set"""
    moves = set()
    for piece, pos in pieces.items():
        new_pos = find_move(pos, dice, occupied, max_fields)
        if new_pos:
            moves.add((piece, new_pos))
    return moves


is_running = True
pieces = {"piece1": 1, "piece2": 0, "piece3": 0, "piece4": 0}
turn = 0


while is_running:
    occupied = set(pieces.values())
    if occupied == {MAX_FIELDS, MAX_FIELDS - 1, MAX_FIELDS - 2, MAX_FIELDS - 3}:
        print("Game over")
        break

    dice = random.randint(DICE_MIN, DICE_MAX)
    print(f"{dice=}", end="\t")

    # Which moves are available?
    legal_moves = collect_legal_moves(pieces, dice, occupied, MAX_FIELDS)

    print(f"{legal_moves=}")

    # Pick a random move
    if legal_moves:
        piece, new_pos = random.choice(list(legal_moves))

        if piece in pieces:
            pieces[piece] = new_pos
            print(piece, "->", new_pos, end="\t")
        else:
            raise AssertionError("unreachable")
    else:
        print("No moves available")

    print(pieces)
    print()

print(f"{turn=}")
