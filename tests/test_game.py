import pytest
from mensch.cli import Player
from mensch.game import Game
from mensch.field import Field
from mensch.piece import Piece


def test_winner():
    alice = Player("Alice", "g")
    bob = Player("Bob", "r")
    game = Game([alice, bob])
    game.board.move_piece(Piece("g", 1, Field("A", color="g")), Field("B1", "g"))
    game.board.move_piece(Piece("g", 2, Field("A", color="g")), Field("B2", "g"))
    game.board.move_piece(Piece("g", 3, Field("A", color="g")), Field("B3", "g"))
    game.board.move_piece(Piece("g", 4, Field("A", color="g")), Field("B4", "g"))
    assert game.has_winner()


def test_no_winner():
    alice = Player("Alice", "g")
    bob = Player("Bob", "r")
    game = Game([alice, bob])
    assert not game.has_winner()
