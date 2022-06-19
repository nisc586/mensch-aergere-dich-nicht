class Piece():
    def __init__(self, color, number, home):
        assert color in {"r", "g", "b", "y"}, "invalid color {}".format(color)
        self.color = color
        self.home = home
        self.number = number


    def __str__(self):
        return "piece-{}{}".format(self.color, self.number)


    def __eq__(self, other):
        return str(self) == str(other)


    def __hash__(self):
        return hash(str(self))
