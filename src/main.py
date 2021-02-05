import random

is_running = True
pos1 = 1
pos2 = 0
pos3 = 0
pos4 = 0

print(f"{pos1=}, {pos2=}, {pos3=}, {pos4=}")
turn = 0

MAX_FIELDS = 22
DICE_MIN, DICE_MAX = 1, 6

def find_move(pos, dice, occupied, max_fields):
    """Returns new position if piece can reach it. None otherwise"""
    # Special case: leave home base
    if pos == 0:
        if dice == DICE_MAX:
            new_pos = 1
            if new_pos not in occupied:
                return new_pos
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


while is_running:
    occupied = {pos1, pos2, pos3, pos4}
    if occupied == {MAX_FIELDS, MAX_FIELDS - 1, MAX_FIELDS - 2, MAX_FIELDS - 3}:
        print("Game over")
        break

    dice = random.randint(DICE_MIN, DICE_MAX)
    print(f"{dice=}", end="\t")

    # Which moves are available?
    legal_moves = set()

    new_pos1 = find_move(pos1, dice, occupied, MAX_FIELDS)
    if new_pos1:
        legal_moves.add(("piece1", new_pos1))
    
    new_pos2 = find_move(pos2, dice, occupied, MAX_FIELDS)
    if new_pos2:
        legal_moves.add(("piece2", new_pos2))
    
    new_pos3 = find_move(pos3, dice, occupied, MAX_FIELDS)
    if new_pos3:
        legal_moves.add(("piece3", new_pos3))
    
    new_pos4 = find_move(pos4, dice, occupied, MAX_FIELDS)
    if new_pos4:
        legal_moves.add(("piece4", new_pos4))

    print(f"{legal_moves=}")

    # Pick a random move
    if legal_moves:
        piece, n = random.choice(list(legal_moves))
        if piece == "piece1":
            pos1 = new_pos1
            print(f"{piece} -> {new_pos1}", end="\t")
        elif piece == "piece2":
            pos2 = new_pos2
            print(f"{piece} -> {new_pos2}", end="\t")
        elif piece == "piece3":
            pos3 = new_pos3
            print(f"{piece} -> {new_pos3}", end="\t")
        elif piece == "piece4":
            pos4 = new_pos4
            print(f"{piece} -> {new_pos4}", end="\t")

        else:
            raise AssertionError("unreachable")
    else:
        print("No moves available")

    print(f"{pos1=}, {pos2=}, {pos3=}, {pos4=}")
    print()
    turn += 1

print(f"{turn=}")
