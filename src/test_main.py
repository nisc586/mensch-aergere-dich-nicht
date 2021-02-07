import pytest
from main import Player, Main

def test_rename(capsys):
    main = Main()
    main.rename_player("Alice", "Alex")
    out, err = capsys.readouterr()
    assert {Player("Alex", "g"), Player("Bob", "r")} == main.players
    assert "Renamed: Player(name='Alice', color='g')\n" == out


def test_rename_no_such(capsys):
    main = Main()
    main.rename_player("Otto", "Oswald")
    out, err = capsys.readouterr()
    assert "No such player\n" == out


def test_add(capsys):
    main = Main()
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
    main = Main()
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
    main = Main()
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
    main = Main()
    main.remove_player("Bob")
    out, er = capsys.readouterr()
    assert "Can't have less than 2 players\n" == out


def test_random_color():
    main = Main()
    col = main.random_color()
    assert(("b" == col) or ("y" == col))


def test_random_color_negative():
    main = Main()
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
