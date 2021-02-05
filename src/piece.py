class Piece():
    def __init__(self, color, number, home, start):
        assert color in {"r", "g", "b", "y"}, "invalid color {}".format(color)
        self._color = color
        self._home = home
        self._start = start
        self._number = number


    def get_home(self):
        return self.home


    def get_color(self):
        return self._color


    def __str__(self):
        return "piece-{}{}".format(self._color, self._number)
