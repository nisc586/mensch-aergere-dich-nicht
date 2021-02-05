import random

is_running = True
pos1 = 1
pos2 = 0
print(f"{pos1=}, {pos2=}")
turn = 0

MAX_FIELDS = 22
DICE_MIN, DICE_MAX = 1, 6

while is_running:
    occupied = {pos1, pos2}
    if occupied == {MAX_FIELDS, MAX_FIELDS - 1}:
        print("Game over")
        is_running = False

    dice = random.randint(DICE_MIN, DICE_MAX)
    print(f"{dice=}", end="\t")

    new_pos1 = pos1 + dice
    new_pos2 = pos2 + dice

    # Which moves are available?
    legal_moves = set()

    if new_pos1 > MAX_FIELDS:
        print("pice1 can't move")
    else:
        if new_pos1 in occupied:
            print("collision")
        else:
            print("piece1 can reach", new_pos1)
            legal_moves.add(("piece1", new_pos1))


    if new_pos2 > MAX_FIELDS:
        print("piece2 can't move")
    else:
        if new_pos2 in occupied:
            print("collision")
        else:
            print("piece2 can reach", new_pos2)
            legal_moves.add(("piece2", new_pos2))

    print(f"{legal_moves=}")

    # Pick a random move
    if legal_moves:
        piece, n = random.choice(list(legal_moves))
        if piece == "piece1":
            pos1 = new_pos1
        elif piece == "piece2":
            pos2 = new_pos2
        else:
            raise AssertionError("unreachable")
    else:
        print("No moves available")

    print(f"{pos1=}, {pos2=}")
    print()
    turn += 1

print(f"{turn=}")
