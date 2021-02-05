class Piece():
    def __init__(self, color, home):
        assert color in {"r", "g", "b", "y"}, f"invalid color {color}"
        
        self._color = color
        self.home = home
        self.position = home


    def move_home(self):
        self.position = self.home


    def get_color(self):
        return self._color
