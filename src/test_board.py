import pytest
from board import Board
from field import Field
from piece import Piece

PIECES = {
    "green1": Piece("g", 1, Field(0, "g"), Field(1), Field(44, "g")),
    "green2": Piece("g", 2, Field(0, "g"), Field(1), Field(44, "g")),
    "green3": Piece("g", 3, Field(0, "g"), Field(1), Field(44, "g")),
    "green4": Piece("g", 4, Field(0, "g"), Field(1), Field(44, "g")),
    "red1": Piece("r", 1, Field(0, "r"), Field(11), Field(14, "r")),
    "blue1": Piece("b", 1, Field(0, "b"), Field(21), Field(24, "b")),
    "blue2": Piece("b", 2, Field(0, "b"), Field(21), Field(24, "b")),
    "yellow1": Piece("y", 1, Field(0, "y"), Field(31), Field(34, "y"))
}

def test_find_move_normal():
    board = Board("g")
    piece = PIECES["green1"]

    suggested_move = board.find_move(piece, 3)
    assert Field(4) == suggested_move


def test_leave_base_normal():
    board = Board("gb")
    piece = PIECES["green1"]

    board.move_home(piece)
    suggested_move = board.find_move(piece, 6, leave_base=True)

def test_leave_base_blocked():
    board = Board("g")
    piece = PIECES["green2"]

    suggested_move = board.find_move(piece, 6, leave_base=True)
    assert None == suggested_move


def test_end_field_free():
    board = Board("g")
    piece = PIECES["green1"]

    board.move_piece(piece, Field(40))
    suggested_move = board.find_move(piece, 4)
    assert Field(44, "g") == suggested_move, "actual field "+str(suggested_move)


def test_end_field_blocked():
    board = Board("b")
    piece1 = PIECES["blue1"]
    piece2 = PIECES["blue2"]

    board.move_piece(piece1, Field(24, "b"))
    board.move_piece(piece2, Field(21, "b"))
    suggested_move = board.find_move(piece2, 3)
    assert None == suggested_move


def test_no_round_trip():
    board = Board("r")
    piece = PIECES["red1"]

    board.move_piece(piece, Field(8))
    suggested_move = board.find_move(piece, 5)
    assert Field(13, "r") == suggested_move


def test_no_round_trip2():
    board = Board("r")
    piece = PIECES["red1"]

    board.move_piece(piece, Field(9))
    suggested_move = board.find_move(piece, 6)
    assert None == suggested_move, str(suggested_move)


# def test_has_winner():
#     board = Board("g")
#     for name, target in zip(["green1", "green2", "green3", "green4"],
#                          [Field(41, "g"), Field(42, "g"), Field(43, "g"), Field(44, "g")]):
#         board.move_piece(PIECES[name], target)
#     assert board.has_winner()


# def test_has_no_winner():
#     board = Board("g")
#     assert not board.has_winner()


if __name__ == "__main__":
    pytest.main()
