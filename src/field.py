class Field():
    def __init__(self, identifier, color=""):
        self.color = color
        self.identifier = identifier
        self.cost = 1 if not identifier.startswith("A") else 6
        return

    def is_end_field(self):
        return self.identifier.startswith("B")

    def allow_color(self, col):
        """Returns true if a piece of the given color may step on the field."""
        if self.color:
            return self.color == col
        else:
            return True

    def __str__(self):
        return self.identifier

    def __eq__(self, other):
        return self.color == other.color and self.identifier == other.identifier

    def __hash__(self):
        return hash((self.identifier, self.color))
