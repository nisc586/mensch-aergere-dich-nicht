class Field():
    def __init__(self, identifier, *,color="", cost_to_leave=1):
        self.color = color
        self.identifier = identifier
        self.cost = cost_to_leave
        return

    def is_end_field(self):
        return self.identifier.startswith("B")

    def __str__(self):
        return self.identifier

    def __eq__(self, other):
        return self.color == other.color and self.identifier == other.identifier

    def __hash__(self):
        return hash((self.identifier, self.color))
