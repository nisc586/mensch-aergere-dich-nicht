class Field():
    def __init__(self, val):
        self._value = val
        self._id = str(val)
        self.is_occupied = False


    def __str__(self):
        return self._id


class SpecialField(Field):
    def __init__(self, val, access):
        assert access in {"r", "g", "b", "y"}, "invalid color : {}".format(access)
        self.super().__init__(val)
        self.access = access
        self._id = f"{val}{access}"
