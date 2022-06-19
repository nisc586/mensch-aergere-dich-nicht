import pytest
from mensch.cli import Player, CLI

def test_rename(capsys):
    main = CLI()
    main.rename_player("Alice", "Alex")
    out, err = capsys.readouterr()
    assert {Player("Alex", "g"), Player("Bob", "r")} == main.players
    assert "Renamed: Player(name='Alice', color='g') to Player(name='Alex', color='g')\n" == out


def test_rename_no_such(capsys):
    main = CLI()
    main.rename_player("Otto", "Oswald")
    out, err = capsys.readouterr()
    assert "No such player\n" == out


def test_add(capsys):
    main = CLI()
    main.add_player("Carl")
    out, err = capsys.readouterr()
    assert(
        (Player("Carl", "b") in main.players)
        or (Player("Carl", "y") in main.players)
    )
    assert(
        "Added: Player(name='Carl', color='y')\n" == out
        or "Added: Player(name='Carl', color='b')\n" == out
    )


def test_no_add(capsys):
    main = CLI()
    main.players = {
        Player("Alice", "g"),
        Player("Bob", "r"),
        Player("Carl", "y"),
        Player("Donna", "b")
    }
    main.add_player("Eric")
    out, err = capsys.readouterr()
    assert "Can't have more than 4 players\n" == out


def test_remove(capsys):
    main = CLI()
    main.players = {
        Player("Alice", "g"),
        Player("Bob", "r"),
        Player("Carl", "y"),
        Player("Donna", "b")
    }
    main.remove_player("Donna")
    out, err = capsys.readouterr()
    assert "Removed: Player(name='Donna', color='b')\n" == out
    assert {Player("Alice", "g"), Player("Bob", "r"), Player("Carl", "y")} == main.players


def test_no_remove(capsys):
    main = CLI()
    main.remove_player("Bob")
    out, er = capsys.readouterr()
    assert "Can't have less than 2 players\n" == out


def test_random_color():
    main = CLI()
    col = main.random_color()
    assert(("b" == col) or ("y" == col))


def test_random_color_negative():
    main = CLI()
    main.players = {
        Player("Alice", "g"),
        Player("Bob", "r"),
        Player("Carl", "y"),
        Player("Donna", "b")
    }
    with pytest.raises(IndexError):
        main.random_color()


if __name__ == "__main__":
    pytest.main()
