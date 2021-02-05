from random import randint

is_running = True
pos = 0
print(f"{pos=}")
turn = 0

MAX_FIELDS = 44
DICE_MIN, DICE_MAX = 1, 6

while is_running:
    dice = randint(DICE_MIN, DICE_MAX)
    print(f"{dice=}", end="\t")
    new_pos = pos + dice
    if new_pos > MAX_FIELDS:
        print("noop")
    elif new_pos == MAX_FIELDS:
        is_running = False
        pos = new_pos
        print("Final spot reached.")
    else:
        pos = new_pos
        print(f"{pos=}")
    turn += 1

print(f"{turn=}")
