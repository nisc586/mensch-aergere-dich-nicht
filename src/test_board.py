import pytest
from board import Board
from field import Field
from piece import Piece

PIECES = {
    "green1": Piece("g", 1, Field("A", color="g")),
    "green2": Piece("g", 2, Field("A", color="g")),
    "blue1": Piece("b", 1, Field("A", color="b")),
    "blue2": Piece("b", 2, Field("A", color="b")),
}

#-----------------
# SUGGESTED MOVES
#-----------------

def test_suggest_moves_normal():
    board = Board("g")
    piece = PIECES["green1"]
    suggested_move = board.suggest_moves(piece, 3)
    assert [Field("4")] == suggested_move


def test_leave_base_normal():
    board = Board("gb")
    piece = PIECES["green1"]
    board.move_home(piece)
    suggested_move = board.suggest_moves(piece, 6)
    assert [Field("1")] == suggested_move


def test_no_suggest_end_field_other_color():
    board = Board("rgby")
    piece = PIECES["green1"]
    board.move_piece(piece, Field("19"))
    suggested_moves = board.suggest_moves(piece, 4)
    assert [Field("23")] == suggested_moves


def test_end_field_blocked():
    board = Board("b")
    piece1 = PIECES["blue1"]
    board.move_piece(piece1, Field("B4", color="b"))
    assert [] == board.suggest_moves(piece1, 3)


def test_leave_base_blocked():
    board = Board("g")
    piece = PIECES["green2"]
    assert [] == board.suggest_moves(piece, 6)


#-----------------
# REACHABLE FIELDS
#-----------------

def test_leave_base():
    board = Board("rgby")
    field = Field("A", color="r")
    actual_field = board.find_reachable_fields(field, 6)
    assert {Field("11")} == actual_field


def test_end_field_free():
    board = Board("g")
    available_moves = board.find_reachable_fields(Field("40"), 4)
    assert 2 == len(available_moves)
    assert set([Field("B4", color="g"), Field("4")]) == available_moves


def test_not_leave_base_too_low():
    board = Board("rgby")
    field = Field("A", color="r")
    assert set() == board.find_reachable_fields(field, 3)


if __name__ == "__main__":
    pytest.main()
