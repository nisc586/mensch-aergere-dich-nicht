class Field():
    def __init__(self, val):
        self._value = val
        self._id = str(val)
        self._piece = None

    def get_piece(self):
        return self._piece

    def set_piece(self, p):
        self._piece = p

    def is_occupied(self):
        return bool(self._piece)

    def __str__(self):
        return self._id


class EndField(Field):
    def __init__(self, val, access):
        assert access in {"r", "g", "b", "y"}
        self.super().__init__(val)
        self.access = access
        self._id = f"{val}{access}"


class StartField(Field):
    def __init__(self, val, access):
        self.super().__init__(val)
        self.access = access
        self._id = f"{val}{access}"
        self._piece = []


    def get_piece(self):
        try:
            return self._piece.pop()
        except IndexError:
            return None


    def set_piece(self, p):
        self._piece.append(p)
