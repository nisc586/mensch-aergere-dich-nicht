class Piece():
    def __init__(self, color, number, home, start, finish):
        assert color in {"r", "g", "b", "y"}, "invalid color {}".format(color)
        self.color = color
        self.home = home
        self.start = start
        self.finish = finish
        self.number = number


    def __str__(self):
        return "piece-{}{}".format(self.color, self.number)


    def __eq__(self, other):
        return str(self) == str(other)


    def __hash__(self):
        return hash(str(self))


if __name__ == "__main__":
    piece = Piece("g", 1, None, None)
    print(piece)
