class Field():
    def __init__(self, val, color=""):
        self.value = val
        self.access = color
        self.identifier = f"{val}{color}"
        self.is_end_field = (val > 0) and (color != "")
        return


    def __str__(self):
        return self.identifier

    def __eq__(self, other):
        return self.__str__() == str(other)

    def __hash__(self):
        return hash(self.identifier)
